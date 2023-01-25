---
page_type: sample
languages:
  - python
products:
  - azure
  - azure-cognitive-services
  - azure-health-decision-support
urlFragment: health-decision-support-samples
---

# Samples for Health Decision Support client library for Python

These code samples show common scenario operations with the Health Decision Support client library.

These sample programs show common scenarios for the Anomaly Detector client's offerings.

|**File Name**|**Description**|
|----------------|-------------|
|[sample_create_onco_phenotype_job.py][sample_create_onco_phenotype_job] |Create onco phenotype job.|
|[sample_create_trial_matcher_job.py][sample_create_trial_matcher_job] |Create trial matcher job.|


## Prerequisites
* Python 2.7 or 3.5 or higher is required to use this package.
* The Pandas data analysis library.
* You must have an [Azure subscription][azure_subscription] and an
[Azure Anomaly Detector account][azure_anomaly_detector_account] to run these samples.

## Setup

1. Install the Azure Anomaly Detector client library for Python with [pip][pip]:

```bash
pip install azure-ai-healthdecisionsupport
```

2. Clone or download this sample repository
3. Open the sample folder in Visual Studio Code or your IDE of choice.

## Running the samples

1. Open a terminal window and `cd` to the directory that the samples are saved in.
2. Set the environment variables specified in the sample file you wish to run.
3. Follow the usage described in the file, e.g. `python sample_create_onco_phenotype_job.py`

## Next steps

Check out the [API reference documentation][python-fr-ref-docs] to learn more about
what you can do with the Azure Anomaly Detector client library.

[pip]: https://pypi.org/project/pip/
[azure_subscription]: https://azure.microsoft.com/free/cognitive-services
[azure_anomaly_detector_account]: https://ms.portal.azure.com/#create/Microsoft.CognitiveServicesAnomalyDetector
[python-fr-ref-docs]: https://azuresdkdocs.blob.core.windows.net/$web/python/azure-cognitiveservices-anomalydetector/0.3.0/index.html

[sample_create_onco_phenotype_job]: https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/healthdecisionsupport/azure-ai-healthdecisionsupport/samples/sample_create_onco_phenotype_job.py
[sample_create_trial_matcher_job]: https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/healthdecisionsupport/azure-ai-healthdecisionsupport/samples/sample_create_trial_matcher_job.py

C:\Users\reutgross\source\repos\github\azure-sdk-for-python\sdk\