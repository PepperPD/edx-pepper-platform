from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django_future.csrf import ensure_csrf_cookie
from mitxmako.shortcuts import render_to_response

import student.views
import branding
import courseware.views
from mitxmako.shortcuts import marketing_link
from util.cache import cache_if_anonymous

@ensure_csrf_cookie
@cache_if_anonymous
def index(request):
    '''
    Redirects to main page -- info page if user authenticated, or marketing if not
    '''
#@begin:Able to visit homepage after login
#@date:2013-11-02        
    # if settings.COURSEWARE_ENABLED and request.user.is_authenticated():
    #     return redirect(reverse('dashboard'))
#@end    

    if settings.MITX_FEATURES.get('AUTH_USE_MIT_CERTIFICATES'):
        from external_auth.views import ssl_login
        return ssl_login(request)
    if settings.MITX_FEATURES.get('ENABLE_MKTG_SITE'):
        return redirect(settings.MKTG_URLS.get('ROOT'))

    university = branding.get_university(request.META.get('HTTP_HOST'))
    if university == 'edge':
        return render_to_response('university_profile/edge.html', {})

    #  we do not expect this case to be reached in cases where
    #  marketing and edge are enabled
    return student.views.index(request, user=request.user)

@ensure_csrf_cookie
@cache_if_anonymous
def courses(request):
    """
    Render the "find courses" page. If the marketing site is enabled, redirect
    to that. Otherwise, if subdomain branding is on, this is the university
    profile page. Otherwise, it's the edX courseware.views.courses page
    """
    if settings.MITX_FEATURES.get('ENABLE_MKTG_SITE', False):
        return redirect(marketing_link('COURSES'), permanent=True)

    university = branding.get_university(request.META.get('HTTP_HOST'))
    if university == 'edge':
        return render_to_response('university_profile/edge.html', {})

    #  we do not expect this case to be reached in cases where
    #  marketing and edge are enabled
    return courseware.views.courses(request)

#@begin:View of the new added page
#@date:2013-11-02        
@ensure_csrf_cookie
@cache_if_anonymous
def what_is(request):
     return render_to_response('what_is.html', {})

@ensure_csrf_cookie
@cache_if_anonymous
def districts(request):
     return render_to_response('districts.html', {})

@ensure_csrf_cookie
@cache_if_anonymous
def intro(request):
     return render_to_response('intro.html', {})

@ensure_csrf_cookie
@cache_if_anonymous
def intro_research(request):
     return render_to_response('intro_research.html', {})

@ensure_csrf_cookie
@cache_if_anonymous
def intro_ourteam(request):
     return render_to_response('intro_ourteam.html', {})

@ensure_csrf_cookie
@cache_if_anonymous
def intro_faq(request):
    return render_to_response('intro_faq.html', {})

@ensure_csrf_cookie
@cache_if_anonymous
def _contact(request):
    return render_to_response('_contact.html', {})
#@end

#@begin:View of the new added page
#@date:2013-11-21  
@ensure_csrf_cookie
@cache_if_anonymous
def tos(request):
    return render_to_response('static_templates/tos.html', {})

@ensure_csrf_cookie
@cache_if_anonymous
def privacy(request):
    return render_to_response('static_templates/privacy.html', {})
#@end