import json

from azure.ai.helathdecisionsupport import OncoPhenotypeClient
from azure.ai.helathdecisionsupport import TrialMatcherClient
from azure.ai.helathdecisionsupport.models import *
from asyncio import sleep, run
from azure.core.pipeline import PipelineResponse

HealthDecisionSupportClient = OncoPhenotypeClient | TrialMatcherClient


class ProcessJob:
    def __init__(self, client: HealthDecisionSupportClient) -> None:
        self._client = client
        self.response = None

    def process_request(self, payload) -> PipelineResponse:
        return run(self.process_request_sync(payload))

    async def process_request_sync(self, payload) -> PipelineResponse:
        poller = self._client.begin_create_job(payload,
                                      raw_response_hook=self.response_hook)
        while self.response is None:
            await sleep(1)
        return self.response


    def response_hook(self, resp):
        if resp.http_request.method == "POST" and \
                resp.http_response.status_code != 202:
            self.response = resp.http_response
        if resp.http_request.method == "GET":
            my_json = resp.http_response.content.decode('utf8').replace("'", '"')
            j_req = json.loads(my_json)
            # onco_results = j_req.results
            # oncoPhenotypeResponse = OncoPhenotypeResponse(mapping=j_req)
            self.response = resp.http_response.content