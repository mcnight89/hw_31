from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from ads.models import Location, Category, Ad, User, Selection


# ===========================================================================
# ADS #
# ===========================================================================
class AdSerializer(serializers.ModelSerializer):
    author_id = serializers.CharField()
    category_id = serializers.CharField()

    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Ad
        fields = ['id', 'name', 'author_id', 'category_id', 'price', 'description', 'is_published']


class AdUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'name', 'author_id', 'category_id', 'price', 'description', 'is_published']


class AdDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id']


# ===========================================================================
# CATEGORY #
# ===========================================================================

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Category
        fields = '__all__'


class CategoryDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id']


# ===========================================================================
# USERS #
# ===========================================================================

class UserSerializer(serializers.ModelSerializer):
    location = serializers.CharField()

    class Meta:
        model = User
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(user.password)
        user.save()

        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']


# ===========================================================================
# LOCATIONS #
# ===========================================================================
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


# ===========================================================================
# SELECTION #
# ===========================================================================
class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = '__all__'


class SelectionCreateSerializer(serializers.ModelSerializer):
    owner = SlugRelatedField(slug_field="username", read_only=True)

    def create(self, validated_data):
        requests = self.context.get("request")
        validated_data["owner"] = requests.user
        return super().create(validated_data)

    class Meta:
        model = Selection
        fields = ["name", "items"]
