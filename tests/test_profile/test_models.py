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
    follower = profile_factory()
    followee = profile_factory()
    follower.follow(followee)
    check.is_(1, follower.follows.count())

    followee2 = profile_factory()
    follower.follow(followee2)
    check.is_(2, follower.follows.count())


@factory.django.mute_signals(signals.pre_save, signals.post_save)
def test_profile_unfollow(db, profile_factory, check):
    follower = profile_factory()
    followee = profile_factory()
    followee2 = profile_factory()
    follower.follow(followee)
    follower.follow(followee2)

    follower.unfollow(followee)
    check.is_(1, follower.follows.count())

    follower.unfollow(followee2)
    check.is_(0, follower.follows.count())


@factory.django.mute_signals(signals.pre_save, signals.post_save)
def test_profile_is_followed_by(db, profile_factory, check):
    follower = profile_factory()
    followee = profile_factory()

    follower.follow(followee)
    check.is_(True, followee.is_followed_by(follower))

    follower.unfollow(followee)
    check.is_(False, followee.is_followed_by(follower))


@factory.django.mute_signals(signals.pre_save, signals.post_save)
def test_profile_favorite(db, profile_factory, book_factory, check):
    profile = profile_factory()
    book = book_factory()

    check.is_(0, profile.favorite_books.count())

    profile.favorite(book)
    check.is_(1, profile.favorite_books.count())

    book2 = book_factory()
    profile.favorite(book2)
    check.is_(2, profile.favorite_books.count())


@factory.django.mute_signals(signals.pre_save, signals.post_save)
def test_profile_unfavorite(db, profile_factory, book_factory, check):
    profile = profile_factory()
    book = book_factory()
    book2 = book_factory()
    profile.favorite(book)
    profile.favorite(book2)

    check.is_(2, profile.favorite_books.count())

    profile.unfavorite(book)
    check.is_(1, profile.favorite_books.count())

    profile.unfavorite(book2)
    check.is_(0, profile.favorite_books.count())


@factory.django.mute_signals(signals.pre_save, signals.post_save)
def test_profile_has_favorited(db, profile_factory, book_factory, check):
    profile = profile_factory()
    book = book_factory()

    profile.favorite(book)
    check.is_(True, profile.has_favorited(book))

    profile.unfavorite(book)
    check.is_(False, profile.has_favorited(book))
