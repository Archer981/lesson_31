from django.contrib.auth.models import User
from django.db import models
from rest_framework.exceptions import ValidationError


# TODO добавьте необходимый код в данный модуль
class Code(models.Model):
    code = models.CharField(max_length=4)


def code_verification_validator(value):
    if not Code.objects.filter(code=value):
        raise ValidationError(f'Значение {value} не существует в кодах')


class Vacation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    code = models.CharField(max_length=4, validators=[code_verification_validator])
