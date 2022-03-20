from tests.test_profile.fixtures import user_controller


def test_get_user(db, user_controller, user_factory, check):
    user = user_factory()
    expected_user = user_controller.get_user(user.id)
    check.equal(user, expected_user)


def test_list_user(db, user_controller, user_factory, check):
    users = user_factory.create_batch(5)
    expected_users = user_controller.list_users_by_filters()
    check.equal(len(users), len(expected_users))


def test_list_empty_user(db, user_controller, check):
    expected_user = user_controller.list_users_by_filters()
    check.equal(0, len(expected_user))


def test_create_user(db, user_controller, check, faker):
    data = dict(
        username=faker.name(),
        password=faker.password(),
    )
    user = user_controller.create_user(**data)
    expected_user = user_controller.get_user(user.id)
    check.equal(user, expected_user)
