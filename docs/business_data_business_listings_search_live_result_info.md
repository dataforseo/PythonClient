# BusinessDataBusinessListingsSearchLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**total_count** | **StrictInt** | total number of results in our database relevant to your request |[optional]|
**count** | **StrictInt** | item types<br>the number of items in the items array |[optional]|
**offset** | **StrictInt** | offset in the results array of returned businesses |[optional]|
**offset_token** | **StrictStr** | token for subsequent requests<br>by specifying the unique offset_token when setting a new task, you will get the subsequent results of the initial task;<br>offset_token values are unique for each subsequent task |[optional]|
**items** | **List[Optional[BusinessDataBusinessListingsSearchLiveItem]]** | encountered item types<br>types of search engine results encountered in the items array;<br>possible item types: business_listing |[optional]|