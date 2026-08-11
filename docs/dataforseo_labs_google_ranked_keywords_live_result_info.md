# DataforseoLabsGoogleRankedKeywordsLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | <em>search engine type</em> |[optional]|
**target** | **StrictStr** | <em>target domain or webpage in a POST array</em> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em><br>            if there is no data, then the value is <code>null</code> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em><br>            if there is no data, then the value is <code>null</code> |[optional]|
**total_count** | **StrictInt** | <em>total number of results in our database relevant to your request</em> |[optional]|
**items_count** | **StrictInt** | <em>the number of results returned in the <code>items</code> array</em> |[optional]|
**metrics** | **Dict[str, Optional[DataforseoLabsMetricsInfo]]** | <em>ranking data relevant to the specified domain or webpage </em><br>            ranking data is provided by the <code>rank_group</code> parameters that show the result’s rank considering only equivalent SERP elements |[optional]|
**metrics_absolute** | **Dict[str, Optional[DataforseoLabsMetricsInfo]]** | <em>ranking data relevant to the specified domain or webpage</em><br>            ranking data is provided by the <code>rank_absolute</code> parameters that indicate the result’s position among all SERP elements |[optional]|
**items** | **List[Optional[DataforseoLabsGoogleRankedKeywordsLiveItem]]** | <em>contains ranked keywords and related data</em> |[optional]|