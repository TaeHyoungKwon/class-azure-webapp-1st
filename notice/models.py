from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	name = models.CharField(max_length=50, blank=True)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)
	photo = models.ImageField(blank=True,null=True)
	hit=models.IntegerField(default=0,blank=True,null=True)




class Comment(models.Model):
	post = models.ForeignKey('notice.Post', related_name='comments')
	message = models.TextField()
	created_at = models.DateTimeField(default=timezone.now)

	def get_absolute_url(self):
		return reverse('notice:post_detail', args=[self.post_id])
