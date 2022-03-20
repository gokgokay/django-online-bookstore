from django.contrib.auth.models import User


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


user_controller = UserController()
