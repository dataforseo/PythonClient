# ContentGenerationCheckGrammarLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**input_tokens** | **StrictInt** | number of input tokens in the POST request |[optional]|
**output_tokens** | **StrictInt** | number of output tokens in the response |[optional]|
**new_tokens** | **StrictInt** | number of new tokens in the response |[optional]|
**initial_text** | **StrictStr** | initial text in the POST request |[optional]|
**language_code** | **StrictStr** | language code in the POST request |[optional]|
**items_count** | **StrictInt** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[ContentGenerationCheckGrammarLiveItem]]** | contains grammar or spelling errors and related data |[optional]|