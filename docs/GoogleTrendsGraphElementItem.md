[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# GoogleTrendsGraphElementItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **int** | the alignment of the element in Google Trends can take the following values: 1, 2, 3, 4, etc. | [optional]
**title** | **str** | title of the element in Google Trends | [optional]
**keywords** | **List[Optional[str]]** | relevant keywords the data included in the google_trends_graph element is based on the keywords listed in this array | [optional]
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

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")