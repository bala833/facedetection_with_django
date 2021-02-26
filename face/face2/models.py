from django.db import models
 
# Create your models here.
 
 
class Videos(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')
     
    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
         
    def __str__(self):
        return self.title

# Create your models here.

class Face(models.Model):
	user_id = models.PositiveSmallIntegerField()
	name = models.CharField(max_length=225)

	class Meta:
		verbose_name = 'face'
		verbose_name_plural = 'faces'

	def __str__(self):
		return self.name