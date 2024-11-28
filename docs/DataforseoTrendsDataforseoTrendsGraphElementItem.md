# DataforseoTrendsDataforseoTrendsGraphElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TrendsGraphDataInfo]**](TrendsGraphDataInfo.md) | DataForSEO Trends data for the specified parameters | [optional] 
**averages** | **List[Optional[int]]** | keyword popularity values averaged over the whole time range | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_trends_dataforseo_trends_graph_element_item import DataforseoTrendsDataforseoTrendsGraphElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoTrendsDataforseoTrendsGraphElementItem from a JSON string
dataforseo_trends_dataforseo_trends_graph_element_item_instance = DataforseoTrendsDataforseoTrendsGraphElementItem.from_json(json)
# print the JSON string representation of the object
print(DataforseoTrendsDataforseoTrendsGraphElementItem.to_json())

# convert the object into a dict
dataforseo_trends_dataforseo_trends_graph_element_item_dict = dataforseo_trends_dataforseo_trends_graph_element_item_instance.to_dict()
# create an instance of DataforseoTrendsDataforseoTrendsGraphElementItem from a dict
dataforseo_trends_dataforseo_trends_graph_element_item_from_dict = DataforseoTrendsDataforseoTrendsGraphElementItem.from_dict(dataforseo_trends_dataforseo_trends_graph_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


