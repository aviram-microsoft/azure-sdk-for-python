# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
import datetime
import asyncio

from azure.core.credentials import AzureKeyCredential
from azure.ai.healthdecisionsupport.models import *
from azure.ai.healthdecisionsupport.aio import TrialMatcherClient

"""
FILE: sample_match_trials.py

DESCRIPTION:
    Finding potential eligible trials for a patient, based on patient’s structured medical information.

    Trial Matcher model matches a single patient to a set of relevant clinical trials,
    that this patient appears to be qualified for. This use case will demonstrate:
    a. How to use the trial matcher when patient clinical health information is provided to the
    Trial Matcher in a key-value structure with coded elements.
    b. How to use the clinical trial configuration to narrow down the trial condition,
    recruitment status, location and other criteria that the service users may choose to prioritize.

USAGE:
    python sample_match_trials.py

    Set the environment variables with your own values before running the sample:
    1) HEALTH_DECISION_SUPPORT_KEY - your source from Health Decision Support API key.
    2) HEALTH_DECISION_SUPPORT_ENDPOINT - the endpoint to your source Health Decision Support resource.
"""


class HealthDecisionSupportSamples:
    async def match_trials(self):
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

        # Health Decision Support Trial match trials
        try:
            poller = await trial_matcher_client.begin_match_trials(trial_matcher_request)
            trial_matcher_response = await poller.result()
            self.print_results(trial_matcher_response)
        except Exception as ex:
            print(str(ex))
            return

    # print match trials (eligible/ineligible)
    def print_results(self, trial_matcher_response):
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


async def main():
    sample = HealthDecisionSupportSamples()
    await sample.match_trials()


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
