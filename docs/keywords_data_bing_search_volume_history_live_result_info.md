# KeywordsDataBingSearchVolumeHistoryLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | <em>keyword in a POST array</em> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em><br>if there is no data, then the value is_<code>null</code>n |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em><br>if there is no data, then the value is_<code>null</code>n |[optional]|
**device** | **List[Optional[StrictStr]]** |  |[optional]|
**period** | **StrictStr** | <em>time period</em><br>indicates if returned data is aggregated to a certain time period<br>default value <code>monthly</code> |[optional]|
**searches** | **SearchVolumeHistorySearchInfo** | <em>contains results distributed by device type</em><br>if the <code>device</code> parameter is not specified, the data will be returned for all available device types |[optional]|