from rest_framework import serializers
from .models import Provider, Category

class ProviderSerializer(serializers.ModelSerializer):
    # Use PKs for writes
    categories = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Category.objects.all()
    )
    # Show names in GET
    category_names = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Provider
        fields = ['id', 'username', 'email', 'phone', 'categories', 'category_names', 'password', 'active']
        extra_kwargs = {'password': {'write_only': True}}

    def get_category_names(self, obj):
        return [cat.name for cat in obj.categories.all()]

    def create(self, validated_data):
        categories_data = validated_data.pop('categories', [])
        password = validated_data.pop('password', None)
        provider = Provider(**validated_data)
        if password:
            provider.set_password(password)
        provider.save()
        provider.categories.set(categories_data)
        return provider

    def update(self, instance, validated_data):
        categories_data = validated_data.pop('categories', None)
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        if categories_data is not None:
            instance.categories.set(categories_data)
        return instance

# -----------------------
# Serializer for EDIT/UPDATE only
# -----------------------
class ProviderUpdateSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Category.objects.all()
    )
    category_names = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Provider
        fields = ['id', 'username', 'email', 'phone', 'categories', 'category_names', 'active']
        read_only_fields = ['id']

    def get_category_names(self, obj):
        return [cat.name for cat in obj.categories.all()]

    def update(self, instance, validated_data):
        categories_data = validated_data.pop('categories', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if categories_data is not None:
            instance.categories.set(categories_data)
        return instance
