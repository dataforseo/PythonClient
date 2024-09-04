# TrustpilotSearchOrganicBusinessDataSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the establishment | [optional] 
**domain** | **str** | domain of the establishment | [optional] 
**url** | **str** | URL to the establishment | [optional] 
**reviews_count** | **int** | the total number of reviews | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.trustpilot_search_organic_business_data_serp_element_item import TrustpilotSearchOrganicBusinessDataSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of TrustpilotSearchOrganicBusinessDataSerpElementItem from a JSON string
trustpilot_search_organic_business_data_serp_element_item_instance = TrustpilotSearchOrganicBusinessDataSerpElementItem.from_json(json)
# print the JSON string representation of the object
print TrustpilotSearchOrganicBusinessDataSerpElementItem.to_json()

# convert the object into a dict
trustpilot_search_organic_business_data_serp_element_item_dict = trustpilot_search_organic_business_data_serp_element_item_instance.to_dict()
# create an instance of TrustpilotSearchOrganicBusinessDataSerpElementItem from a dict
trustpilot_search_organic_business_data_serp_element_item_form_dict = trustpilot_search_organic_business_data_serp_element_item.from_dict(trustpilot_search_organic_business_data_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


