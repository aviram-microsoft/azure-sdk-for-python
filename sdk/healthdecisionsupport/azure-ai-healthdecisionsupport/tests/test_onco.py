import functools

# sys.path.append("../azure/healthdecisionsupport")
# sys.path.append("..")

from azure.ai.helathdecisionsupport import OncoPhenotypeClient

from devtools_testutils import (
    AzureRecordedTestCase,
    PowerShellPreparer,
    recorded_by_proxy,
)

from azure.core.credentials import AzureKeyCredential

OncoEnvPreparer = functools.partial(
    PowerShellPreparer,
    "onco",
    endpoint="https://westeurope.api.cognitive.microsoft.com",
    key="95c92b4a837a420c83d37ef2689d7f4a",
)

class TestOnco(AzureRecordedTestCase):
    @OncoEnvPreparer()
    @recorded_by_proxy
    def test_onco(self, **kwargs):
        onco_endpoint = kwargs.pop("endpoint")
        onco_key = kwargs.pop("key")
        onco_client = OncoPhenotypeClient(onco_endpoint, AzureKeyCredential(onco_key))
        assert onco_client is not None
        #
        # f = open('bodySample.json')
        # j = json.load(f)
        #
        # response = trial_matcher_client.create_job(j)
        print("hi")