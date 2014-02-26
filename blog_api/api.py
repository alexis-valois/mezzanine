__author__ = 'Alexis'
from tastypie.resources import ModelResource
from mezzanine.blog.models import BlogPost

class PostResource(ModelResource):
    class Meta:
        queryset = BlogPost.objects.all()
        resource_name = "post"
