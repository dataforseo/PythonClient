# AiOptimizationLlmMentionsSearchLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**total_count** | **StrictInt** | total amount of results relevant the request |[optional]|
**current_offset** | **StrictInt** | the number of mentions objects that are omitted in the items array |[optional]|
**search_after_token** | **StrictStr** | token for subsequent requests<br>by specifying the unique search_after_token when setting a new task, you will get the subsequent results of the initial task;<br>search_after_token values are unique for each subsequent task |[optional]|
**items_count** | **StrictInt** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[AiOptimizationLlmMentionsSearchLiveItem]]** | contains relevant mentions data |[optional]|