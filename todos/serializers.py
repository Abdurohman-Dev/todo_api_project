from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User
from rest_framework import serializers
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id','user','title','completed','created_at']
        read_only_fields = ['user']

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Titleህ ቢያንስ 3 ፊደላት መሆን አለበት!")
        return value
    def validate(self, data):
        title = data.get('title','')
        completed = data.get('completed',False)

        if title.lower() == 'test' and completed:
            raise serializers.ValidationError("የ 'test' Title ያለው Todo ተጠናቋል (complated) ተብሎ ሊመዘገብ አይችልም! ")
        return data
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validate_data):
        user = User.objects.create_user(
            username=self.validated_data['username'],
            email=self.validated_data.get('email',''),
            password= self.validated_data['password']
        )
        return user


















