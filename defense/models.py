from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.contrib.postgres.fields import ArrayField

def personalID():
	t_id = 'PER-1'
	try:
		prev = CustomUser.objects.values('personal_id').last()
		prev = prev['personal_id']
		number = prev.split('-')[1]
		number=int(number)+1
		t_id = 'PER-'+str(number)
	except:
		t_id='PER-1'
	return t_id

ROLE = (
	('militarychief','militarychief'),
	('militarypersonal','militarypersonal'),
	('controlcenter','controlcenter')
)
BASE= (
	('None','None'),
	('Al Dafra Base','Al Dafra Base'),
	('Al Tanf Base','Al Tanf Base'),
)
COUNTRY = (
	('None','None'),
	('United Arab Emirates','United Arab Emirates'),
	('Syria' , 'Syria'),
)
MISSION = (
	('None','None'),
	('security','security'),
)
STATUS= (
	('Pending','Pending'),
	('Accepted','Accepted'),
	('Uploaded','Uploaded'),
	('Finalized','Finalized')
)

class Blockchain(models.Model):
    block_number = models.IntegerField()
    previous_hash = models.CharField(max_length=64)
    data = models.TextField()
    hash = models.CharField(max_length=64)

    def __str__(self):
        return f'Block {self.block_number}'


class CustomUser(AbstractUser):
	personal_id = models.CharField(max_length=20,default=personalID,blank=True)
	department = models.CharField(max_length=5,choices = (('None','None'),('army',"army")), default='None')
	base = models.CharField(max_length=40,choices = BASE, default='None')
	country = models.CharField(max_length=40,choices=COUNTRY,default='None')
	mission = models.CharField(max_length=30,choices=MISSION,default='None')
	role = models.CharField(max_length=20,choices = ROLE, default='militarychief')
	blockchain = models.ForeignKey(Blockchain, on_delete=models.CASCADE, null=True, blank=True)
	zero_proof = models.CharField(max_length=128, null=True, blank=True)

	def __str__(self):
		return self.username

class Request(models.Model):
	tusername = models.CharField(max_length=40,default='None')
	file_code = models.CharField(max_length=70,default="None")
	file1 = models.FileField(default=None)
	file2 = models.FileField(default=None)
	""" deadline = models.DateField(default=datetime.date.today) """
	status = models.CharField(max_length=10,default='Pending')
	enc_field = ArrayField(models.BinaryField(max_length=500,default=None),default=list)
	private_key = models.FileField(default=None)

	def __str__(self):
		return self.tusername

class FinalPapers(models.Model):
	file_code = models.CharField(max_length=70,default="None")
	department = models.CharField(max_length=70,default='None')
	base = models.CharField(max_length=70,default='None')
	country = models.CharField(max_length=40,default='None')
	mission = models.CharField(max_length=30,default='None')
	paper = models.FileField(default=None)

	def __str__(self):
		return self.file_code

class FileCode(models.Model):
	file_code = models.CharField(max_length=70)
	mission = models.CharField(max_length=30)

	def __str__(self):
		return self.mission
	

