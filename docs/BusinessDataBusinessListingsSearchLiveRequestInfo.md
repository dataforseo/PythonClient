# BusinessDataBusinessListingsSearchLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **List[str]** | business categories optional field the categories you specify are used to search for business listings; if you don’t use this field, we will return business listings found in the specified location; you can specify up to 10 categories | [optional] 
**description** | **str** | description of the element in SERP optional field the description of the business entity for which the results are collected; can contain up to 200 symbols | [optional] 
**title** | **str** | title of the element in SERP optional field the name of the business entity for which the results are collected; can contain up to 200 symbols | [optional] 
**is_claimed** | **bool** | indicates whether the business is verified by its owner on Google Maps optional field | [optional] 
**location_coordinate** | **str** | GPS coordinates of a location optional field location_coordinate parameter should be specified in the “latitude,longitude,radius” format the maximum number of decimal digits for “latitude” and “longitude”: 7 the minimum value for “radius”: 1 the maximum value for “radius”: 100000 example: 53.476225,-2.243572,200 | [optional] 
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, not_regex, &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, &#x3D;, &lt;&gt;, in, not_in, like, not_like you can use the % operator with like and not_like to match any string of zero or more characters example: [\&quot;rating.value\&quot;,\&quot;&gt;\&quot;,3] you can receive the list of available filters by making a separate request to https://api.dataforseo.com/v3/business_data/business_listings/available_filters | [optional] 
**order_by** | **List[str]** | results sorting rules optional field you can use the same values as in the filters array to sort the results possible sorting types: asc – results will be sorted in the ascending order desc – results will be sorted in the descending order you should use a comma to set up a sorting parameter example: [\&quot;rating.value,desc\&quot;]note that you can set no more than three sorting rules in a single request you should use a comma to separate several sorting rules example: [\&quot;rating.value,desc\&quot;,\&quot;rating.votes_count,desc\&quot;] | [optional] 
**limit** | **int** | the maximum number of returned businesses optional field default value: 100 maximum value: 1000 | [optional] 
**offset** | **int** | offset in the results array of returned businesses optional field default value: 0 if you specify the 10 value, the first ten entities in the results array will be omitted and the data will be provided for the successive entities | [optional] 
**offset_token** | **str** | token for subsequent requests optional field provided in the identical filed of the response to each request; use this parameter to avoid timeouts while trying to obtain over 100,000 results in a single request; by specifying the unique offset_token value from the response array, you will get the subsequent results of the initial task; offset_token values are unique for each subsequent task Note: if the offset_token is specified in the request, all other parameters should be identical to the previous request | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.business_data_business_listings_search_live_request_info import BusinessDataBusinessListingsSearchLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataBusinessListingsSearchLiveRequestInfo from a JSON string
business_data_business_listings_search_live_request_info_instance = BusinessDataBusinessListingsSearchLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print BusinessDataBusinessListingsSearchLiveRequestInfo.to_json()

# convert the object into a dict
business_data_business_listings_search_live_request_info_dict = business_data_business_listings_search_live_request_info_instance.to_dict()
# create an instance of BusinessDataBusinessListingsSearchLiveRequestInfo from a dict
business_data_business_listings_search_live_request_info_form_dict = business_data_business_listings_search_live_request_info.from_dict(business_data_business_listings_search_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


