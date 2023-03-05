from datetime import date

from rest_framework import serializers


def check_not_published(value: bool):
    if value:
        raise serializers.ValidationError(f"This field may not be True")


def check_age(date_of_birth: date):
    today = date.today()
    age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    if age < 9:
        raise serializers.ValidationError(f"This field must be at least 9 years old")


def check_email(email):
    if "rambler.ru" in email:
        raise serializers.ValidationError(f"Регистрация с домена rambler.ru запрещена")
