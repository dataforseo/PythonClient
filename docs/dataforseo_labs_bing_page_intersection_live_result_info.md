# DataforseoLabsBingPageIntersectionLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | search engine type<br>search engine type specified in a POST request;<br>for this endpoint, the field equals bing |[optional]|
**pages** | **Dict[str, Optional[StrictStr]]** | URLs you specified a POST array |[optional]|
**exclude_pages** | **List[Optional[StrictStr]]** | URLs you specified in a POST array that will be excluded from the results |[optional]|
**location_code** | **StrictInt** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**total_count** | **StrictInt** | total amount of results in our database relevant to your request |[optional]|
**items_count** | **StrictInt** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[DataforseoLabsPageIntersectionLiveItem]]** | contains keywords, relevant SERP elements and related data |[optional]|