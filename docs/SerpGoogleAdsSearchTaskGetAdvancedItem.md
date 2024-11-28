# SerpGoogleAdsSearchTaskGetAdvancedItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional] 
**advertiser_id** | **str** | unique identifier of the advertiser account | [optional] 
**creative_id** | **str** | unique identifier of the advertisement | [optional] 
**title** | **str** | title of the element | [optional] 
**url** | **str** | search URL with refinement parameters | [optional] 
**verified** | **bool** | verified advertiser account equals true if advertiser account is verified by Google Ads | [optional] 
**format** | **str** | format of the advertisement possible values: text, image, video | [optional] 
**preview_image** | [**PreviewImage**](PreviewImage.md) |  | [optional] 
**preview_url** | **str** | url pointing to the ad preview | [optional] 
**first_shown** | **str** | date and time when the ad was shown for the first time in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” | [optional] 
**last_shown** | **str** | date and time when the ad was shown the last time in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” | [optional] 

## Example

```python
from dataforseo_client.models.serp_google_ads_search_task_get_advanced_item import SerpGoogleAdsSearchTaskGetAdvancedItem

# TODO update the JSON string below
json = "{}"
# create an instance of SerpGoogleAdsSearchTaskGetAdvancedItem from a JSON string
serp_google_ads_search_task_get_advanced_item_instance = SerpGoogleAdsSearchTaskGetAdvancedItem.from_json(json)
# print the JSON string representation of the object
print(SerpGoogleAdsSearchTaskGetAdvancedItem.to_json())

# convert the object into a dict
serp_google_ads_search_task_get_advanced_item_dict = serp_google_ads_search_task_get_advanced_item_instance.to_dict()
# create an instance of SerpGoogleAdsSearchTaskGetAdvancedItem from a dict
serp_google_ads_search_task_get_advanced_item_from_dict = SerpGoogleAdsSearchTaskGetAdvancedItem.from_dict(serp_google_ads_search_task_get_advanced_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


