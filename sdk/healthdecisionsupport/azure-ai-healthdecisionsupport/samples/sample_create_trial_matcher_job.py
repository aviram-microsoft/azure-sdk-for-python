# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
import datetime
import asyncio
import json

from azure.core.credentials import AzureKeyCredential
from azure.ai.helathdecisionsupport.models import *
from azure.ai.helathdecisionsupport.aio import TrialMatcherClient


class HealthDecisionSupportSamples:
    async def create_trial_matcher_job(self):
        KEY = os.getenv("HEALTH_DECISION_SUPPORT_KEY")
        ENDPOINT = os.getenv("HEALTH_DECISION_SUPPORT_ENDPOINT")

        # Create an Trial Matcher client
        # <client>
        trial_matcher_client = TrialMatcherClient(endpoint=ENDPOINT,
                                                  credential=AzureKeyCredential(KEY))
        # </client>

        # Create clinical info list
        # <clinicalInfo>
        clinical_info_list = [ClinicalCodedElement(system="http://www.nlm.nih.gov/research/umls",
                                                   code="C0006826",
                                                   name="Malignant Neoplasms",
                                                   value="true"),
                              ClinicalCodedElement(system="http://www.nlm.nih.gov/research/umls",
                                                   code="C1522449",
                                                   name="Therapeutic radiology procedure",
                                                   value="true"),
                              ClinicalCodedElement(system="http://www.nlm.nih.gov/research/umls",
                                                   code="METASTATIC",
                                                   name="metastatic",
                                                   value="true"),
                              ClinicalCodedElement(system="http://www.nlm.nih.gov/research/umls",
                                                   code="C1512162",
                                                   name="Eastern Cooperative Oncology Group",
                                                   value="1"),
                              ClinicalCodedElement(system="http://www.nlm.nih.gov/research/umls",
                                                   code="C0019693",
                                                   name="HIV Infections",
                                                   value="false"),
                              ClinicalCodedElement(system="http://www.nlm.nih.gov/research/umls",
                                                   code="C1300072",
                                                   name="Tumor stage",
                                                   value="2"),
                              ClinicalCodedElement(system="http://www.nlm.nih.gov/research/umls",
                                                   code="C0019163",
                                                   name="Hepatitis B",
                                                   value="false"),
                              ClinicalCodedElement(system="http://www.nlm.nih.gov/research/umls",
                                                   code="C0018802",
                                                   name="Congestive heart failure",
                                                   value="true"),
                              ClinicalCodedElement(system="http://www.nlm.nih.gov/research/umls",
                                                   code="C0019196",
                                                   name="Hepatitis C",
                                                   value="false"),
                              ClinicalCodedElement(system="http://www.nlm.nih.gov/research/umls",
                                                   code="C0220650",
                                                   name="Metastatic malignant neoplasm to brain",
                                                   value="true")]

        # </clinicalInfo>

        # Construct Patient
        # <PatientConstructor>
        patient_info = PatientInfo(gender=PatientInfoGender.MALE, birth_date=datetime.date(1965, 12, 26),
                                   clinical_info=clinical_info_list)
        patient1 = Patient(id="patient_id", info=patient_info)
        # </PatientConstructor>

        # Create registry filter
        registry_filters = ClinicalTrialRegistryFilter()
        # Limit the trial to a specific patient condition ("Non-small cell lung cancer")
        registry_filters.conditions = ["Non-small cell lung cancer"]
        # Limit the clinical trial to a certain phase, phase 1
        registry_filters.phases = [ClinicalTrialPhase.PHASE1]
        # Specify the clinical trial registry source as ClinicalTrials.Gov
        registry_filters.sources = [ClinicalTrialSource.CLINICALTRIALS_GOV]
        # Limit the clinical trial to a certain location, in this case California, USA
        registry_filters.facility_locations = [Location(country="United States", city="Gilbert", state="Arizona")]
        # Limit the trial to a specific study type, interventional
        registry_filters.study_types = [ClinicalTrialStudyType.INTERVENTIONAL]

        # Construct ClinicalTrial instance and attach the registry filter to it.
        clinical_trials = ClinicalTrials(registry_filters=[registry_filters])

        # Create TrialMatcherRequest
        configuration = TrialMatcherModelConfiguration(clinical_trials=clinical_trials)
        trial_matcher_request = TrialMatcherRequest(patients=[patient1], configuration=configuration)

        # view operation results
        def callback(response):
            if response.http_request.method == "GET":
                trial_matcher_response = load_json(response.http_response.content)
                if trial_matcher_response.status == JobStatus.SUCCEEDED:
                    tm_results = trial_matcher_response.results
                    for patient_result in tm_results.patients:
                        print(f"Inferences of Patient {patient_result.id}")
                        for tm_inferences in patient_result.inferences:
                            print(f"Trial Id {tm_inferences.id}")
                            print(f"Type: {str(tm_inferences.type)}  Value: {tm_inferences.value}")
                            print(f"Description {tm_inferences.description}")
                else:
                    tm_errors = trial_matcher_response.errors
                    if tm_errors is not None:
                        for error in tm_errors:
                            print(f"{error.code} : {error.message}")

        # Health Decision Support Trial Matcher create job async
        try:
            poller = await trial_matcher_client.begin_create_job(trial_matcher_request, raw_response_hook=callback)
            await poller.wait()
        except Exception as ex:
            print(str(ex))
            return


def load_json(content) -> TrialMatcherResponse:
    my_json = content.decode('utf8').replace("'", '"')
    return TrialMatcherResponse(json.loads(my_json))


async def main():
    sample = HealthDecisionSupportSamples()
    await sample.create_trial_matcher_job()


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
