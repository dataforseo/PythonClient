# ResultAvailableLanguages


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**available_platforms** | **List[Optional[StrictStr]]** | supported LLM platforms<br>contains the sources of data supported for a specific location and language combination<br>only google and chat_gpt are currently available |[optional]|
**language_name** | **StrictStr** | language name |[optional]|
**language_code** | **StrictStr** | language code according to ISO 639-1 |[optional]|
**responses_count** | **StrictInt** | number of LLM responses<br>the number of LLM responses available in the database for the certain location and language parameters |[optional]|