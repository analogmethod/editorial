from mezzanine.blog.models import BlogPost
from django.shortcuts import render_to_response
from django.template import RequestContext
def homepage(request):
	b = BlogPost.objects.order_by('publish_date')[:10]
	return render_to_response('index.html', {'blogs':b}, context_instance=RequestContext(request))
