# SerpBaiduLocationsResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**location_code** | **StrictFloat** | location code |[optional]|
**location_name** | **StrictStr** | full name of the location |[optional]|
**location_code_parent** | **StrictFloat** | the code of the superordinate location<br>only City location_type is supported for all countries except China (where Country is also supported);<br>don’t match locations by location_code_parent because the results for Region and Country-level results for most countries are not supported by Baidu SERP API |[optional]|
**country_iso_code** | **StrictStr** | ISO country code of the location |[optional]|
**location_type** | **StrictStr** | location type<br>only City is supported for all countries except China (where Country is also supported) |[optional]|