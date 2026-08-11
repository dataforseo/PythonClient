# SerpSeznamLocationsResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**location_code** | **StrictInt** | <em>location code</em> |[optional]|
**location_name** | **StrictStr** | <em>full name of the location</em> |[optional]|
**location_code_parent** | **StrictInt** | <em>the code of the superordinate location</em><br>only <code>City</code> <code>location_type</code> is supported for all countries except China (where <code>Country</code> is also supported);<br>don't match locations by <code>location_code_parent</code> because the results for <code>Region</code> and <code>Country</code>-level results for most countries are not supported by Baidu SERP API |[optional]|
**country_iso_code** | **StrictStr** | <em>ISO country code of the location</em> |[optional]|
**location_type** | **StrictStr** | <em>location type</em> |[optional]|