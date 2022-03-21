import factory
from django.db.models import signals
from tests.test_profile.fixtures import user_controller, profile_controller


def test_get_user(db, user_controller, user_factory, check):
    user = user_factory()
    expected_user = user_controller.get_user(user.id)
    check.equal(user, expected_user)


@factory.django.mute_signals(signals.pre_save, signals.post_save)
def test_get_profile(db, profile_controller, profile_factory, check):
    profile = profile_factory()
    expected_profile = profile_controller.get_profile(profile.id)
    check.equal(profile, expected_profile)


def test_list_users(db, user_controller, user_factory, check):
    users = user_factory.create_batch(5)
    expected_users = user_controller.list_users_by_filters()
    check.equal(len(users), len(expected_users))


@factory.django.mute_signals(signals.pre_save, signals.post_save)
def test_list_profiles(db, profile_controller, profile_factory, check):
    profiles = profile_factory.create_batch(5)
    expected_profiles = profile_controller.list_profiles_by_filters()
    check.equal(len(profiles), len(expected_profiles))


def test_list_empty_user(db, user_controller, check):
    expected_user = user_controller.list_users_by_filters()
    check.equal(0, len(expected_user))


@factory.django.mute_signals(signals.pre_save, signals.post_save)
def test_list_empty_profile(db, profile_controller, check):
    expected_profile = profile_controller.list_profiles_by_filters()
    check.equal(0, len(expected_profile))


def test_create_user(db, user_controller, check, faker):
    data = dict(
        username=faker.name(),
        password=faker.password(),
    )
    user = user_controller.create_user(**data)
    expected_user = user_controller.get_user(user.id)
    check.equal(user, expected_user)


@factory.django.mute_signals(signals.pre_save, signals.post_save)
def test_create_profile(db, profile_controller, user_factory, check, faker):
    data = dict(
        user=user_factory(),
        bio=faker.text(),
        phone=faker.word(),
    )
    profile = profile_controller.create_profile(**data)
    expected_profile = profile_controller.get_profile(profile.id)
    check.equal(profile, expected_profile)
