import functools
import json

from azure.ai.helathdecisionsupport.models import *
from azure.core.credentials import AzureKeyCredential
from azure.ai.helathdecisionsupport import TrialMatcherClient

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

    def load_json(self, path) -> json:
        with open(path, 'rt', encoding='utf8') as json_file:
            res = json.load(json_file)
            return res

    def response_json(self, content) -> TrialMatcherResponse:
        my_json = content.decode('utf8').replace("'", '"')
        return TrialMatcherResponse(json.loads(my_json))

    @HealthDecisionSupportEnvPreparer()
    @recorded_by_proxy
    def test_valid_request(self, healthdecisionsupport_endpoint, healthdecisionsupport_key):
        trial_matcher_client = TrialMatcherClient(healthdecisionsupport_endpoint,
                                                  AzureKeyCredential(healthdecisionsupport_key))

        assert trial_matcher_client is not None

        data = self.load_json('trial_matcher_valid_request.json')

        def my_callback(response):
            print(response.http_response.content)
            if response.http_request.method == "GET":
                json_response = self.response_json(response.http_response.content)
                if json_response.status == JobStatus.SUCCEEDED:
                    print(json_response.results)

        poller = trial_matcher_client.begin_create_job(data, raw_response_hook=my_callback)
        poller.wait()

    @HealthDecisionSupportEnvPreparer()
    @recorded_by_proxy
    def test_empty_request(self, healthdecisionsupport_endpoint, healthdecisionsupport_key):
        trial_matcher_client = TrialMatcherClient(healthdecisionsupport_endpoint,
                                                  AzureKeyCredential(healthdecisionsupport_key))

        assert trial_matcher_client is not None

        data = self.load_json('trial_matcher_empty_request.json')

        def my_callback(response):
            print(response.http_response.content)
            if response.http_request.method == "GET":
                json_response = self.response_json(response.http_response.content)
                if json_response.status == JobStatus.SUCCEEDED:
                    assert json_response.results.patients[0].inferences == []
                    print(json_response.results)

        poller = trial_matcher_client.begin_create_job(data, raw_response_hook=my_callback)
        poller.wait()
