from rest_framework import serializers
from .models import User

class UserAdminSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id','password', 'is_superuser', 'first_name', 'last_name', 'is_active', 'date_joined', 'email']
        read_only_fields = ('date_joined',)

    def create(self, validated_data):
        password =  validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user