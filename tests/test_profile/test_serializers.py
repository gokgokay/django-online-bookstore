import factory
from django.db.models import signals
from profile.serializers import ProfileSerializer


@factory.django.mute_signals(signals.pre_save, signals.post_save)
def test_serializer_profile(db, profile_factory, check):
    profile = profile_factory()
    serializer_profile = {
        'username': profile.user.username,
        'bio': profile.bio,
        'phone': profile.phone,
    }
    expected_profile = ProfileSerializer(data=serializer_profile)
    check.equal(True, expected_profile.is_valid(raise_exception=True))
