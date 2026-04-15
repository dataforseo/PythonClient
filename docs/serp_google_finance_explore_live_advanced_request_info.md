# SerpGoogleFinanceExploreLiveAdvancedRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**location_code** | **StrictInt** | search engine location coderequired field if you don't specify location_nameif you use this field, you don't need to specify location_nameyou can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/serp/google/locationsexample:2840 |[optional]|
**language_code** | **StrictStr** | search engine language coderequired field if you don't specify language_nameif you use this field, you don't need to specify language_nameyou can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/languagesexample:en |[optional]|
**device** | **StrictStr** | device typeoptional fieldreturn results for a specific device typepossible value: desktop |[optional]|
**location_name** | **StrictStr** | full name of search engine locationrequired field if you don't specify location_codeif you use this field, you don't need to specify location_codeyou can receive the list of available locations of the search engine with their location_name by making a separate request to https://api.dataforseo.com/v3/serp/google/locationsexample:London,England,United Kingdom |[optional]|
**language_name** | **StrictStr** | full name of search engine languagerequired field if you don't specify language_codeif you use this field, you don't need to specify language_codeyou can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/serp/google/languagesexample:English |[optional]|
**os** | **StrictStr** | device operating systemoptional fieldpossible values: windows |[optional]|
**tag** | **StrictStr** | user-defined task identifieroptional fieldthe character limit is 255you can use this parameter to identify the task and match it with the resultyou will find the specified tag value in the data object of the response |[optional]|
**news_type** | **StrictStr** | financial news filtersoptional fieldpossible values: top_stories, local_market, world_marketsdefault value: top_storiesNote: if you specify local_market or world_markets, the charge per task will be multiplied by 2 |[optional]|