import asyncio
import sys
import json

from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.ai.healthdecisionsupport import OncoPhenotypeClient
from azure.core.credentials import AzureKeyCredential
from process_job import ProcessJob


def onco_test() -> LROPoller:


    onco_client = OncoPhenotypeClient(endpoint=endpoint,
                                      credential=AzureKeyCredential(key))

    payload = load_json('onco_test_data.json')

    poller = onco_client.begin_create_job(payload, raw_response_hook=my_callback)
    response = poller.result()

    return response


def load_json(path) -> json:
    with open(path, 'rt', encoding='utf8') as json_file:
        res = json.load(json_file)
        return res


def my_callback(resp):
    print(resp.http_response.content)


def main():
    result = onco_test()
    print(result)


if __name__ == '__main__':
    main()
