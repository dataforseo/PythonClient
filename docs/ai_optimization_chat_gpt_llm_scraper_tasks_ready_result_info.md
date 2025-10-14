# AiOptimizationChatGptLlmScraperTasksReadyResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**id** | **StrictStr** | task identifier of the completed task<br>unique task identifier in our system in the UUID format |[optional]|
**se** | **StrictStr** | search engine specified when setting the task |[optional]|
**se_type** | **StrictStr** | type of search engine<br>example: llm_scraper |[optional]|
**date_posted** | **StrictStr** | date when the task was posted (in the UTC format) |[optional]|
**tag** | **StrictStr** | user-defined task identifier |[optional]|
**endpoint_regular** | **StrictStr** | URL for collecting the results of the Regular task<br>if the Regular function is not supported in the specified endpoint, the value will be null |[optional]|
**endpoint_advanced** | **StrictStr** | URL for collecting the results of the Advanced task<br>if the Advanced function is not supported in the specified endpoint, the value will be null |[optional]|
**endpoint_html** | **StrictStr** | URL for collecting the results of the HTML task<br>if the HTML function is not supported in the specified endpoint, the value will be null |[optional]|