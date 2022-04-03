import factory
from django.db.models import signals


@factory.django.mute_signals(signals.pre_save, signals.post_save)
def test_profile_str(db, profile_factory, check):
    profile = profile_factory()
    check.is_(profile.__str__(), f"{profile.user.username}")


def test_user_str(db, user_factory, check):
    user = user_factory.create()
    check.is_(user.__str__(), f"{user.username}")


@factory.django.mute_signals(signals.pre_save, signals.post_save)
def test_profile_follow(db, profile_factory, check):
    pass


@factory.django.mute_signals(signals.pre_save, signals.post_save)
def test_profile_unfollow(db, profile_factory, check):
    pass


@factory.django.mute_signals(signals.pre_save, signals.post_save)
def test_profile_is_followed_by(db, profile_factory, check):
    pass


@factory.django.mute_signals(signals.pre_save, signals.post_save)
def test_profile_favorite(db, profile_factory, check):
    pass


@factory.django.mute_signals(signals.pre_save, signals.post_save)
def test_profile_unfavorite(db, profile_factory, check):
    pass


@factory.django.mute_signals(signals.pre_save, signals.post_save)
def test_profile_has_favorited(db, profile_factory, check):
    pass
