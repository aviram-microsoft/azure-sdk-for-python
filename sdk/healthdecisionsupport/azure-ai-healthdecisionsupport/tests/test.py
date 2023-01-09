import asyncio
import json
import sys

sys.path.append("../azure/healthdecisionsupport")
sys.path.append("..")

from azure.ai.helathdecisionsupport.aio import TrialMatcherClient
from azure.core.credentials import AzureKeyCredential

async def sample_trialmatcher_async() -> None:
    endpoint = "http://westeurope.api.cognitive.microsoft.com"
    key = "95c92b4a837a420c83d37ef2689d7f4a"

    trial_matcher_client = TrialMatcherClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key)
    )

    # Opening JSON file
    f = open("C:\\Users\\reutgross\\Downloads\\bodySample.json")

    # returns JSON object as a dictionary
    j = json.load(f)

    response = trial_matcher_client.create_job(j)
    print(response)

async def main():
    await sample_trialmatcher_async()


if __name__ == '__main__':
    asyncio.run(main())
