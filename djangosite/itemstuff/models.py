from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
	user = models.ForeignKey(User)
	#user = models.TextField()
	title = models.TextField()
	details = models.TextField()
	price = models.FloatField()
	picture = models.FileField(upload_to="items/",null=True,blank=True)
	description = models.TextField()
	category = models.IntegerField()
	tags = models.TextField(blank=True, null=True)
	time = models.DateTimeField(auto_now=True)
	itemid = models.TextField()
	def __str__(self):
		return self.title
class Review(models.Model):
	user = models.ForeignKey(User)
	rating = models.IntegerField()
	text = models.TextField(blank = True, null = True)