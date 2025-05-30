# MerchantGoogleProductSpecTasksReadyResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**id** | **StrictStr** | task identifier of the completed task<br>unique task identifier in our system in the UUID format |[optional]|
**se** | **StrictStr** | search engine specified when setting the task |[optional]|
**se_type** | **StrictStr** | type of search engine<br>can take the following values: shopping_specifications |[optional]|
**date_posted** | **StrictStr** | date when the task was posted (in the UTC format) |[optional]|
**tag** | **StrictStr** | user-defined task identifier |[optional]|
**endpoint_advanced** | **StrictStr** | URL for collecting the results of the Google Shopping Product Specifications Advanced task |[optional]|
**endpoint_html** | **StrictStr** | URL for collecting the results of the Google Shopping Product Specifications HTML task |[optional]|