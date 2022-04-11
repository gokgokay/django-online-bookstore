from django.contrib.auth.models import User

from profile.models import Profile


class UserController:

    def get_user(self, user_id):
        return User.objects.get(pk=user_id)

    def create_user(self, **data):
        user = User(**data)
        user.save()
        return user

    def list_users_by_filters(self, first_name=None):
        query = User.objects
        if first_name:
            query = query.filter(first_name=first_name)
        return query.all()


class ProfileController:

    def get_profile(self, profile_id):
        return Profile.objects.get(pk=profile_id)

    def create_profile(self, **data):
        profile = Profile(**data)
        profile.save()
        return profile

    def list_profiles_by_filters(self, phone=None):
        query = Profile.objects
        if phone:
            query = query.filter(phone=phone)
        return query.all()


user_controller = UserController()
profile_controller = ProfileController()
