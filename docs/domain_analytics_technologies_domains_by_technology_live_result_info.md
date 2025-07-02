# DomainAnalyticsTechnologiesDomainsByTechnologyLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**total_count** | **StrictInt** | total number of relevant items in the database |[optional]|
**items_count** | **StrictInt** | number of items in the results array |[optional]|
**offset** | **StrictInt** | specified offset value |[optional]|
**offset_token** | **StrictStr** | token for subsequent requests<br>by specifying the unique offset_token when setting a new task, you will get the subsequent results of the initial task;<br>offset_token values are unique for each subsequent task |[optional]|
**items** | **List[Optional[DomainAnalyticsTechnologiesDomainsByLiveItem]]** | items array |[optional]|