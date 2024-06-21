# DataforseoLabsRankedKeywordsLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**keyword_data** | [**KeywordDataKeywordDataInfo**](KeywordDataKeywordDataInfo.md) |  | [optional] 
**ranked_serp_element** | [**RankedSerpElement**](RankedSerpElement.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_ranked_keywords_live_item import DataforseoLabsRankedKeywordsLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsRankedKeywordsLiveItem from a JSON string
dataforseo_labs_ranked_keywords_live_item_instance = DataforseoLabsRankedKeywordsLiveItem.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsRankedKeywordsLiveItem.to_json()

# convert the object into a dict
dataforseo_labs_ranked_keywords_live_item_dict = dataforseo_labs_ranked_keywords_live_item_instance.to_dict()
# create an instance of DataforseoLabsRankedKeywordsLiveItem from a dict
dataforseo_labs_ranked_keywords_live_item_form_dict = dataforseo_labs_ranked_keywords_live_item.from_dict(dataforseo_labs_ranked_keywords_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


