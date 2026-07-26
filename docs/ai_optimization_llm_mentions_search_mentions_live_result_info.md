# AiOptimizationLlmMentionsSearchMentionsLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**total_count** | **StrictInt** | <em>total amount of results relevant the request</em> |[optional]|
**offset** | **StrictInt** |  |[optional]|
**search_after_token** | **StrictStr** | <em>token for subsequent requests</em><br>by specifying the unique <code>search_after_token</code> when setting a new task, you will get the subsequent results of the initial task;<br><code>search_after_token</code> values are unique for each subsequent task |[optional]|
**items_count** | **StrictInt** | <em>the number of results returned in the <code>items</code> array</em> |[optional]|
**items** | **List[Optional[AiOptimizationLlmMentionsSearchMentionsLiveItem]]** | <em>contains relevant mentions data</em> |[optional]|