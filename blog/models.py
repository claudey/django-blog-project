from django.db import models
from django.contrib import admin

# Add more models here.
class Post(models.Model):
	title = models.CharField(max_length=60)
	body = models.TextField()
	author = models.CharField(max_length=60)
	post = models.CharField(max_length=60)
	created = models.DateField(auto_now = True, auto_now_add = True)
	updated = models.DateField(auto_now = True, auto_now_add = True)
		
	def __unicode__(self):
		return self.title
		
def title_first_60(self):
	return title[:60]

class Comment(models.Model):
	body = models.TextField()
	author = models.CharField(max_length=60)
	created = models.DateField(auto_now = True, auto_now_add = True)
	updated = models.DateField(auto_now = True, auto_now_add = True)
	post = models.ForeignKey(Post, related_name='comments')
	list_display = ('title_first_60')
	
	def __unicode__(self):
		return self.body
		
class CommentInline(admin.TabularInline):
	model = Comment
		
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'created', 'updated')
	search_fields = ('title', 'body')
	list_filter = ('created', 'author')
	ordering = ('title', 'post')
	inlines = [CommentInline]
	
	def __unicode__(self):
		return self.title
		
class CommentAdmin(admin.ModelAdmin):
	list_display = ('post', 'author')
	list_filter = ('created', 'author')
	
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)