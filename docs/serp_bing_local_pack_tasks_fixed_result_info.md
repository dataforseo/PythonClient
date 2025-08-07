# SerpBingLocalPackTasksFixedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**id** | **StrictStr** | task identifier of the completed task<br>unique task identifier in our system in the UUID format |[optional]|
**se** | **StrictStr** | search engine specified when setting the task |[optional]|
**se_type** | **StrictStr** | type of search engine<br>can take the following values: local_pack |[optional]|
**date_posted** | **StrictStr** |  |[optional]|
**tag** | **StrictStr** | user-defined task identifier |[optional]|
**endpoint_regular** | **StrictStr** | URL for collecting the results of the SERP Regular task<br>if SERP Regular is not supported in the specified endpoint, the value will be null |[optional]|
**endpoint_advanced** | **StrictStr** | URL for collecting the results of the SERP Advanced task<br>if SERP Advanced is not supported in the specified endpoint, the value will be null |[optional]|
**endpoint_html** | **StrictStr** | URL for collecting the results of the SERP HTML task<br>if SERP HTML is not supported in the specified endpoint, the value will be null |[optional]|