# Custom serializers for djoser
from djoser.serializers import UserCreateSerializer as BaseUserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()
