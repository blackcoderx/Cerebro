from django.db import models
from django.contrib.auth.models import User


class School(models.Model):
  name = models.CharField(max_length = 200)

  def __str__(self) -> str:
    return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, null=False)
    school_name = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, blank=True)
    # school_name = models.CharField(max_length=255, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    course = models.CharField(max_length=255, blank=False, null=False)
    # level_of_education = models.CharField(max_length=255, blank=False, null=False)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=False, null=False)

    def __str__(self):
        return self.user.username


