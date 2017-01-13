from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile')
    real_name = models.CharField(
        max_length=10,
        default='홍길동',
    )
    phone_number = models.IntegerField(
        default=0,
    )
    student_number = models.IntegerField(
        default=0,
    )
    GRADE_CHOICES = (
        ('FR', '1학년'),
        ('SO', '2학년'),
        ('JR', '3학년'),
        ('SR', '4학년'),
    )
    REGISTER_CHOICES = (
        ('Y', '재학생'),
        ('N', '휴학생'),
    )
    grade = models.CharField(
        max_length=2,
        choices=GRADE_CHOICES,
        default='one',
    )
    register = models.CharField(
        max_length=2,
        choices=REGISTER_CHOICES,
        default='Y',
    )
    majoring = models.CharField(
        max_length=20,
        default='컴퓨터공학과',
    )
    def __str__(self):
          return "%s" % self.user

def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)
