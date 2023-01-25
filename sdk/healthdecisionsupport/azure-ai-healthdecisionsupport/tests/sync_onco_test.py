import asyncio
import sys
import json

from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.ai.helathdecisionsupport import OncoPhenotypeClient
from azure.core.credentials import AzureKeyCredential
from process_job import ProcessJob


def onco_test() -> LROPoller:
    endpoint = "https://westeurope.api.cognitive.microsoft.com"
    key = "95c92b4a837a420c83d37ef2689d7f4a"

    onco_client = OncoPhenotypeClient(endpoint=endpoint,
                                      credential=AzureKeyCredential(key))

    payload = load_json('onco_test_data.json')

    # client_job_processor = ProcessJob(onco_client)
    # response = client_job_processor.process_request(payload)
    # func = CallBack()
    poller = onco_client.begin_create_job(payload, raw_response_hook=my_callback)
    response = poller.result()

    return response


def load_json(path) -> json:
    with open(path, 'rt', encoding='utf8') as json_file:
        res = json.load(json_file)
        return res


# class CallBack:
#     stored_input = None
#     def my_callback(self, resp):
#         self.stored_input = resp.http_response.content
#         print(resp.http_response.content)

def my_callback(resp):
    print(resp.http_response.content)



# async def main():
#     result = await onco_test()
#     print(result)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())

def main():
    result = onco_test()
    print(result)


if __name__ == '__main__':
    main()
