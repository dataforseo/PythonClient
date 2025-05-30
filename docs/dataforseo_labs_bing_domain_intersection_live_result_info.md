# DataforseoLabsBingDomainIntersectionLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | search engine type<br>search engine type specified in a POST request;<br>for this endpoint, the field equals bing |[optional]|
**target_1** | **StrictStr** | target specified in a POST array |[optional]|
**target_2** | **StrictStr** | target specified in a POST array |[optional]|
**location_code** | **StrictFloat** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**total_count** | **StrictFloat** | total amount of results in our database relevant to your request |[optional]|
**items_count** | **StrictFloat** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[DataforseoLabsDomainIntersectionLiveItem]]** | contains keywords, relevant SERP elements and related data |[optional]|