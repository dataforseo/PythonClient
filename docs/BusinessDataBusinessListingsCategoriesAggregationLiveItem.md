# BusinessDataBusinessListingsCategoriesAggregationLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**categories** | **List[Optional[str]]** | business categories Google My Business general category that best describes the cluster of related categories | [optional] 
**aggregation** | [**BusinessListingAggregationInfo**](BusinessListingAggregationInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.business_data_business_listings_categories_aggregation_live_item import BusinessDataBusinessListingsCategoriesAggregationLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataBusinessListingsCategoriesAggregationLiveItem from a JSON string
business_data_business_listings_categories_aggregation_live_item_instance = BusinessDataBusinessListingsCategoriesAggregationLiveItem.from_json(json)
# print the JSON string representation of the object
print(BusinessDataBusinessListingsCategoriesAggregationLiveItem.to_json())

# convert the object into a dict
business_data_business_listings_categories_aggregation_live_item_dict = business_data_business_listings_categories_aggregation_live_item_instance.to_dict()
# create an instance of BusinessDataBusinessListingsCategoriesAggregationLiveItem from a dict
business_data_business_listings_categories_aggregation_live_item_from_dict = BusinessDataBusinessListingsCategoriesAggregationLiveItem.from_dict(business_data_business_listings_categories_aggregation_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


