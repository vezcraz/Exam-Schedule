from django.db import models

# Create your models here.
class database(models.Model):

	CAMPUS_ID=models.CharField(max_length=100)
	Name=models.CharField(max_length=100)
	Course_ID=models.CharField(max_length=100)
	


	def __str__(self):
		return self.Name

class reference(models.Model):

	cid=models.CharField(max_length=100)
	courseno=models.CharField(max_length=100)
	title=models.CharField(max_length=100)
	md=models.DateField(null=True)
	mt=models.CharField(max_length=100, null=True)
	cd=models.DateField(null=True)
	ct=models.CharField(max_length=100, null=True)


	def __str__(self):
		return self.cid

    