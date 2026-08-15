from rest_framework import serializers
from .models import Todo
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id','title','completed','created_at']

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



















