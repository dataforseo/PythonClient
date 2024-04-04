# GoogleTrendsQueriesListElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **int** | the alignment of the element in Google Trends can take the following values: 1, 2, 3, 4, etc. | [optional] 
**title** | **str** | title of the element in Google Trends | [optional] 
**keywords** | **List[Optional[str]]** | relevant keywords the data included in the google_trends_topics_list element is based on the keywords listed in this array | [optional] 
**data** | [**QueriesListDataInfo**](QueriesListDataInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.google_trends_queries_list_element_item import GoogleTrendsQueriesListElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleTrendsQueriesListElementItem from a JSON string
google_trends_queries_list_element_item_instance = GoogleTrendsQueriesListElementItem.from_json(json)
# print the JSON string representation of the object
print GoogleTrendsQueriesListElementItem.to_json()

# convert the object into a dict
google_trends_queries_list_element_item_dict = google_trends_queries_list_element_item_instance.to_dict()
# create an instance of GoogleTrendsQueriesListElementItem from a dict
google_trends_queries_list_element_item_form_dict = google_trends_queries_list_element_item.from_dict(google_trends_queries_list_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


