# DataforseoLabsAppleAppIntersectionLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | <em>search engine type</em> |[optional]|
**app_ids** | **Dict[str, Optional[StrictStr]]** | <em>ids of the apps in a POST array</em> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em> |[optional]|
**total_count** | **StrictInt** | <em>total amount of results in our database relevant to your request</em> |[optional]|
**items_count** | **StrictInt** | <em>the number of results returned in the <code>items</code> array</em> |[optional]|
**items** | **List[Optional[DataforseoLabsleAppIntersectionLiveItem]]** | <em>contains data related to the ranking keywords for the app specified in the <code>app_id</code> field</em> |[optional]|