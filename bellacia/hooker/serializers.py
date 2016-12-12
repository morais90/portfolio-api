# -*- coding:utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework import serializers

from .models import Hooker, Service, Contact


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name')


class HookerSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Hooker
        fields = ('id', 'name', 'age', 'weight', 'height', 'services')
        read_only_fields = ('id', 'services')


class ContactSerializer(serializers.ModelSerializer):
    def validate(self, data):
        contact = data.get('contact')
        kind = data.get('kind')

        if kind == Contact.EMAIL:
            try:
                validate_email(contact)
            except ValidationError:
                raise serializers.ValidationError({'contact': 'invalid_value'})
        elif kind in (Contact.WHATSAPP, Contact.PHONE):
            if len(contact) > 11:
                raise serializers.ValidationError(
                    {'contact': _('Ensure this field has no more than {max_length} characters.')}
                )
            elif not contact.isdigit():
                raise serializers.ValidationError(
                    {'contact': _('Not a valid number')}
                )

    class Meta:
        model = Contact
        fields = ('id', 'kind', 'contact', 'hooker')
        extra_kwargs = {
            'hooker': {
                'write_only'
            }
        }
