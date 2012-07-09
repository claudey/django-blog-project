from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment 


def post_list(request):
    post_list = Post.objects.all()
    
    print type(post_list)
    print post_list
#	response = 
    
    return post_list

def post_detail(request, id, showComments=False):
    pass
    
def post_search(request, term):
    return HttpResponse()

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') 
