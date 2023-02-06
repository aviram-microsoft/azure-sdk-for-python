# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
import datetime

from azure.core.credentials import AzureKeyCredential
from azure.ai.healthdecisionsupport.models import *
from azure.ai.healthdecisionsupport import TrialMatcherClient

"""
FILE: sample_match_trials_sync.py

DESCRIPTION:
    This example demonstrates Finding potential eligible trials for a patient,
    based on patient’s structured medical information.
    It uses **SYNC** function unlike other samples that uses async function.

    It looks for structured clinical trials that were taken from ClinicalTrials.gov
    Trial Matcher model matches a single patient to a set of relevant clinical trials,
    that this patient appears to be qualified for. This use case will demonstrate:
    a. How to use the trial matcher when patient clinical health information is provided to the
    Trial Matcher in a key-value structure with coded elements.
    b. How to use the clinical trial configuration to narrow down the trial condition,
    recruitment status, location and other criteria that the service users may choose to prioritize.


USAGE:
    python sample_match_trials_sync.py

    Set the environment variables with your own values before running the sample:
    1) HEALTH_DECISION_SUPPORT_KEY - your source from Health Decision Support API key.
    2) HEALTH_DECISION_SUPPORT_ENDPOINT - the endpoint to your source Health Decision Support resource.
"""


class HealthDecisionSupportSamples:
    def match_trials(self):
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
                                                   code="C0032181",
                                                   name="Platelet count",
                                                   value="250000"),
                              ClinicalCodedElement(system="http://www.nlm.nih.gov/research/umls",
                                                   code="C0002965",
                                                   name="Unstable Angina",
                                                   value="true"),
                              ClinicalCodedElement(system="http://www.nlm.nih.gov/research/umls",
                                                   code="C1522449",
                                                   name="Radiotherapy",
                                                   value="false"),
                              ClinicalCodedElement(system="http://www.nlm.nih.gov/research/umls",
                                                   code="C0242957",
                                                   name="GeneOrProtein-Expression",
                                                   value="Negative;EntityType:GENEORPROTEIN-EXPRESSION"),
                              ClinicalCodedElement(system="http://www.nlm.nih.gov/research/umls",
                                                   code="C1300072",
                                                   name="cancer stage",
                                                   value="2")]

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
        registry_filters.conditions = ["non small cell lung cancer (nsclc)"]
        # Specify the clinical trial registry source as ClinicalTrials.Gov
        registry_filters.sources = [ClinicalTrialSource.CLINICALTRIALS_GOV]
        # Limit the clinical trial to a certain location, in this case California, USA
        registry_filters.facility_locations = [Location(country="United States", city="Gilbert", state="Arizona")]
        # Limit the trial to a specific recruitment status
        registry_filters.recruitment_statuses = [ClinicalTrialRecruitmentStatus.RECRUITING]

        # Construct ClinicalTrial instance and attach the registry filter to it.
        clinical_trials = ClinicalTrials(registry_filters=[registry_filters])

        # Create TrialMatcherRequest
        configuration = TrialMatcherModelConfiguration(clinical_trials=clinical_trials)
        trial_matcher_request = TrialMatcherRequest(patients=[patient1], configuration=configuration)

        # Health Decision Support Trial match trials
        try:
            poller = trial_matcher_client.begin_match_trials(trial_matcher_request)
            trial_matcher_response = poller.result()
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


if __name__ == "__main__":
    sample = HealthDecisionSupportSamples()
    sample.match_trials()

