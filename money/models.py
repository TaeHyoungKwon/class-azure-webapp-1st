from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy,reverse
from django.contrib.auth.models import User
import django.db.models.deletion




class Post(models.Model):
	user = models.ForeignKey('auth.User',related_name='money_post_user')
	title = models.CharField(max_length=200)
	message = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	photo = models.ImageField(blank=True,null=True)
	hit=models.IntegerField(default=0,blank=True,null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()


	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('money:post_detail', args=[self.id])




class Comment(models.Model):
	post = models.ForeignKey('money.Post', related_name='comments')
	comment_user = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, related_name='money_comment_user')
	comment_message = models.TextField()
	comment_created_date = models.DateTimeField(default=timezone.now)

	def get_absolute_url(self):
		return reverse('money:post_detail', args=[self.post_id])
	
	def __str__(self):
		return self.comment_message

