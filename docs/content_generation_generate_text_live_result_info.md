# ContentGenerationGenerateTextLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**input_tokens** | **StrictInt** | number of input tokens |[optional]|
**output_tokens** | **StrictInt** | number of output tokens |[optional]|
**new_tokens** | **StrictInt** | number of new tokens |[optional]|
**generated_text** | **StrictStr** | resulting text |[optional]|
**supplement_token** | **StrictStr** | token for generating subsequent results<br>you can use this parameter to continue the generation from the end of the current result;<br>supplement_token values are unique for each subsequent task |[optional]|