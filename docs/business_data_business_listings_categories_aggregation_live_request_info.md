# BusinessDataBusinessListingsCategoriesAggregationLiveRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**categories** | **List[Optional[StrictStr]]** | business categories<br>optional field<br>the categories you specify are used to search for business listings;<br>if you don’t use this field, we will return business listings found in the specified location;<br>you can specify up to 10 categories |[optional]|
**description** | **StrictStr** | description of the element in SERP<br>optional field<br>the description of the business entity for which the results are collected;<br>can contain up to 200 characters |[optional]|
**title** | **StrictStr** | title of the element in SERP<br>optional field<br>the name of the business entity for which the results are collected;<br>can contain up to 200 characters |[optional]|
**is_claimed** | **StrictBool** | indicates whether the business is verified by its owner on Google Maps<br>optional field |[optional]|
**location_coordinate** | **StrictStr** | GPS coordinates of a location<br>optional field<br>location_coordinate parameter should be specified in the “latitude,longitude,radius” format<br>the maximum number of decimal digits for “latitude” and “longitude”: 7<br>the minimum value for “radius”: 1<br>the maximum value for “radius”: 100000<br>example:<br>53.476225,-2.243572,200 |[optional]|
**initial_dataset_filters** | **List[Optional[Any]]** | array of results filtering parameters<br>optional field<br>you can add several filters at once (8 filters maximum)<br>you should set a logical operator and, or between the conditions<br>the following operators are supported:<br>regex, not_regex, <, <=, >, >=, =, <>, in, not_in, like, not_like, match, not_match<br>you can use the % operator with like and not_like to match any string of zero or more characters<br>example:<br>['rating.value','>',3]<br>you can receive the list of available filters by making a separate request to https://api.dataforseo.com/v3/business_data/business_listings/available_filters |[optional]|
**internal_list_limit** | **StrictInt** | maximum number of elements within internal arrays<br>optional field<br>you can use this field to limit the number of elements within the aggregated categories<br>default value: 10 |[optional]|
**limit** | **StrictInt** | the maximum number of returned businesses<br>optional field<br>default value: 100<br>maximum value: 1000 |[optional]|
**offset** | **StrictInt** | the maximum number of returned businesses<br>optional field |[optional]|
**tag** | **StrictStr** | user-defined task identifier<br>optional field<br>the character limit is 255<br>you can use this parameter to identify the task and match it with the result<br>you will find the specified tag value in the data object of the response |[optional]|