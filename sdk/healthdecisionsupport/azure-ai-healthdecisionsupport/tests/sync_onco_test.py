import asyncio
import sys
import json

# sys.path.append("../azure/healthdecisionsupport")
# sys.path.append("..")

from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.ai.helathdecisionsupport import OncoPhenotypeClient
from azure.core.credentials import AzureKeyCredential


def onco_test() -> LROPoller:
    endpoint = "https://westeurope.api.cognitive.microsoft.com"
    key = "95c92b4a837a420c83d37ef2689d7f4a"

    onco_client = OncoPhenotypeClient(endpoint=endpoint,
                                      credential=AzureKeyCredential(key))

    body = open('onco_data.json')
    doc = json.load(body)

    poller = onco_client.begin_create_job(doc, raw_response_hook=my_callback)
    response = poller.result()

    return response


def my_callback(resp):
    print(resp.http_response.content)


def main():
    result = onco_test()


if __name__ == '__main__':
    main()
