from rest_framework import serializers
from .models import User, Teacher
from django.db import transaction
class UsersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'last_name',
            'email',
            'password',
            'gender',
        ]
        read_only_fields = ['id']
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class TeacherSerializer(serializers.ModelSerializer):
    user = UsersSerializer()

    class Meta:
        model = Teacher
        fields = '__all__'

    def validate(self, data):
        user_data = data.get('user')

        if user_data:
            email = user_data.get('email')
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError({
                    "email": "El email ya está registrado"
                })

        nss = data.get('nss')
        if nss and Teacher.objects.filter(nss=nss).exists():
            raise serializers.ValidationError({
                "nss": "El NSS ya está registrado"
            })

        cellphone = data.get('cellphone')
        if cellphone and Teacher.objects.filter(cellphone=cellphone).exists():
            raise serializers.ValidationError({
                "cellphone": "El teléfono ya está registrado"
            })

        return data

    def create(self, validated_data):
        user_data = validated_data.pop('user')

        with transaction.atomic():
            # Crear usuario
            user = User.objects.create_user(**user_data)

            # Crear teacher
            teacher = Teacher.objects.create(user=user, **validated_data)

        return teacher