import json
import sys
import pytest
import functools

sys.path.append("../azure/healthdecisionsupport")
sys.path.append("..")

from azure.ai.helathdecisionsupport import TrialMatcherClient

from devtools_testutils import (
    AzureRecordedTestCase,
    PowerShellPreparer,
    recorded_by_proxy,
)

from azure.core.credentials import AzureKeyCredential

TrialMatcherDetectorEnvPreparer = functools.partial(
    PowerShellPreparer,
    "trial_matcher",
    trial_matcher_endpoint="https://westeurope.api.cognitive.microsoft.com/",
    trial_matcher_key="95c92b4a837a420c83d37ef2689d7f4a",
)

class TestTrialMatcher(AzureRecordedTestCase):
    @TrialMatcherDetectorEnvPreparer()
    @recorded_by_proxy
    def test_trialmatcher_connection(self, **kwargs):
        trial_matcher_endpoint = kwargs.pop("trial_matcher_endpoint")
        trial_matcher_key = kwargs.pop("trial_matcher_key")
        trial_matcher_client = TrialMatcherClient(trial_matcher_endpoint, AzureKeyCredential(trial_matcher_key))
        assert trial_matcher_client is not None
        #
        # f = open('bodySample.json')
        # j = json.load(f)
        #
        # response = trial_matcher_client.create_job(j)
        print("hi")
