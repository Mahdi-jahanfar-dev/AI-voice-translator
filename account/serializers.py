from django.contrib.auth.models import User
from rest_framework import serializers


# register serializer
class UserRegisterSerializer(serializers.ModelSerializer):
    password_2 = serializers.CharField(max_length = 20, required = True, write_only = True, min_length = 8)
    password_1 = serializers.CharField(max_length = 20, required = True, write_only = True, min_length = 8)
    
    class Meta:
        model = User
        fields = ["username", "first_name", "password_1", "password_2"]
        
    def validate(self, attrs):
        if attrs["password_1"] != attrs["password_2"]:
            raise serializers.ValidationError("Passwords do not match.")
        return super().validate(attrs)
    
    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            first_name=validated_data["first_name"],
        )
        user.set_password(validated_data["password_1"])
        user.save()
        return user


# login serializer
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)