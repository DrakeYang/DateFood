from django.db import models
from django.utils import timezone


class Post(models.Model):
	menu = models.CharField(max_length=200)
	category = models.CharField(max_length=200)
	maker = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	city_detail = models.CharField(max_length=200,null=True)
	user = models.ForeignKey('auth.User')
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	dated_date = models.DateField()

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.menu+' '+ str(self.maker)+' '+ str(self.dated_date)