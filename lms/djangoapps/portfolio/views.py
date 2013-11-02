from courseware.courses import (get_courses, get_course_with_access,
                                get_courses_by_university, sort_by_announcement)
from mitxmako.shortcuts import render_to_response
from django.conf import settings
from courseware.module_render import toc_for_course, get_module_for_descriptor
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django_future.csrf import ensure_csrf_cookie
from django.views.decorators.cache import cache_control
from portfolio_utils import Get_accept_upload, get_module_combinedopenended

def about_me(request,course_id):
    course = get_course_with_access(request.user, course_id, 'load')
    return render_to_response('portfolio/about_me.html', {'course':course})

@login_required
@ensure_csrf_cookie
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def journal_and_reflections(request,course_id):
    course = get_course_with_access(request.user, course_id, 'load')
    '''
    section_descriptor = modulestore().get_instance(course.id, course.location, depth=None)
    field_data_cache = FieldDataCache.cache_for_descriptor_descendents(
                course_id, request.user, section_descriptor, depth=None)
    
    location = Location(course.location)
    descriptor = modulestore().get_orphans(course_id, location, depth=None)
    content=[]
    for x in range(len(descriptor)):
        module = get_module_for_descriptor(request.user, request, descriptor[x], field_data_cache, course_id,
                                         position=None, wrap_xmodule_display=True, grade_bucket_type=None,
                                         static_asset_path='')
        #content.append(module.runtime.render(module, None, 'student_view').content)
        con = module.runtime.render(module, None, 'student_view').content
        upload_attr = Get_accept_upload()
        upload_attr.feed(con)
        import logging
        log = logging.getLogger("tracking")
        log.debug("collection===============================\n:"+str(upload_attr.urls[0])+"\n===========================")
        if upload_attr.urls[0]=="False":
            content.append(con)
    '''
    content = get_module_combinedopenended(request,course,course_id,"False")
    return render_to_response('portfolio/journal_and_reflections.html', {'course':course, 'csrf': csrf(request)['csrf_token'],
        'content':content,'xqa_server': settings.MITX_FEATURES.get('USE_XQA_SERVER', 'http://xqa:server@content-qa.mitx.mit.edu/xqa')})

def uploads(request,course_id):
    course = get_course_with_access(request.user, course_id, 'load')
    content = get_module_combinedopenended(request,course,course_id,"True")
    return render_to_response('portfolio/uploads.html', {'course':course, 'csrf': csrf(request)['csrf_token'],
        'content':content,'xqa_server': settings.MITX_FEATURES.get('USE_XQA_SERVER', 'http://xqa:server@content-qa.mitx.mit.edu/xqa')})



