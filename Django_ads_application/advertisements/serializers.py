from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""
    creator = UserSerializer(read_only=True,    )
    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )    


    def create(self, validated_data):
        """Метод для создания"""
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)
        

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        user = self.context["request"].user.id
        count_ad = Advertisement.objects.filter(creator_id = user, status = 'OPEN').count()   
        if count_ad > 9 and self.context["request"].method == "POST" and data.get("status") != "CLOSED":
            raise ValidationError(' Превышен лимит открытых объявлений')
        return data





#    def create:
        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
