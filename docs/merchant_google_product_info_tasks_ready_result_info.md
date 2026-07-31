# MerchantGoogleProductInfoTasksReadyResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**id** | **StrictStr** | <em>task identifier of the completed task</em><br><strong>unique task identifier in our system in the <a href='https://en.wikipedia.org/wiki/Universally_unique_identifier'>UUID</a> format</strong> |[optional]|
**se** | **StrictStr** | <em>search engine specified when setting the task</em> |[optional]|
**se_type** | **StrictStr** | <em>type of search engine</em><br>can take the following values: <code>shopping_specifications</code> |[optional]|
**date_posted** | **StrictStr** | <em>date when the task was posted (in the UTC format)</em> |[optional]|
**tag** | **StrictStr** |  |[optional]|
**endpoint_advanced** | **StrictStr** | <em>URL for collecting the results of the Google Shopping Product Specifications Advanced task</em> |[optional]|
**endpoint_html** | **StrictStr** | <em>URL for collecting the results of the Google Shopping Product Specifications HTML task</em><br><strong>note:</strong> HTML is not available for this endpoint, the value will be <code>null</code> |[optional]|