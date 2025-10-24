# AiOptimizationClaudeLlmResponsesTasksReadyResultInfo

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**id** | **string** | task identifier of the completed task<br>unique task identifier in our system in the UUID format |[optional]|
**se** | **string** | LLM model specified when setting the task |[optional]|
**se_type** | **string** |  |[optional]|
**date_posted** | **string** | date when the task was posted (in the UTC format) |[optional]|
**tag** | **string** | user-defined task identifier |[optional]|
**endpoint** | **string** | URL for collecting the results of the task |[optional]|