# AppDataleAppListingsSearchLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | ID of the returned app | [optional] 
**se_domain** | **str** | search engine domain in a POST array | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**check_url** | **str** | direct URL to search engine results you can use it to make sure that we provided accurate results | [optional] 
**time_update** | **str** | date and time when SERP data was last updated in the ISO 8601 format: “YYYY-MM-DDThh:mm:ss.sssssssZ” example: 2023-05-23 10:16:19 +00:00 | [optional] 
**item** | [**BaseAppDataSerpElementItem**](BaseAppDataSerpElementItem.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.app_datale_app_listings_search_live_item import AppDataleAppListingsSearchLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of AppDataleAppListingsSearchLiveItem from a JSON string
app_datale_app_listings_search_live_item_instance = AppDataleAppListingsSearchLiveItem.from_json(json)
# print the JSON string representation of the object
print(AppDataleAppListingsSearchLiveItem.to_json())

# convert the object into a dict
app_datale_app_listings_search_live_item_dict = app_datale_app_listings_search_live_item_instance.to_dict()
# create an instance of AppDataleAppListingsSearchLiveItem from a dict
app_datale_app_listings_search_live_item_from_dict = AppDataleAppListingsSearchLiveItem.from_dict(app_datale_app_listings_search_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


