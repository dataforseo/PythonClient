# GoogleTrendsQueriesListElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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


