__author__ = 'Alexis'
from django.conf.urls import patterns, include, url
from tastypie.api import Api
from blog_api.api import PostResource

#v1_api = Api(api_name='v1')
#v1_api.register(PostRessource())

postressource = PostResource()

urlpatterns = patterns("",
    url(r'^', include(postressource.urls))
    #url(r'^', include(v1_api.urls))
)
