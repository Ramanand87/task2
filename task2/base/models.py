from django.db import models
from django.contrib.auth.models import User
import uuid
class Profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    user_type=models.CharField(max_length=100,blank=True)
    name=models.CharField(max_length=100,blank=True)
    # image=models.ImageField(upload_to='image')
    uid=models.UUIDField(default=uuid.uuid4)
    address=models.TextField(blank=True)
    # image=models.ImageField(upload_to ='img/')

    def __str__(self):
        return self.name
