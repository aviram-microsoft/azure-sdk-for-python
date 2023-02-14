import functools
import json

from azure.core.credentials import AzureKeyCredential
from azure.ai.healthdecisionsupport import TrialMatcherClient
from azure.ai.healthdecisionsupport.models import *

from devtools_testutils import (
    AzureRecordedTestCase,
    PowerShellPreparer,
    recorded_by_proxy,
)

HealthDecisionSupportEnvPreparer = functools.partial(
    PowerShellPreparer,
    "healthdecisionsupport",
    healthdecisionsupport_endpoint="https://fake_ad_resource.cognitiveservices.azure.com/",
    healthdecisionsupport_key="00000000000000000000000000000000",
)


class TestTrialMatcher(AzureRecordedTestCase):

    @staticmethod
    def load_json(path) -> json:
        with open(path, 'rt', encoding='utf8') as json_file:
            res = json.load(json_file)
            return res

    @HealthDecisionSupportEnvPreparer()
    @recorded_by_proxy
    def test_valid_request(self, healthdecisionsupport_endpoint, healthdecisionsupport_key):
        trial_matcher_client = TrialMatcherClient(healthdecisionsupport_endpoint,
                                                  AzureKeyCredential(healthdecisionsupport_key))

        assert trial_matcher_client is not None

        data = self.load_json('data/trial_matcher_data.json')

        poller = trial_matcher_client.begin_match_trials(data)
        response = poller.result()

        assert len(response.results.patients[0].inferences) == 37
