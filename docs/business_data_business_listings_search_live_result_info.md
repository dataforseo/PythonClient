# BusinessDataBusinessListingsSearchLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**total_count** | **StrictInt** | <em>total number of results in our database relevant to your request</em> |[optional]|
**count** | **StrictInt** | <em>item types</em><br>the number of items in the <code>items</code> array |[optional]|
**offset** | **StrictInt** |  |[optional]|
**offset_token** | **StrictStr** |  |[optional]|
**items** | **List[Optional[BusinessDataBusinessListingsSearchLiveItem]]** | <em>encountered item types</em><br>types of search engine results encountered in the <code>items</code> array;<br>possible item types: <code>business_listing</code> |[optional]|