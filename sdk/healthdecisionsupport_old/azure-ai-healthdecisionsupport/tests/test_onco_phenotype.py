import functools
import json

from azure.core.credentials import AzureKeyCredential
from azure.ai.healthdecisionsupport import OncoPhenotypeClient
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


class TestOncoPhenotype(AzureRecordedTestCase):

    @staticmethod
    def load_json(path) -> json:
        with open(path, 'rt', encoding='utf8') as json_file:
            res = json.load(json_file)
            return res

    @staticmethod
    def response_json(content) -> OncoPhenotypeResponse:
        my_json = content.decode('utf8').replace("'", '"')
        return OncoPhenotypeResponse(json.loads(my_json))

    @HealthDecisionSupportEnvPreparer()
    @recorded_by_proxy
    def test_onco_phenotype(self, healthdecisionsupport_endpoint, healthdecisionsupport_key):
        onco_client = OncoPhenotypeClient(healthdecisionsupport_endpoint, AzureKeyCredential(healthdecisionsupport_key))

        assert onco_client is not None

        data = self.load_json('data/onco_test_data.json')

        poller = onco_client.begin_infer_oncology_phenotyping(data)
        response = poller.result()
        if response.status == JobStatus.SUCCEEDED:
            assert response.results.patients[0].inferences == []
            print(response.results)


