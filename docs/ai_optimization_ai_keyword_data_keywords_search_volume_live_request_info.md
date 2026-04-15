# AiOptimizationAiKeywordDataKeywordsSearchVolumeLiveRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keywords** | **List[Optional[StrictStr]]** | keywordsrequired fieldUTF-8 encodingThe maximum number of keywords you can specify: 1000;The maximum number of characters in a single keyword: 250;The keywords will be converted to lowercase format;learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article |[optional]|
**location_name** | **StrictStr** | full name of the locationrequired field if you don't specify location_codeNote: it is required to specify either location_name or location_codeyou can receive the list of available locations with their location_name by making a separate request to thehttps://api.dataforseo.com/v3/ai_optimization/ai_keyword_data/locations_and_languagesexample:United Kingdom |[optional]|
**location_code** | **StrictInt** | unique location identifierrequired field if you don't specify location_nameNote: it is required to specify either location_name or location_codeyou can receive the list of available locations with their location_code by making a separate request to the https://api.dataforseo.com/v3/ai_optimization/ai_keyword_data/locations_and_languagesexample:2840 |[optional]|
**language_name** | **StrictStr** | full name of the languagerequired field if you don't specify language_codeif you use this field, you don't need to specify language_codeyou can receive the list of available languages with their language_name by making a separate request to thehttps://api.dataforseo.com/v3/ai_optimization/ai_keyword_data/locations_and_languagesexample:English |[optional]|
**language_code** | **StrictStr** | language coderequired field if you don't specify language_nameif you use this field, you don't need to specify language_nameyou can receive the list of available languages with their language_code by making a separate request to thehttps://api.dataforseo.com/v3/ai_optimization/ai_keyword_data/locations_and_languagesexample:en |[optional]|
**tag** | **StrictStr** | user-defined task identifieroptional fieldthe character limit is 255you can use this parameter to identify the task and match it with the resultyou will find the specified tag value in the data object of the response |[optional]|