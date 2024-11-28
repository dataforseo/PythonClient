# BusinessDataBusinessListingsCategoriesAggregationLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | total number of results in our database relevant to your request | [optional] 
**count** | **int** | item types the number of items in the items array | [optional] 
**offset** | **int** | offset in the results array of returned categories | [optional] 
**offset_token** | **str** | token for subsequent requests by specifying the unique offset_token when setting a new task, you will get the subsequent results of the initial task; offset_token values are unique for each subsequent task | [optional] 
**items** | [**List[BusinessDataBusinessListingsCategoriesAggregationLiveItem]**](BusinessDataBusinessListingsCategoriesAggregationLiveItem.md) | encountered item types types of search engine results encountered in the items array; possible item types: business_category | [optional] 

## Example

```python
from dataforseo_client.models.business_data_business_listings_categories_aggregation_live_result_info import BusinessDataBusinessListingsCategoriesAggregationLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataBusinessListingsCategoriesAggregationLiveResultInfo from a JSON string
business_data_business_listings_categories_aggregation_live_result_info_instance = BusinessDataBusinessListingsCategoriesAggregationLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(BusinessDataBusinessListingsCategoriesAggregationLiveResultInfo.to_json())

# convert the object into a dict
business_data_business_listings_categories_aggregation_live_result_info_dict = business_data_business_listings_categories_aggregation_live_result_info_instance.to_dict()
# create an instance of BusinessDataBusinessListingsCategoriesAggregationLiveResultInfo from a dict
business_data_business_listings_categories_aggregation_live_result_info_from_dict = BusinessDataBusinessListingsCategoriesAggregationLiveResultInfo.from_dict(business_data_business_listings_categories_aggregation_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


