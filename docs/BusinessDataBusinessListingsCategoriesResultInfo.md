# BusinessDataBusinessListingsCategoriesResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_name** | **str** | full name of the category | [optional] 
**business_count** | **int** | number of businesses in the category | [optional] 

## Example

```python
from dataforseo_client.models.business_data_business_listings_categories_result_info import BusinessDataBusinessListingsCategoriesResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataBusinessListingsCategoriesResultInfo from a JSON string
business_data_business_listings_categories_result_info_instance = BusinessDataBusinessListingsCategoriesResultInfo.from_json(json)
# print the JSON string representation of the object
print(BusinessDataBusinessListingsCategoriesResultInfo.to_json())

# convert the object into a dict
business_data_business_listings_categories_result_info_dict = business_data_business_listings_categories_result_info_instance.to_dict()
# create an instance of BusinessDataBusinessListingsCategoriesResultInfo from a dict
business_data_business_listings_categories_result_info_from_dict = BusinessDataBusinessListingsCategoriesResultInfo.from_dict(business_data_business_listings_categories_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


