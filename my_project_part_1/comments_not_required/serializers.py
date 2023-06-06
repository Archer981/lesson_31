from rest_framework import serializers
from comments_not_required.models import Calendar


# TODO добавьте необходимый код в сериалайзер ниже
class CalendarEventsSerializer(serializers.ModelSerializer):
    comment = serializers.CharField(read_only=True, allow_null=True, allow_blank=True)

    class Meta:
        model = Calendar
        fields = "__all__"
