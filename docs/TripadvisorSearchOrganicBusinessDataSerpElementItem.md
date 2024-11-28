# TripadvisorSearchOrganicBusinessDataSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | name of the business entity | [optional] 
**url_path** | **str** | URL path of the business entity URL path to the Tripadvisor page of the business entity you can use this identifier to collect reviews for the business entity using Tripadvisor Reviews | [optional] 
**is_sponsored** | **bool** | indicates a sponsored placement if true, related tripadvisor_search_organic item is a paid advertising on Tripadvisor | [optional] 
**reviews_count** | **int** | the total number of reviews | [optional] 
**category** | **str** | place category | [optional] 
**price_rate** | **str** | average price rate | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.tripadvisor_search_organic_business_data_serp_element_item import TripadvisorSearchOrganicBusinessDataSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of TripadvisorSearchOrganicBusinessDataSerpElementItem from a JSON string
tripadvisor_search_organic_business_data_serp_element_item_instance = TripadvisorSearchOrganicBusinessDataSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(TripadvisorSearchOrganicBusinessDataSerpElementItem.to_json())

# convert the object into a dict
tripadvisor_search_organic_business_data_serp_element_item_dict = tripadvisor_search_organic_business_data_serp_element_item_instance.to_dict()
# create an instance of TripadvisorSearchOrganicBusinessDataSerpElementItem from a dict
tripadvisor_search_organic_business_data_serp_element_item_from_dict = TripadvisorSearchOrganicBusinessDataSerpElementItem.from_dict(tripadvisor_search_organic_business_data_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


