# DataforseoLabsAmazonRelatedKeywordsLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | <em>search engine type</em> |[optional]|
**seed_keyword** | **StrictStr** | <em>keyword in a POST array</em> |[optional]|
**seed_keyword_data** | **AmazonKeywordData** | <em>keyword data for the seed keyword</em><br>fields in the object are identical to that of <code>keyword_data</code> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em> |[optional]|
**total_count** | **StrictInt** | <em>total amount of results in our database relevant to your request</em> |[optional]|
**items_count** | **StrictInt** | <em>the number of results returned in the <code>items</code> array</em> |[optional]|
**items** | **List[Optional[DataforseoLabsAmazonRelatedKeywordsLiveItem]]** | <em>contains objects with keywords and related data</em> |[optional]|