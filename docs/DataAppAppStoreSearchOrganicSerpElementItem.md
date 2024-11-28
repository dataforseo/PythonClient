# DataAppAppStoreSearchOrganicSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | id of the app | [optional] 
**url** | **str** | URL to the app page on App Store | [optional] 
**icon** | **str** | URL to the app icon | [optional] 
**reviews_count** | **int** | the total number of reviews of the app | [optional] 
**is_free** | **bool** | indicates whether the app is free | [optional] 
**price** | [**PriceInfo**](PriceInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.data_app_app_store_search_organic_serp_element_item import DataAppAppStoreSearchOrganicSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataAppAppStoreSearchOrganicSerpElementItem from a JSON string
data_app_app_store_search_organic_serp_element_item_instance = DataAppAppStoreSearchOrganicSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(DataAppAppStoreSearchOrganicSerpElementItem.to_json())

# convert the object into a dict
data_app_app_store_search_organic_serp_element_item_dict = data_app_app_store_search_organic_serp_element_item_instance.to_dict()
# create an instance of DataAppAppStoreSearchOrganicSerpElementItem from a dict
data_app_app_store_search_organic_serp_element_item_from_dict = DataAppAppStoreSearchOrganicSerpElementItem.from_dict(data_app_app_store_search_organic_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


