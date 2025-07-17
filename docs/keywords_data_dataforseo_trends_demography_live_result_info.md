# KeywordsDataDataforseoTrendsDemographyLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keywords** | **List[Optional[StrictStr]]** | keywords in a POST array |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**location_code** | **StrictInt** | location code in a POST array<br>if there is no data, then the value is null |[optional]|
**language_code** | **StrictStr** | language code in a POST array<br>if there is no data, then the value is null |[optional]|
**datetime** | **StrictStr** | date and time when the result was received<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**items_count** | **StrictInt** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[DataforseoTrendsDemographyElementItem]]** | contains keyword popularity and related data |[optional]|