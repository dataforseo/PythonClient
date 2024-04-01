# DataforseoLabsGoogleRelatedKeywordsLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**keyword_data** | [**KeywordDataInfo**](KeywordDataInfo.md) |  | [optional] 
**depth** | **int** | keyword search depth | [optional] 
**related_keywords** | **List[Optional[str]]** | list of related keywords represents the list of search queries which are related to the keyword returned in the array above | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_related_keywords_live_item import DataforseoLabsGoogleRelatedKeywordsLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleRelatedKeywordsLiveItem from a JSON string
dataforseo_labs_google_related_keywords_live_item_instance = DataforseoLabsGoogleRelatedKeywordsLiveItem.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsGoogleRelatedKeywordsLiveItem.to_json())

# convert the object into a dict
dataforseo_labs_google_related_keywords_live_item_dict = dataforseo_labs_google_related_keywords_live_item_instance.to_dict()
# create an instance of DataforseoLabsGoogleRelatedKeywordsLiveItem from a dict
dataforseo_labs_google_related_keywords_live_item_form_dict = dataforseo_labs_google_related_keywords_live_item.from_dict(dataforseo_labs_google_related_keywords_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


