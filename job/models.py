from django.db import models

JOB_Type=(
    ('full time','full time'),
    ('part time','part time'),
    
)
# Create your models here.
class job(models.Model):
    title = models.CharField(max_length=50)
    #location
    job_type=models.CharField(max_length=50,choices=JOB_Type)
    descerption=models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experince=models.IntegerField(default=1)

    def __str__(self):
        return self.title
    