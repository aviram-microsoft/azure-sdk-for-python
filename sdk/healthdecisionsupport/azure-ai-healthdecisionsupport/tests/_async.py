import asyncio
import json
import sys

sys.path.append("../azure/healthdecisionsupport")
sys.path.append("..")

from azure.ai.helathdecisionsupport import TrialMatcherClient
from azure.core.credentials import AzureKeyCredential

def trialmatcher_test() -> None:
    endpoint = "https://westeurope.api.cognitive.microsoft.com"
    key = "95c92b4a837a420c83d37ef2689d7f4a"

    trial_matcher_client = TrialMatcherClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key)
    )

    # Opening JSON file
    f = open('bodySample.json')

    # returns JSON object as a dictionary
    j = json.load(f)

    trial_matcher_client.create_job(j)


def main():
    trialmatcher_test()


if __name__ == '__main__':
    main()
