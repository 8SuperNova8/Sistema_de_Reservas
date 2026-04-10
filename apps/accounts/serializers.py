from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import User

class UserAdminSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id','password', 'first_name', 'last_name', 'is_active', 'date_joined', 'email']
        read_only_fields = ('date_joined',)

    def create(self, validated_data):
        password =  validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        
        receptionist_group= Group.objects.get(name='Receptionist')
        user.groups.add(receptionist_group)
        return user
    
class UserListSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id','password', 'first_name', 'last_name', 'is_active', 'date_joined', 'email', 'role']
    
    def get_role(self, user):
        if user.is_superuser:
            return 'SUPERUSER'
        if user.groups.filter(name='Receptionist').exists():
            return 'RECEPTIONIST'
        return 'NO_ROLE'
    
#para actualizar contraseña
class UpdatePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=True)

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance