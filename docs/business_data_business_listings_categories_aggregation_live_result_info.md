# BusinessDataBusinessListingsCategoriesAggregationLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**total_count** | **StrictInt** | <em>total number of results in our database relevant to your request</em> |[optional]|
**count** | **StrictInt** | <em>item types</em><br>the number of items in the <code>items</code> array |[optional]|
**offset** | **StrictStr** | <em>offset in the results array of returned categories</em> |[optional]|
**offset_token** | **Any** | <em>token for subsequent requests</em><br>by specifying the unique <code>offset_token</code> when setting a new task, you will get the subsequent results of the initial task;<br><code>offset_token</code> values are unique for each subsequent task |[optional]|
**items** | **List[Optional[BusinessDataBusinessListingsCategoriesAggregationLiveItem]]** | <em>encountered item types</em><br>types of search engine results encountered in the <code>items</code> array;<br>possible item types: <code>business_category</code> |[optional]|