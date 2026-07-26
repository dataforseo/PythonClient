# AiOptimizationChatGptLlmResponsesTasksReadyResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**id** | **StrictStr** | <em>task identifier of the completed task</em><br><strong>unique task identifier in our system in the <a href='https://en.wikipedia.org/wiki/Universally_unique_identifier'>UUID</a> format</strong> |[optional]|
**se** | **StrictStr** | <em>LLM model specified when setting the task</em> |[optional]|
**se_type** | **StrictStr** |  |[optional]|
**date_posted** | **StrictStr** | <em>date when the task was posted (in the UTC format)</em> |[optional]|
**tag** | **StrictStr** | <em>user-defined task identifier</em> |[optional]|
**endpoint** | **StrictStr** | <em>URL for collecting the results of the task</em> |[optional]|