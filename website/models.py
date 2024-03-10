from django.db import models


class Person(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	PersonID = models.CharField(max_length=50)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	TFN =  models.CharField(max_length=50)
	DOB = models.DateField(max_length=15)
	address =  models.CharField(max_length=100)
	SelectEmpyeeToCheckSS =  models.CharField(max_length=50)
	declarationAcceptance =  models.CharField(max_length=50)
	

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")