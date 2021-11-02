from django.db import models
from django.contrib.auth.models import User



class ProfileModel(models.Model):

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربر'


    user = models.OneToOneField(User, verbose_name= 'کاربری', on_delete=models.CASCADE, related_name='profile')

    status_choices = (

        ("man", "مرد"),
        ("woman", "زن"),
    )

    gender = models.CharField(max_length=50 ,choices=status_choices, verbose_name = 'جنسیت')


    def __str__(self):
        return self.gender



