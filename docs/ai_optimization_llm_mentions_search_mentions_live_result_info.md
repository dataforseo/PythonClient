# AiOptimizationLlmMentionsSearchMentionsLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**total_count** | **StrictInt** | total amount of results relevant the request |[optional]|
**offset** | **StrictInt** |  |[optional]|
**search_after_token** | **StrictStr** | token for subsequent requests<br>by specifying the unique search_after_token when setting a new task, you will get the subsequent results of the initial task;<br>search_after_token values are unique for each subsequent task |[optional]|
**items_count** | **StrictInt** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[AiOptimizationLlmMentionsSearchMentionsLiveItem]]** | contains relevant mentions data |[optional]|