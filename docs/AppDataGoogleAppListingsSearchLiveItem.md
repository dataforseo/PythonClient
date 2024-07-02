# AppDataGoogleAppListingsSearchLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | ID of the returned app | [optional] 
**se_domain** | **str** | search engine domain in a POST array | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**check_url** | **str** | direct URL to search engine results you can use it to make sure that we provided accurate results | [optional] 
**time_update** | **str** | date and time when SERP data was last updated in the ISO 8601 format: “YYYY-MM-DDThh:mm:ss.sssssssZ” example: 2023-05-23 10:16:19 +00:00 | [optional] 
**item** | [**DataAppGooglePlayInfoOrganicSerpElementItem**](DataAppGooglePlayInfoOrganicSerpElementItem.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.app_data_google_app_listings_search_live_item import AppDataGoogleAppListingsSearchLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of AppDataGoogleAppListingsSearchLiveItem from a JSON string
app_data_google_app_listings_search_live_item_instance = AppDataGoogleAppListingsSearchLiveItem.from_json(json)
# print the JSON string representation of the object
print AppDataGoogleAppListingsSearchLiveItem.to_json()

# convert the object into a dict
app_data_google_app_listings_search_live_item_dict = app_data_google_app_listings_search_live_item_instance.to_dict()
# create an instance of AppDataGoogleAppListingsSearchLiveItem from a dict
app_data_google_app_listings_search_live_item_form_dict = app_data_google_app_listings_search_live_item.from_dict(app_data_google_app_listings_search_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


