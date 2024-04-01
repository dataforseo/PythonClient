# DataforseoLabsBBulkKeywordDifficultyLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**keyword** | **str** | keyword in a POST array | [optional] 
**keyword_difficulty** | **int** | difficulty of ranking in the first top-10 organic results for a keyword indicates the chance of getting in top-10 organic results for a keyword on a logarithmic scale from 0 to 100; calculated by analysing, among other parameters, link profiles of the first 10 pages in SERP; learn more about the metric in this help center guide | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_b_bulk_keyword_difficulty_live_item import DataforseoLabsBBulkKeywordDifficultyLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsBBulkKeywordDifficultyLiveItem from a JSON string
dataforseo_labs_b_bulk_keyword_difficulty_live_item_instance = DataforseoLabsBBulkKeywordDifficultyLiveItem.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsBBulkKeywordDifficultyLiveItem.to_json())

# convert the object into a dict
dataforseo_labs_b_bulk_keyword_difficulty_live_item_dict = dataforseo_labs_b_bulk_keyword_difficulty_live_item_instance.to_dict()
# create an instance of DataforseoLabsBBulkKeywordDifficultyLiveItem from a dict
dataforseo_labs_b_bulk_keyword_difficulty_live_item_form_dict = dataforseo_labs_b_bulk_keyword_difficulty_live_item.from_dict(dataforseo_labs_b_bulk_keyword_difficulty_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


