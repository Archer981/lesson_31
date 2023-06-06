import datetime

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from try_to_dismiss.models import Resource


def dismiss_date_verification(value: datetime.date):
    if value < datetime.date.today():
        raise ValidationError('Дата увольнения раньше сегодня')


# TODO добавьте необходимый код в сериалайзер ниже
class ResourceSerializer(serializers.ModelSerializer):
    is_active = serializers.ReadOnlyField()
    dismiss_date = serializers.DateField(validators=[dismiss_date_verification])

    class Meta:
        model = Resource
        fields = "__all__"
