# RankedKeywordsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_from_keywords_count_top_3** | **int** | number of keywords for which the page is ranked in top 3 search results | [optional] 
**page_from_keywords_count_top_10** | **int** | number of keywords for which the page is ranked in top 10 search results | [optional] 
**page_from_keywords_count_top_100** | **int** | number of keywords for which the page is ranked in top 100 search results | [optional] 

## Example

```python
from dataforseo_client.models.ranked_keywords_info import RankedKeywordsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RankedKeywordsInfo from a JSON string
ranked_keywords_info_instance = RankedKeywordsInfo.from_json(json)
# print the JSON string representation of the object
print(RankedKeywordsInfo.to_json())

# convert the object into a dict
ranked_keywords_info_dict = ranked_keywords_info_instance.to_dict()
# create an instance of RankedKeywordsInfo from a dict
ranked_keywords_info_from_dict = RankedKeywordsInfo.from_dict(ranked_keywords_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


