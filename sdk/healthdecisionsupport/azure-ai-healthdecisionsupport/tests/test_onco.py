import functools
import json
import os

from azure.core.credentials import AzureKeyCredential
from azure.ai.helathdecisionsupport import OncoPhenotypeClient

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


class TestOnco(AzureRecordedTestCase):

    def load_json(self, path) -> json:
        with open(path, 'rt', encoding='utf8') as json_file:
            res = json.load(json_file)
            return res


    @HealthDecisionSupportEnvPreparer()
    @recorded_by_proxy
    def test_onco(self, healthdecisionsupport_endpoint, healthdecisionsupport_key):
        onco_client = OncoPhenotypeClient(healthdecisionsupport_endpoint, AzureKeyCredential(healthdecisionsupport_key))

        assert onco_client is not None

        data = self.load_json('onco_test_data.json')

        def my_callback(response):
            print(response.http_response.content)

        poller = onco_client.begin_create_job(data, raw_response_hook=my_callback)
        poller.wait()

