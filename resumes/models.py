from django.db import models
from django.contrib.auth.models import User
from .storage import OverwriteStorage

def change_file_name(instance, filename):
    file_type = filename.split('.')[1]
    new_filname = instance.upload_user_majoring + '_' + \
        str(instance.upload_user_student_number) + '_' + \
        instance.upload_user_real_name + \
        '.' + file_type
    return '/'.join(['documents', new_filname])

class Resume(models.Model):
    upload_user = models.CharField(
        max_length=30,
        default='xxxx',
    )
    upload_user_real_name = models.CharField(
        max_length=30,
        default='홍길동',
    )
    upload_user_student_number = models.IntegerField(
        default=0,
    )
    upload_user_majoring = models.CharField(
        max_length=30,
        default='컴퓨터공학과',
    )
    document = models.FileField(
        storage=OverwriteStorage(),
        upload_to=change_file_name
        )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.upload_user)
