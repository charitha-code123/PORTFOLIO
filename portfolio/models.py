from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return self.title
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True, null=True)  # Live demo (optional)
    github = models.URLField(blank=True, null=True)  # ✅ GitHub link

    def __str__(self):
        return self.title
    
# Create your models here.
