from rest_framework import serializers

from ads.models import Location, Category, Ad, User

# ===========================================================================
                            # ADS #
# ===========================================================================
class AdSerializer(serializers.ModelSerializer):
    author_id = serializers.CharField()
    category_id = serializers.CharField()

    class Meta:
        model = Ad
        fields = '__all__'


# ===========================================================================
                            # CATEGORY #
# ===========================================================================

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


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


# ===========================================================================
                           # LOCATIONS #
# ===========================================================================
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
