# KeywordsDataBingSearchVolumeHistoryTaskGetResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | keyword in a POST array |[optional]|
**location_code** | **StrictInt** | location code in a POST array<br>if there is no data, then the value is null |[optional]|
**language_code** | **StrictStr** | language code in a POST array<br>if there is no data, then the value is null |[optional]|
**device** | **List[Optional[StrictStr]]** |  |[optional]|
**period** | **StrictStr** | time period<br>indicates if returned data is aggregated to a certain time period<br>default value monthly |[optional]|
**searches** | **SearchVolumeHistorySearchInfo** | contains results distributed by device type<br>if the device parameter is not specified, the data will be returned for all available device types |[optional]|