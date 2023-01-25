# Cognitive Services Health Decision Support client library for Python

[Health Decision Support](https://learn.microsoft.com/azure/cognitive-services/Anomaly-Detector/overview) is an AI service ####

## Getting started

### Prerequisites

- Python 3.7 or later is required to use this package.###
- You need an [Azure subscription][azure_sub] to use this package.###
- An existing Cognitive Services Health Decision Support instance.

### Installating the package

```bash
python -m pip install azure-ai-healthdecisionsupport
```

#### Prequisites

- Python 3.7 or later is required to use this package.
- You need an [Azure subscription][azure_sub] to use this package.
- An existing None instance.

#### Get the endpoint

#### Create a HealthDecisionSupportClient with an API Key Credential

Once you have the value for the API key, you can pass it as a string into an instance of **AzureKeyCredential**. Use the key as the credential parameter
to authenticate the client:

```python
from azure.core.credentials import AzureKeyCredential
from azure.ai.helathdecisionsupport import OncoPhenotypeClient
from azure.ai.helathdecisionsupport import TrialMatcherClient

credential = AzureKeyCredential("<api_key>")
onco_phenotype_client = OncoPhenotypeClient(endpoint="https://<resource-name>.cognitiveservices.azure.com/", credential=credential)
trial_matcher_client = TrialMatcherClient(endpoint="https://<resource-name>.cognitiveservices.azure.com/", credential=credential)
```

## Key concepts
### Univariate Anomaly Detection
### Multivariate Anomaly Detection
### Thread safety

## Examples

The following section provides several code snippets covering some of the most common Health Decision Support service tasks, including:
- [Onco Phenotype - Create job](#Create onco phenotype job)
- [Trial Matcher - Create job](#Create trial matcher job)

### Batch detection

### General
### Logging
### Optional Configuration

## Next steps

These code samples show common scenario operations with the Azure Health Decision Support library. More samples can be found under the [samples](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/healthdecisionsupport/azure-ai-healthdecisionsupport/samples/) directory.

- Onco Phenotype - Create job: [sample_create_onco_phenotype_job.py](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/healthdecisionsupport/azure-ai-healthdecisionsupport/samples/sample_create_onco_phenotype_job.py)

- Trial Matcher - Create job: [sample_create_trial_matcher_job.py](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/healthdecisionsupport/azure-ai-healthdecisionsupport/samples/sample_create_trial_matcher_job.py)


### Additional documentation

For more extensive documentation on Azure Anomaly Detector, see the [](https://learn.microsoft.com/azure/cognitive-services/anomaly-detector/overview) on docs.microsoft.com.

## Contributing

This project welcomes contributions and suggestions. Most contributions require
you to agree to a Contributor License Agreement (CLA) declaring that you have
the right to, and actually do, grant us the rights to use your contribution.
For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether
you need to provide a CLA and decorate the PR appropriately (e.g., label,
comment). Simply follow the instructions provided by the bot. You will only
need to do this once across all repos using our CLA.

This project has adopted the
[Microsoft Open Source Code of Conduct][code_of_conduct]. For more information,
see the Code of Conduct FAQ or contact opencode@microsoft.com with any
additional questions or comments.

<!-- LINKS -->
[code_of_conduct]: https://opensource.microsoft.com/codeofconduct/
[authenticate_with_token]: https://docs.microsoft.com/azure/cognitive-services/authentication?tabs=powershell#authenticate-with-an-authentication-token
[azure_identity_credentials]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/identity/azure-identity#credentials
[azure_identity_pip]: https://pypi.org/project/azure-identity/
[default_azure_credential]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/identity/azure-identity#defaultazurecredential
[pip]: https://pypi.org/project/pip/
[azure_sub]: https://azure.microsoft.com/free/
|[sample_create_onco_phenotype_job.py][sample_create_onco_phenotype_job] |Create onco phenotype job.|
|[sample_create_trial_matcher_job.py][sample_create_trial_matcher_job] |Create trial matcher job.|