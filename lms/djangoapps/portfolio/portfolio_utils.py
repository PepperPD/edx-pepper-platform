from xmodule.modulestore.django import modulestore
from xmodule.modulestore import Location
from courseware.module_render import toc_for_course, get_module_for_descriptor
from courseware.model_data import FieldDataCache
from sgmllib import SGMLParser

class Get_accept_upload(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.urls=[]
    def start_section(self, attrs):
        attr = [v for k, v in attrs if k=='data-accept-file-upload']
        if attr:
        	self.urls.extend(attr)
        else:
            self.urls.append("null")

def get_module_combinedopenended(request, course, course_id, isupload):
    section_descriptor = modulestore().get_instance(course.id, course.location, depth=None)
    field_data_cache = FieldDataCache.cache_for_descriptor_descendents(course_id, request.user, section_descriptor, depth=None)
    location = Location(course.location)
    descriptor = modulestore().get_orphans(course_id, location, depth=None)
    content = []
    for x in range(len(descriptor)):
        module = get_module_for_descriptor(request.user, request, descriptor[x], field_data_cache, course_id,
                                         position=None, wrap_xmodule_display=True, grade_bucket_type=None,
                                         static_asset_path='')
        con = module.runtime.render(module, None, 'student_view').content
        import logging
        log = logging.getLogger("tracking")
        #log.debug("collection===============================\n:"+str(con)+"\n===========================")
        upload_attr = Get_accept_upload()
        upload_attr.feed(con)
        if upload_attr.urls[0] == isupload:
        	content.append(con)
    return content