from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=50) 
    content = models.CharField(max_length=50)
    image = models.ImageField(upload_to='projects')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name = 'project'
        verbose_name_plural = 'projects'

    def __str__(self):
        return self.title