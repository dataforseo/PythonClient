# BacklinksBacklinksLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**target** | **StrictStr** | <em>target domain in a POST array</em> |[optional]|
**mode** | **StrictStr** | <em>mode specified in a POST array</em> |[optional]|
**custom_mode** | **Dict[str, Optional[Any]]** | <em>custom mode specified in a POST array</em> |[optional]|
**total_count** | **StrictInt** | <em>total amount of results relevant the request</em> |[optional]|
**items_count** | **StrictInt** | <em>the number of results returned in the <code>items</code> array</em> |[optional]|
**items** | **List[Optional[BacklinksBacklinksLiveItem]]** | <em>contains relevant backlinks and referring domains data</em> |[optional]|
**search_after_token** | **StrictStr** | <em>token for subsequent requests</em><br>by specifying the unique <code>search_after_token</code> when setting a new task, you will get the subsequent results of the initial task;<br><code>search_after_token</code> values are unique for each subsequent task |[optional]|