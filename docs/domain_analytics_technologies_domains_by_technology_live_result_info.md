# DomainAnalyticsTechnologiesDomainsByTechnologyLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**total_count** | **StrictInt** | <em>total number of relevant items in the database</em> |[optional]|
**items_count** | **StrictInt** | <em>number of items in the results array</em> |[optional]|
**offset** | **StrictInt** | <em>specified offset value</em> |[optional]|
**offset_token** | **StrictStr** | <em>token for subsequent requests</em><br>by specifying the unique <code>offset_token</code> when setting a new task, you will get the subsequent results of the initial task;<br><code>offset_token</code> values are unique for each subsequent task |[optional]|
**items** | **List[Optional[DomainAnalyticsTechnologiesDomainsByLiveItem]]** | <em>items array</em> |[optional]|