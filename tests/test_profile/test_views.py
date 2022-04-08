import json
import factory
from django.db.models import signals


class TestListProfileView:
    endpoint = '/api/profiles/'

    @factory.django.mute_signals(signals.pre_save, signals.post_save)
    def test_list(self, db, api_client, profile_factory, check):
        profile_factory.create_batch(5)
        response = api_client().get(self.endpoint)
        check.is_(200, response.status_code)
        check.is_(5, len(json.loads(response.content)['profiles']))
