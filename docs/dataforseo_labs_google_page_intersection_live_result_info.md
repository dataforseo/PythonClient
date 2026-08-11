# DataforseoLabsGooglePageIntersectionLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | <em>search engine type</em> |[optional]|
**pages** | **Dict[str, Optional[StrictStr]]** | <em>URLs you specified a POST array</em> |[optional]|
**exclude_pages** | **List[Optional[StrictStr]]** | <em>URLs you specified in a POST array that will be excluded from the results</em> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em> |[optional]|
**total_count** | **StrictInt** | <em>total amount of results in our database relevant to your request</em> |[optional]|
**items_count** | **StrictInt** | <em>the number of results returned in the <code>items</code> array</em> |[optional]|
**items** | **List[Optional[DataforseoLabsGooglePageIntersectionLiveItem]]** | <em>contains keywords, relevant SERP elements and related data</em> |[optional]|