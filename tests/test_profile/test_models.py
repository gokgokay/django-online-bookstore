def test_profile_str(db, profile_factory, check):
    profile = profile_factory()
    check.is_(profile.__str__(), f"{profile.username}")
