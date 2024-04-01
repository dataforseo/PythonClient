# BusinessDataBusinessListingsCategoriesAggregationLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **List[str]** | business categories optional field the categories you specify are used to search for business listings; if you don’t use this field, we will return business listings found in the specified location; you can specify up to 10 categories | [optional] 
**description** | **str** | description of the element in SERP optional field the description of the business entity for which the results are collected; can contain up to 200 symbols | [optional] 
**title** | **str** | title of the element in SERP optional field the name of the business entity for which the results are collected; can contain up to 200 symbols | [optional] 
**is_claimed** | **bool** | indicates whether the business is verified by its owner on Google Maps optional field | [optional] 
**location_coordinate** | **str** | GPS coordinates of a location optional field location_coordinate parameter should be specified in the “latitude,longitude,radius” format the maximum number of decimal digits for “latitude” and “longitude”: 7 the minimum value for “radius”: 1 the maximum value for “radius”: 100000 example: 53.476225,-2.243572,200 | [optional] 
**initial_dataset_filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, &#x3D;, &lt;&gt;, in, not_in, like, not_like you can use the % operator with like and not_like to match any string of zero or more characters example: [\&quot;rating.value\&quot;,\&quot;&gt;\&quot;,3] you can receive the list of available filters by making a separate request to https://api.dataforseo.com/v3/business_data/business_listings/available_filters | [optional] 
**internal_list_limit** | **int** | maximum number of elements within internal arrays optional field you can use this field to limit the number of elements within the aggregated categories default value: 10 | [optional] 
**limit** | **int** | the maximum number of returned businesses optional field default value: 100 maximum value: 1000 | [optional] 
**offset** | **int** | the maximum number of returned businesses optional field | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.business_data_business_listings_categories_aggregation_live_request_info import BusinessDataBusinessListingsCategoriesAggregationLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataBusinessListingsCategoriesAggregationLiveRequestInfo from a JSON string
business_data_business_listings_categories_aggregation_live_request_info_instance = BusinessDataBusinessListingsCategoriesAggregationLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(BusinessDataBusinessListingsCategoriesAggregationLiveRequestInfo.to_json())

# convert the object into a dict
business_data_business_listings_categories_aggregation_live_request_info_dict = business_data_business_listings_categories_aggregation_live_request_info_instance.to_dict()
# create an instance of BusinessDataBusinessListingsCategoriesAggregationLiveRequestInfo from a dict
business_data_business_listings_categories_aggregation_live_request_info_form_dict = business_data_business_listings_categories_aggregation_live_request_info.from_dict(business_data_business_listings_categories_aggregation_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


