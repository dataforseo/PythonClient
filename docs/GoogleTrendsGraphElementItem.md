# GoogleTrendsGraphElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TrendsGraphDataInfo]**](TrendsGraphDataInfo.md) | Google Trends data for the specified parameters | [optional] 
**averages** | **List[Optional[float]]** | keyword popularity values averaged over the whole time range | [optional] 

## Example

```python
from dataforseo_client.models.google_trends_graph_element_item import GoogleTrendsGraphElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleTrendsGraphElementItem from a JSON string
google_trends_graph_element_item_instance = GoogleTrendsGraphElementItem.from_json(json)
# print the JSON string representation of the object
print GoogleTrendsGraphElementItem.to_json()

# convert the object into a dict
google_trends_graph_element_item_dict = google_trends_graph_element_item_instance.to_dict()
# create an instance of GoogleTrendsGraphElementItem from a dict
google_trends_graph_element_item_form_dict = google_trends_graph_element_item.from_dict(google_trends_graph_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


