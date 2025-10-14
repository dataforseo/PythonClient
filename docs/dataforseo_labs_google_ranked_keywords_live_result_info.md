# DataforseoLabsGoogleRankedKeywordsLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | search engine type |[optional]|
**target** | **StrictStr** | target domain or webpage in a POST array |[optional]|
**location_code** | **StrictInt** | location code in a POST array<br>if there is no data, then the value is null |[optional]|
**language_code** | **StrictStr** | language code in a POST array<br>if there is no data, then the value is null |[optional]|
**total_count** | **StrictInt** | total number of results in our database relevant to your request |[optional]|
**items_count** | **StrictInt** | the number of results returned in the items array |[optional]|
**metrics** | **Dict[str, Optional[DataforseoLabsMetricsInfo]]** | ranking data relevant to the specified domain or webpage <br>ranking data is provided by the rank_group parameters that show the result’s rank considering only equivalent SERP elements |[optional]|
**metrics_absolute** | **Dict[str, Optional[DataforseoLabsMetricsInfo]]** | ranking data relevant to the specified domain or webpage<br>ranking data is provided by the rank_absolute parameters that indicate the result’s position among all SERP elements |[optional]|
**items** | **List[Optional[DataforseoLabsRankedKeywordsLiveItem]]** | contains ranked keywords and related data |[optional]|