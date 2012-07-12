from django.template import Context, loader
from django.http import HttpResponse
from models import Post, Comment

def post_list(request):
	allPosts = Post.objects.all()
	myhtml = ''
	for pst in allPosts:
		myhtml += '<ul>'+str(pst)+'</ul>'
	return HttpResponse(myhtml)


def post_detail(request, id, showComments=False):
	onePost = Post.objects.get(pk=id)
	oneComment = onePost.comments.all()
	eachComment = ''
#	thishtml = str(onePost) + str(onePost.body)
	thishtml = onePost
	for x in oneComment:
		eachComment += x.body
	return HttpResponse(thishtml, eachComment)	

    
def post_search(request, term):
	termRetrieve = Post.objects.filter(body__contains = term)
	html = ''
	for a in termRetrieve:
		html += '<ul>'+str(a)+'</ul>'
	return HttpResponse(html)
#	return HttpResponse(html)

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') 