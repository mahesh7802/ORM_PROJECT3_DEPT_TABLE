from django.db import models

# Create your models here.

class Dept(models.Model):
    dname=models.CharField(max_length=20,primary_key=True)
    did=models.IntegerField()
    dlocation=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.dname
    
class Emp(models.Model):
    dname=models.ForeignKey(Dept,on_delete=models.CASCADE)
    ename=models.CharField(max_length=20)
    enumber=models.IntegerField()
    elocation=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.ename
