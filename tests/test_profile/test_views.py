import json
import factory
from django.db.models import signals


class TestListProfileView:

    @factory.django.mute_signals(signals.pre_save, signals.post_save)
    def test_list(self, db, api_client, profile_factory, check):
        endpoint = '/api/profiles/'
        profile_factory.create_batch(5)
        response = api_client.get(endpoint)
        check.is_(200, response.status_code)
        check.is_(5, len(json.loads(response.content)['profiles']))


class TestProfileFollowAPIView:

    @factory.django.mute_signals(signals.pre_save, signals.post_save)
    def test_post(self, db, api_client, profile_factory, check):
        follower = profile_factory()
        followee = profile_factory()
        endpoint = f'/api/profiles/{followee.user.username}/follow/'

        data = {
            'username': followee.user.username,
        }

        api_client.force_authenticate(follower.user)
        response = api_client.post(endpoint, data=data, format='json')

        expected_data = {
            'status': response.status_code,
            'followee':
                {
                    'username': followee.user.username
                }
        }

        check.equal(200, response.status_code)
        check.equal(expected_data, json.loads(response.content))

    @factory.django.mute_signals(signals.pre_save, signals.post_save)
    def test_delete(self, db, api_client, profile_factory, check):
        follower = profile_factory()
        followee = profile_factory()
        endpoint = f'/api/profiles/{followee.user.username}/follow/'

        data = {
            'username': followee.user.username,
        }

        api_client.force_authenticate(follower.user)
        api_client.post(endpoint, data=data, format='json')
        response = api_client.delete(endpoint, data=data, format='json')

        expected_data = {
            'status': response.status_code,
            'followee':
                {
                    'username': followee.user.username
                }
        }

        check.equal(200, response.status_code)
        check.equal(expected_data, json.loads(response.content))
