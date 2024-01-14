from django.db import models
class Member(models.Model):
	User_name = models.CharField(max_length=32)
	email = models.EmailField(max_length=50)
	passwd = models.CharField(max_length=50)

	def __str__(self):
		return self.User_name




