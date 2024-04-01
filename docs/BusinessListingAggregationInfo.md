# BusinessListingAggregationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top_categories** | **Dict[str, Optional[int]]** | the most mentioned related categories top categories displayed with the number of businesses in each category | [optional] 
**top_countries** | **Dict[str, Optional[int]]** | the most mentioned counties country codes with the biggest number of businesses in the category | [optional] 
**websites_count** | **int** | number of unique websites | [optional] 
**count** | **int** | number of unique entities | [optional] 
**top_attributes** | **Dict[str, Optional[int]]** | the most mentioned service details service details of a business entity displayed in a form of checks and the number of entities mentioning each attribute | [optional] 
**top_place_topics** | **Dict[str, Optional[int]]** | top keywords mentioned in customer reviews contains most popular keywords related to products/services mentioned in customer reviews of a business entity and the number of reviews mentioning each keyword | [optional] 

## Example

```python
from dataforseo_client.models.business_listing_aggregation_info import BusinessListingAggregationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessListingAggregationInfo from a JSON string
business_listing_aggregation_info_instance = BusinessListingAggregationInfo.from_json(json)
# print the JSON string representation of the object
print(BusinessListingAggregationInfo.to_json())

# convert the object into a dict
business_listing_aggregation_info_dict = business_listing_aggregation_info_instance.to_dict()
# create an instance of BusinessListingAggregationInfo from a dict
business_listing_aggregation_info_form_dict = business_listing_aggregation_info.from_dict(business_listing_aggregation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


