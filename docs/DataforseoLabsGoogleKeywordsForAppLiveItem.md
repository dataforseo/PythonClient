# DataforseoLabsGoogleKeywordsForAppLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**keyword_data** | [**KeywordDataInfo**](KeywordDataInfo.md) |  | [optional] 
**ranked_serp_element** | [**AppRankedSerpElementInfo**](AppRankedSerpElementInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_keywords_for_app_live_item import DataforseoLabsGoogleKeywordsForAppLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleKeywordsForAppLiveItem from a JSON string
dataforseo_labs_google_keywords_for_app_live_item_instance = DataforseoLabsGoogleKeywordsForAppLiveItem.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsGoogleKeywordsForAppLiveItem.to_json())

# convert the object into a dict
dataforseo_labs_google_keywords_for_app_live_item_dict = dataforseo_labs_google_keywords_for_app_live_item_instance.to_dict()
# create an instance of DataforseoLabsGoogleKeywordsForAppLiveItem from a dict
dataforseo_labs_google_keywords_for_app_live_item_from_dict = DataforseoLabsGoogleKeywordsForAppLiveItem.from_dict(dataforseo_labs_google_keywords_for_app_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


