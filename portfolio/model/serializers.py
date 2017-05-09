# -*- coding:utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework import serializers

from .models import Model, Character, Contact


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('id', 'name')


class ModelSerializer(serializers.ModelSerializer):
    Character = CharacterSerializer(many=True, read_only=True)

    class Meta:
        model = Model
        fields = ('id', 'name', 'age', 'weight', 'height', 'services', 'picture', 'is_active')
        read_only_fields = ('id', 'services', 'is_active')


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
        fields = ('id', 'kind', 'contact', 'model')
        extra_kwargs = {
            'model': {
                'write_only'
            }
        }
