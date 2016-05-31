from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Post(models.Model):
	#author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	photo = models.ImageField(blank=True,null=True)
	hit=models.IntegerField(default=0,blank=True,null=True)
	likes = models.PositiveIntegerField(default=0)

	@property
	def total_likes(self):
	    return self.likes.count()
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()


	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('bamboo:post_detail', args=[self.id])



	
class Comment(models.Model):
	post = models.ForeignKey('bamboo.Post', related_name='comments')
	#author = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True)
	author = models.ForeignKey(settings.AUTH_USER_MODEL,null=True)
	message = models.TextField()
	created_at = models.DateTimeField(default=timezone.now)
	anonymous=models.IntegerField(default=0,blank=True,null=True)

	def get_absolute_url(self):
		return reverse('bamboo:post_detail', args=[self.post_id])
	def __str__(self):
		return self.text




class User(models.Model):
	def get_absolute_url(self):
		return reverse('bamboo:post_list')




