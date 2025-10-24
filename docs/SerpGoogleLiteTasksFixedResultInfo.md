# SerpGoogleLiteTasksFixedResultInfo

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**id** | **string** | task identifier of the completed task<br>unique task identifier in our system in the UUID format |[optional]|
**se** | **string** | search engine specified when setting the task |[optional]|
**se_type** | **string** | type of search engine<br>can take the following values: lite |[optional]|
**date_posted** | **string** |  |[optional]|
**tag** | **string** | user-defined task identifier |[optional]|
**endpoint_regular** | **string** | URL for collecting the results of the SERP Regular task<br>if SERP Regular is not supported in the specified endpoint, the value will be null |[optional]|
**endpoint_advanced** | **string** | URL for collecting the results of the SERP Advanced task<br>if SERP Advanced is not supported in the specified endpoint, the value will be null |[optional]|
**endpoint_html** | **string** | URL for collecting the results of the SERP HTML task<br>if SERP HTML is not supported in the specified endpoint, the value will be null |[optional]|