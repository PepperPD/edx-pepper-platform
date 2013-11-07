from mitxmako.shortcuts import render_to_response, render_to_string
from django.contrib.auth.models import User
from django.db import IntegrityError, transaction
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django_future.csrf import ensure_csrf_cookie
from mitxmako.shortcuts import render_to_response

from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotAllowed, Http404

import student.views
import branding
import courseware.views
from mitxmako.shortcuts import marketing_link
from util.cache import cache_if_anonymous
import json

from student.models import Contract,UserProfile,Registration,District

from django import forms
import csv

def index(request):
    return render_to_response('manage/district.html', {"districts":District.objects.all(),"ui":"list"})

def create(request):
    return render_to_response('manage/district.html', {"districts":District.objects.all(),"district_from":True})

def modify(request,district_id=''):
    from student.models import District
    district={}
    if district_id:
        c=District.objects.get(id=district_id)
        district['id']=c.id
        district['name']=c.name
        district['district_id']=c.district_id
        district['term_months']=c.term_months
        district['licenses']=c.licenses
    return render_to_response('manage/district.html',
                              {"districts":District.objects.all(),
                               "district":district,
                               "district_from":True})

@ensure_csrf_cookie
@cache_if_anonymous
def import_user(request):
    district={}
    return render_to_response('manage/district.html', {"districts":District.objects.all(), "import_from":True})

@ensure_csrf_cookie
@cache_if_anonymous
def submit(request):
    if not request.user.is_authenticated:
        raise Http404
    district_id = request.POST['district_id']
    name = request.POST['name']
    district_id = request.POST['district_id']
    term_months = request.POST['term_months']
    licenses = request.POST['licenses']
    try:
        c=District()
        c.id=district_id
        c.name=name
        c.district_id=district_id
        c.term_months=term_months
        c.licenses=licenses
        c.status='ALLOW'
        c.save()
    except Exception:
        transaction.rollback()
        return HttpResponse(json.dumps({'success': False,'error':'?'}))
    return HttpResponse(json.dumps({'success': True}))

DISTRICT_CVS_COL_DISTRICT_ID=0
DISTRICT_CVS_COL_DISTRICT_ID=1
DISTRICT_CVS_COL_EMAIL=2
DISTRICT_CVS_COL_USERNAME=3
DISTRICT_CVS_COUNT_COL=4  

def validate_cvs_line(line):
    district_id=line[DISTRICT_CVS_COL_DISTRICT_ID]
    district_id=line[DISTRICT_CVS_COL_DISTRICT_ID]
    email=line[DISTRICT_CVS_COL_EMAIL]
    username=line[DISTRICT_CVS_COL_USERNAME]

    exist=False
    
    # check field count
    n=0
    for item in line:
        if len(item.strip()):
            n=n+1
    if n != DISTRICT_CVS_COUNT_COL:
        raise Exception("Wrong fields count.")

    # check district_id
    # don't use objects.get, that throw 'District matching query does not exist'
    if len(District.objects.filter(id=int(district_id)))!=1:
        raise Exception("Invalide district id.")

    # check district_id
    # don't use objects.get, that throw 'District matching query does not exist'
    if len(District.objects.filter(id=int(district_id)))!=1:
        raise Exception("Invalide district id.")    

    if len(User.objects.filter(username=username,email=email)) == 0:
        # check email
        if len(User.objects.filter(email=email)) > 0:
            raise Exception("An account with the Email '{email}' already exists.".format(email=email))

        # check username
        if len(User.objects.filter(username=username)) > 0:
            raise Exception("An account with the Public Username '{username}' already exists.".format(username=username))
    else:
        exist=True

    return exist

def district_users(reqest):
    pass

@ensure_csrf_cookie
@cache_if_anonymous  
# http://www.cnblogs.com/yijun-boxing/archive/2011/04/18/2020155.html
def import_user_submit(request):  
    message={}
    if request.method == 'POST':
        f=request.FILES['file']
        dialect = csv.Sniffer().sniff(f.read(1024), delimiters=";,")
        f.seek(0)
        r=csv.reader(f,dialect)
        try:
            count_success=0
            count_exist=0;
            for i,line in enumerate(r):
                exist=validate_cvs_line(line)

                if(exist):
                    count_exist=count_exist+1
                    continue
        
                district_id=line[DISTRICT_CVS_COL_DISTRICT_ID]
                district_id=line[DISTRICT_CVS_COL_DISTRICT_ID]
                email=line[DISTRICT_CVS_COL_EMAIL]
                username=line[DISTRICT_CVS_COL_USERNAME]
                user = User(username=username, email=email, is_active=True)
                user.set_password(username)
                registration = Registration()
                user.save()
                
                # try:
                #     user.save()
                # except IntegrityError:
                #     if len(User.objects.filter(username=username)) > 0:
                #         raise Exception("An account with the Public Username '{username}' already exists.".format(username=username))
                #     if len(User.objects.filter(email=email)) > 0:
                #         raise Exception("An account with the Email '{email}' already exists.".format(email=email))
                
                registration.register(user)
                profile=UserProfile(user=user)
                profile.district_id=district_id
                profile.district_id=district_id
                profile.email=email
                profile.username=username
                profile.reg_status='ToInvite'
                profile.save()
                
                reg = Registration.objects.get(user=user)
                d = {'name': profile.name, 'key': reg.activation_key}
                
                subject = render_to_string('emails/activation_email_subject.txt', d)
                subject = ''.join(subject.splitlines())
                message = render_to_string('emails/activation_email.txt', d)
                
                try:
                    _res = user.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)
                except:
                    log.warning('Unable to send reactivation email', exc_info=True)
                    raise Exception(_('Unable to send reactivation email'))

                # todo: store if the email is sent
                
                count_success=count_success+1
                transaction.commit()

        except Exception as e:
            transaction.rollback()
            message={'success': False,'message':'Import error: %s At cvs line: %s, Nobody impored.' % (e,n)}

        message={"success": True,
            "message":"Success! %s users imported." % (count_success),
            "count_exist":count_exist,
            "count_success":count_success,
            "faile_list":faile_list
            }            

    return HttpResponse(json.dumps(message))

@ensure_csrf_cookie
@cache_if_anonymous
def submit_district(request):
    if not request.user.is_authenticated:
        raise Http404
    district_id = request.POST['district_id']
    name = request.POST['name']
    district_id = request.POST['district_id']
    term_months = request.POST['term_months']
    licenses = request.POST['licenses']
    try:
        from student.models import District
        c=District()
        if len(district_id):
            c.id=district_id
        c.name=name
        c.district_id=district_id
        c.state_id=state_id
        c.term_months=term_months
        c.licenses=licenses
        c.status='ALLOW'
        c.save()
    except Exception as e:
        transaction.rollback()
        return HttpResponse(json.dumps({'success': False,'error': "%s" % e}))
    return HttpResponse(json.dumps({'success': True}))

