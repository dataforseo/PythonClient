# BacklinksBacklinksLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**target** | **StrictStr** | target domain in a POST array |[optional]|
**mode** | **StrictStr** | mode specified in a POST array |[optional]|
**custom_mode** | **Dict[str, Optional[Any]]** | custom mode specified in a POST array |[optional]|
**total_count** | **StrictInt** | total amount of results relevant the request |[optional]|
**items_count** | **StrictInt** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[BacklinksBacklinksLiveItem]]** | contains relevant backlinks and referring domains data |[optional]|
**search_after_token** | **StrictStr** | token for subsequent requests<br>by specifying the unique search_after_token when setting a new task, you will get the subsequent results of the initial task;<br>search_after_token values are unique for each subsequent task |[optional]|