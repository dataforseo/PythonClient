# SerpGoogleLocalFinderTasksReadyResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**id** | **StrictStr** | <em>task identifier of the completed task</em><br><strong>unique task identifier in our system in the <a href='https://en.wikipedia.org/wiki/Universally_unique_identifier'>UUID</a> format</strong> |[optional]|
**se** | **StrictStr** | <em>search engine specified when setting the task</em> |[optional]|
**se_type** | **StrictStr** | <em>type of search engine</em><br>example: <code>{{low_se_type_under}}</code> |[optional]|
**date_posted** | **StrictStr** | <em>date when the task was posted (in the UTC format)</em> |[optional]|
**tag** | **StrictStr** | <em>user-defined task identifier</em> |[optional]|
**endpoint_regular** | **StrictStr** | <em>URL for collecting the results of the SERP Regular task</em><br>if SERP Regular is not supported in the specified endpoint, the value will be <code>null</code> |[optional]|
**endpoint_advanced** | **StrictStr** | <em>URL for collecting the results of the SERP Advanced task</em><br>if SERP Advanced is not supported in the specified endpoint, the value will be <code>null</code> |[optional]|
**endpoint_html** | **StrictStr** | <em>URL for collecting the results of the SERP HTML task</em><br>if SERP HTML is not supported in the specified endpoint, the value will be <code>null</code> |[optional]|