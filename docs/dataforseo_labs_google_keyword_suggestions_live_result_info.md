# DataforseoLabsGoogleKeywordSuggestionsLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | <em>search engine type</em> |[optional]|
**seed_keyword** | **StrictStr** | <em>keyword in a POST array</em> |[optional]|
**seed_keyword_data** | **KeywordDataInfo** | <em>keyword data for the seed keyword</em><br>fields in this object are identical to those of the <code>items</code> array |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em><br>if there is no data, then the value is_<code>null</code>n |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em><br>if there is no data, then the value is_<code>null</code>n |[optional]|
**total_count** | **StrictInt** | <em>total amount of results in our database relevant to your request</em> |[optional]|
**items_count** | **StrictInt** | <em>the number of results returned in the <code>items</code> array</em> |[optional]|
**offset** | **StrictInt** | <em>current offset value</em> |[optional]|
**offset_token** | **StrictStr** | <em>offset token for subsequent requests</em><br>you can use the string provided in this field to get the subsequent results of the initial task;<br><strong>note:</strong> <code>offset_token</code> values are unique for each subsequent task |[optional]|
**items** | **List[Optional[KeywordDataInfo]]** | <em>contains keywords and related data</em> |[optional]|