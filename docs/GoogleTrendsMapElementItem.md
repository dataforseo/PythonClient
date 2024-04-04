# GoogleTrendsMapElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **int** | the alignment of the element in Google Trends can take the following values: 1, 2, 3, 4, etc. | [optional] 
**title** | **str** | title of the element in Google Trends | [optional] 
**keywords** | **List[Optional[str]]** | relevant keywords the data included in the google_trends_map element is based on the keywords listed in this array | [optional] 
**data** | [**List[TrendsMapDataInfo]**](TrendsMapDataInfo.md) | Google Trends data from the corresponding item | [optional] 

## Example

```python
from dataforseo_client.models.google_trends_map_element_item import GoogleTrendsMapElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleTrendsMapElementItem from a JSON string
google_trends_map_element_item_instance = GoogleTrendsMapElementItem.from_json(json)
# print the JSON string representation of the object
print GoogleTrendsMapElementItem.to_json()

# convert the object into a dict
google_trends_map_element_item_dict = google_trends_map_element_item_instance.to_dict()
# create an instance of GoogleTrendsMapElementItem from a dict
google_trends_map_element_item_form_dict = google_trends_map_element_item.from_dict(google_trends_map_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


