# BaseGoogleTrendsItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**position** | **int** | the alignment of the element in Google Trends can take the following values: 1, 2, 3, 4, etc. | [optional] 
**title** | **str** | title of the element in Google Trends | [optional] 
**keywords** | **List[Optional[str]]** | relevant keywords the data included in the google_trends_graph element is based on the keywords listed in this array | [optional] 

## Example

```python
from dataforseo_client.models.base_google_trends_item import BaseGoogleTrendsItem

# TODO update the JSON string below
json = "{}"
# create an instance of BaseGoogleTrendsItem from a JSON string
base_google_trends_item_instance = BaseGoogleTrendsItem.from_json(json)
# print the JSON string representation of the object
print BaseGoogleTrendsItem.to_json()

# convert the object into a dict
base_google_trends_item_dict = base_google_trends_item_instance.to_dict()
# create an instance of BaseGoogleTrendsItem from a dict
base_google_trends_item_form_dict = base_google_trends_item.from_dict(base_google_trends_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


