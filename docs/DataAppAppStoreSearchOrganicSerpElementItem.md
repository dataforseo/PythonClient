# DataAppAppStoreSearchOrganicSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional] 
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**app_id** | **str** | id of the app | [optional] 
**title** | **str** | title of the app | [optional] 
**url** | **str** | URL to the app page on App Store | [optional] 
**icon** | **str** | URL to the app icon | [optional] 
**reviews_count** | **int** | the total number of reviews of the app | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 
**is_free** | **bool** | indicates whether the app is free | [optional] 
**price** | [**Price**](Price.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.data_app_app_store_search_organic_serp_element_item import DataAppAppStoreSearchOrganicSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataAppAppStoreSearchOrganicSerpElementItem from a JSON string
data_app_app_store_search_organic_serp_element_item_instance = DataAppAppStoreSearchOrganicSerpElementItem.from_json(json)
# print the JSON string representation of the object
print DataAppAppStoreSearchOrganicSerpElementItem.to_json()

# convert the object into a dict
data_app_app_store_search_organic_serp_element_item_dict = data_app_app_store_search_organic_serp_element_item_instance.to_dict()
# create an instance of DataAppAppStoreSearchOrganicSerpElementItem from a dict
data_app_app_store_search_organic_serp_element_item_form_dict = data_app_app_store_search_organic_serp_element_item.from_dict(data_app_app_store_search_organic_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


