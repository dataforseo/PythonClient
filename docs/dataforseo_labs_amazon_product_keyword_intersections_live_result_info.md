# DataforseoLabsAmazonProductKeywordIntersectionsLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | <em>search engine type</em> |[optional]|
**asins** | **Dict[str, Optional[StrictStr]]** | <em>ASINs in a POST array</em> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em><br>if there is no data, then the value is_<code>null</code> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em><br>if there is no data, then the value is_<code>null</code> |[optional]|
**total_count** | **StrictInt** | <em>total amount of results in our database relevant to your request</em> |[optional]|
**items_count** | **StrictInt** | <em>the number of results returned in the <code>items</code> array</em> |[optional]|
**items** | **List[Optional[DataforseoLabsAmazonProductKeywordIntersectionsLiveItem]]** | <em>contains detected Amazon product competitors and related data</em> |[optional]|