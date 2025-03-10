# NewsSearchSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional] 
**domain** | **str** | domain in SERP | [optional] 
**url** | **str** | search URL with refinement parameters | [optional] 
**image_url** | **str** | URL of the image the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available) | [optional] 
**snippet** | **str** | snippet of the result in SERP | [optional] 
**time_published** | **str** | indicates the time the result was published | [optional] 
**timestamp** | **str** | date and time when the news was published in the format “year-month-date:minutes:UTC_difference_hours:UTC_difference_minutes” example: 2019-11-15 12:57:46 +00:00 | [optional] 

## Example

```python
from dataforseo_client.models.news_search_serp_element_item import NewsSearchSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of NewsSearchSerpElementItem from a JSON string
news_search_serp_element_item_instance = NewsSearchSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(NewsSearchSerpElementItem.to_json())

# convert the object into a dict
news_search_serp_element_item_dict = news_search_serp_element_item_instance.to_dict()
# create an instance of NewsSearchSerpElementItem from a dict
news_search_serp_element_item_from_dict = NewsSearchSerpElementItem.from_dict(news_search_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


