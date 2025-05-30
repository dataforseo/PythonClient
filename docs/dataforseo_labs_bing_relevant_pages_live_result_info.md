# DataforseoLabsBingRelevantPagesLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | search engine type |[optional]|
**target** | **StrictStr** | target domain in a POST array |[optional]|
**location_code** | **StrictFloat** | location code in a POST array<br>if there is no data, then the value is null |[optional]|
**language_code** | **StrictStr** | language code in a POST array<br>if there is no data, then the value is null |[optional]|
**total_count** | **StrictFloat** | total amount of results in our database relevant to your request |[optional]|
**items_count** | **StrictFloat** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[DataforseoLabsRelevantPagesLiveItem]]** | relevant pages and related data |[optional]|