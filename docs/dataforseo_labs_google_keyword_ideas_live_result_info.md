# DataforseoLabsGoogleKeywordIdeasLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | <em>search engine type</em> |[optional]|
**seed_keywords** | **List[Optional[StrictStr]]** | <em>keywords in a POST array</em><br><strong>keywords are returned with decoded %## (plus character '+' will be decoded to a space character)</strong> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em> |[optional]|
**total_count** | **StrictInt** | <em>total number of results relevant to your request in our database </em> |[optional]|
**items_count** | **StrictInt** | <em>number of results returned in the <code>items</code> array</em> |[optional]|
**offset** | **StrictInt** | <em>current offset value</em> |[optional]|
**offset_token** | **StrictStr** | <em>offset token for subsequent requests</em><br>you can use the string provided in this field to get the subsequent results of the initial task;<br><strong>note:</strong> <code>offset_token</code> values are unique for each subsequent task |[optional]|
**items** | **List[Optional[KeywordDataInfo]]** | <em>contains keyword ideas and related data</em> |[optional]|