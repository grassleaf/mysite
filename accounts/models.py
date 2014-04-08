from django.db import models
from django.contrib import admin

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length = 32, unique = True)
	passwd = models.CharField(max_length = 32)
	email = models.EmailField(unique = True)

	def __unicode__(self):
		return "%s [%s] %s" % (self.name, self.passwd, str(self.email))

	class Admin:
		pass
