from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    CHOICE_GENDER=(
        ('m','남성'),
        ('f','여성'),
        ('x','선텍안함'),
    )

    img_profile = models.ImageField(upload_to='user',  blank= True)
    site = models.URLField(blank=True)
    introduce = models.TextField(blank= True)
    gender = models.CharField(max_length=1, choices=CHOICE_GENDER)

    def __str__(self):
        return self.username

