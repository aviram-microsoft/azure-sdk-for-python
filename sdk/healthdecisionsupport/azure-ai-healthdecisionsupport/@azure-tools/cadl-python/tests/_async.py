import asyncio
import json
import sys
import json
import subprocess
from asyncio import sleep

sys.path.append("../azure/healthdecisionsupport")
sys.path.append("..")

from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.ai.helathdecisionsupport import OncoPhenotypeClient
from azure.core.credentials import AzureKeyCredential


def onco_test() -> LROPoller:
    endpoint = "https://westeurope.api.cognitive.microsoft.com"
    key = "95c92b4a837a420c83d37ef2689d7f4a"

    onco_client = OncoPhenotypeClient(endpoint=endpoint,
        credential=AzureKeyCredential(key))

    body = open('bodySample.json')
    j = json.load(body)

    body2 = open('onco_data.json')
    j2 = json.load(body2)

    poller = onco_client.begin_create_job(j2)
    poller.wait()
    response = poller.result()

    return response


def main():
    result = onco_test()
    print(result)

if __name__ == '__main__':
    main()
