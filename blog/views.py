from django.template import Context, loader
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Post, Comment
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

def post_list(request):
	allPosts = Post.objects.all()
	t = loader.get_template('blog/post_list.html')
	c = Context({'posts':allPosts})
	return HttpResponse(t.render(c))
	
class CommentForm():
	class Meta():
		exclude=['post']

@csrf_exempt
def post_detail(request, id, showComments=False):
	onePost = Post.objects.get(pk=id)
	if request.method == 'POST':
		comment = Comment(post=target_post)
		form = CommentForm(request.POST, instance = comment)
		if form.id_valid():
			form.save()
		return HttpResponseRedirect(request.path)
	else:
		form = CommentForm()
	oneComment = onePost.comments.all()
#	eachComment = ''
#	for x in oneComment:
#		eachComment += '<ol>'+str(x.body)+'</ol>'
#	return HttpResponse('<h3>Post: </h3><br/> <ul>'+str(onePost)+'</ul> <br/><h3>Comments: </h3>'+eachComment)
	return render_to_response('blog/post_details.html',{'posts':termRetrieve, 'comments':oneComment, 'form':form})
    
def post_search(request, term):
	termRetrieve = Post.objects.filter(body__contains = term)
	return render_to_response('blog/post_search.html',{'posts':termRetrieve, 'term':term})

def home(request):
	return render_to_response('blog/base.html', {})
'''    print 'it works'
    return HttpResponse('hello world. Ete zene?') '''