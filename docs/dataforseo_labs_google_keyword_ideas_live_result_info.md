# DataforseoLabsGoogleKeywordIdeasLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | search engine type |[optional]|
**seed_keywords** | **List[Optional[StrictStr]]** | keywords in a POST array<br>keywords are returned with decoded %## (plus character ‘+’ will be decoded to a space character) |[optional]|
**location_code** | **StrictFloat** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**total_count** | **StrictFloat** | total number of results relevant to your request in our database |[optional]|
**items_count** | **StrictFloat** | number of results returned in the items array |[optional]|
**offset** | **StrictFloat** | current offset value |[optional]|
**offset_token** | **StrictStr** | offset token for subsequent requests<br>you can use the string provided in this field to get the subsequent results of the initial task;<br>note: offset_token values are unique for each subsequent task |[optional]|
**items** | **List[Optional[KeywordDataInfo]]** | contains keyword ideas and related data |[optional]|