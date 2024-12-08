from django.conf import settings
from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=200, blank=False)
    image = models.ImageField(max_length=36)
    upload_date = models.DateTimeField()
    
    uplouded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='images',
        blank=False,
    )
    
    def __str__(self) -> str:
        return f"Image<{self.id}>"
 
   