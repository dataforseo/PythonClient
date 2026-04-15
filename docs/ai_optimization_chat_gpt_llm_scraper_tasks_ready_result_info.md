# AiOptimizationChatGptLlmScraperTasksReadyResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**id** | **StrictStr** | task identifier of the completed taskunique task identifier in our system in the UUID format |[optional]|
**se** | **StrictStr** | search engine specified when setting the task |[optional]|
**se_type** | **StrictStr** | type of search engineexample: llm_scraper |[optional]|
**date_posted** | **StrictStr** | date when the task was posted (in the UTC format) |[optional]|
**tag** | **StrictStr** | user-defined task identifier |[optional]|
**endpoint_regular** | **StrictStr** | URL for collecting the results of the Regular taskif the Regular function is not supported in the specified endpoint, the value will be null |[optional]|
**endpoint_advanced** | **StrictStr** | URL for collecting the results of the Advanced taskif the Advanced function is not supported in the specified endpoint, the value will be null |[optional]|
**endpoint_html** | **StrictStr** | URL for collecting the results of the HTML taskif the HTML function is not supported in the specified endpoint, the value will be null |[optional]|