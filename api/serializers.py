from rest_framework import serializers
from api.models import User, UserProfile

# Writable Nested Serializer : a serializer that uses another serializer for a particular field('profile' in this case)
# By default nested serializers are read-only.
# If you want to support write-operations to a nested serializer field,
# you'll need to create create() and/or update() methods in order to explicitly specify how the child relationships should be saved.

# set_password() : the password is hashed and stored as a hash rather than a plain text

# write_only : meaning that it will be used for deserialization(creating the model), but not for serialization


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['title', 'date_of_birth',
                  'address', 'country', 'city', 'zip']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ['url', 'email', 'first_name',
                  'last_name', 'password', 'profile']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.title = profile_data.get('title', profile.title)
        profile.date_of_birth = profile_data.get(
            'date_of_birth', profile.date_of_birth)
        profile.address = profile_data.get('address', profile.address)
        profile.country = profile_data.get('country', profile.country)
        profile.city = profile_data.get('city', profile.city)
        profile.zip = profile_data.get('zip', profile.zip)
        profile.save()

        return instance
