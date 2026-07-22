# BusinessDataBusinessListingsSearchLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**total_count** | **StrictInt** | total number of results in our database relevant to your request |[optional]|
**count** | **StrictInt** | item types<br>the number of items in the items array |[optional]|
**offset** | **StrictInt** |  |[optional]|
**offset_token** | **StrictStr** |  |[optional]|
**items** | **List[Optional[BusinessDataBusinessListingsSearchLiveItem]]** | encountered item types<br>types of search engine results encountered in the items array;<br>possible item types: business_listing |[optional]|