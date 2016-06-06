from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy,reverse
from django.contrib.auth.models import User




class Post(models.Model):
	user = models.ForeignKey('auth.User',related_name='goodcolumn_post_user')
	title = models.CharField(max_length=200)
	message = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	photo = models.ImageField(blank=True,null=True)
	hit=models.IntegerField(default=0,blank=True,null=True)
	likes = models.PositiveIntegerField(default=0)
	link = models.CharField(max_length=200,blank=True,null=True)



	@property
	def total_likes(self):
	    return self.likes.count()	

	def publish(self):
		self.published_date = timezone.now()
		self.save()


	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('goodcolumn:post_detail', args=[self.id])




class Comment(models.Model):
	post = models.ForeignKey('goodcolumn.Post', related_name='goodcolumn_comments')
	#author = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, related_name='comments_author')
	comment_user = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, related_name='goodcolumn_comments_author')
	comment_message = models.TextField()
	comment_created_date = models.DateTimeField(default=timezone.now)

	def get_absolute_url(self):
		return reverse('goodcolumn:post_detail', args=[self.post_id])
	
	def __str__(self):
		return self.comment_message

