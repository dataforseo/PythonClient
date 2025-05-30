# ContentGenerationCheckGrammarLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**input_tokens** | **StrictFloat** | number of input tokens in the POST request |[optional]|
**output_tokens** | **StrictFloat** | number of output tokens in the response |[optional]|
**new_tokens** | **StrictFloat** | number of new tokens in the response |[optional]|
**initial_text** | **StrictStr** | initial text in the POST request |[optional]|
**language_code** | **StrictStr** | language code in the POST request |[optional]|
**items_count** | **StrictFloat** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[ContentGenerationCheckGrammarLiveItem]]** | contains grammar or spelling errors and related data |[optional]|