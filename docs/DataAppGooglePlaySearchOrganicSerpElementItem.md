# DataAppGooglePlaySearchOrganicSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | id of the app | [optional] 
**url** | **str** | URL to the app page on Google Play | [optional] 
**icon** | **str** | URL to the app icon | [optional] 
**reviews_count** | **int** | the total number of reviews of the app | [optional] 
**is_free** | **bool** | indicates whether the app is free | [optional] 
**price** | [**Price**](Price.md) |  | [optional] 
**developer** | **str** | name of the app developer | [optional] 
**developer_url** | **str** | URL to the developer page on Google Play | [optional] 

## Example

```python
from dataforseo_client.models.data_app_google_play_search_organic_serp_element_item import DataAppGooglePlaySearchOrganicSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataAppGooglePlaySearchOrganicSerpElementItem from a JSON string
data_app_google_play_search_organic_serp_element_item_instance = DataAppGooglePlaySearchOrganicSerpElementItem.from_json(json)
# print the JSON string representation of the object
print DataAppGooglePlaySearchOrganicSerpElementItem.to_json()

# convert the object into a dict
data_app_google_play_search_organic_serp_element_item_dict = data_app_google_play_search_organic_serp_element_item_instance.to_dict()
# create an instance of DataAppGooglePlaySearchOrganicSerpElementItem from a dict
data_app_google_play_search_organic_serp_element_item_form_dict = data_app_google_play_search_organic_serp_element_item.from_dict(data_app_google_play_search_organic_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


