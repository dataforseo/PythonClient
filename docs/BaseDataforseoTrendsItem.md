# BaseDataforseoTrendsItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**position** | **int** | the alignment of the element can take the following values: 1, 2, 3, 4, etc. | [optional] 
**keywords** | **List[Optional[str]]** | relevant keywords the data included in the dataforseo_trends_graph element is based on the keywords listed in this array | [optional] 

## Example

```python
from dataforseo_client.models.base_dataforseo_trends_item import BaseDataforseoTrendsItem

# TODO update the JSON string below
json = "{}"
# create an instance of BaseDataforseoTrendsItem from a JSON string
base_dataforseo_trends_item_instance = BaseDataforseoTrendsItem.from_json(json)
# print the JSON string representation of the object
print(BaseDataforseoTrendsItem.to_json())

# convert the object into a dict
base_dataforseo_trends_item_dict = base_dataforseo_trends_item_instance.to_dict()
# create an instance of BaseDataforseoTrendsItem from a dict
base_dataforseo_trends_item_from_dict = BaseDataforseoTrendsItem.from_dict(base_dataforseo_trends_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


