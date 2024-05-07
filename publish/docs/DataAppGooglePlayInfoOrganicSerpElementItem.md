# DataAppGooglePlayInfoOrganicSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank among all the listed apps absolute position among all apps on the list | [optional] 
**position** | **str** | the alignment of the element in SERP can take the following values: left | [optional] 
**app_id** | **str** | ID of the app | [optional] 
**title** | **str** | title of the app | [optional] 
**url** | **str** | URL to the app page on Google Play | [optional] 
**icon** | **str** | URL to the app icon | [optional] 
**description** | **str** | description of the app | [optional] 
**reviews_count** | **int** | the total number of reviews the app has | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 
**price** | [**PriceInfo**](PriceInfo.md) |  | [optional] 
**is_free** | **bool** | indicates whether the app is free | [optional] 
**main_category** | **str** | main category of the app | [optional] 
**installs** | **str** | number of installs of the app approximate number of installs as displayed on the app page | [optional] 
**installs_count** | **int** | number of installs of the app the exact number of installs of the app | [optional] 
**developer** | **str** | name of the app developer | [optional] 
**developer_id** | **str** | ID of the app developer | [optional] 
**developer_url** | **str** | URL to the developer page on Google Play | [optional] 
**developer_email** | **str** | email address of the developer | [optional] 
**developer_address** | **str** | physical address of the developer | [optional] 
**developer_website** | **str** | official website of the developer | [optional] 
**version** | **str** | current version of the app | [optional] 
**minimum_os_version** | **str** | minimum OS version required to install the app | [optional] 
**size** | **str** | size of the app | [optional] 
**released_date** | **str** | date and time when the app was released in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”; example: 2019-11-15 12:57:46 +00:00 | [optional] 
**last_update_date** | **str** | date and time when the app was last updated in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”; example: 2019-11-15 12:57:46 +00:00 | [optional] 
**update_notes** | **str** | update notes contains the latest update notes from the developer | [optional] 
**images** | **List[Optional[str]]** | app images contains URLs to the images published on the app page on Google Play | [optional] 
**videos** | **List[Optional[str]]** | app videos contains URLs to the video published on the app page on Google Play | [optional] 
**similar_apps** | [**List[AppsInfo]**](AppsInfo.md) | similar apps displays apps similar to the app in a POST request | [optional] 
**more_apps_by_developer** | [**List[AppsInfo]**](AppsInfo.md) | similar apps information about apps built by the same developer | [optional] 
**genres** | **List[Optional[str]]** | app genres contains relevant app categories | [optional] 
**tags** | **List[Optional[str]]** | app tags contains relevant app tags | [optional] 

## Example

```python
from dataforseo_client.models.data_app_google_play_info_organic_serp_element_item import DataAppGooglePlayInfoOrganicSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataAppGooglePlayInfoOrganicSerpElementItem from a JSON string
data_app_google_play_info_organic_serp_element_item_instance = DataAppGooglePlayInfoOrganicSerpElementItem.from_json(json)
# print the JSON string representation of the object
print DataAppGooglePlayInfoOrganicSerpElementItem.to_json()

# convert the object into a dict
data_app_google_play_info_organic_serp_element_item_dict = data_app_google_play_info_organic_serp_element_item_instance.to_dict()
# create an instance of DataAppGooglePlayInfoOrganicSerpElementItem from a dict
data_app_google_play_info_organic_serp_element_item_form_dict = data_app_google_play_info_organic_serp_element_item.from_dict(data_app_google_play_info_organic_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


