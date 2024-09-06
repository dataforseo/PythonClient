# DataAppSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AppElement]**](AppElement.md) | contains arrays of specific images | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.data_app_serp_element_item import DataAppSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataAppSerpElementItem from a JSON string
data_app_serp_element_item_instance = DataAppSerpElementItem.from_json(json)
# print the JSON string representation of the object
print DataAppSerpElementItem.to_json()

# convert the object into a dict
data_app_serp_element_item_dict = data_app_serp_element_item_instance.to_dict()
# create an instance of DataAppSerpElementItem from a dict
data_app_serp_element_item_form_dict = data_app_serp_element_item.from_dict(data_app_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


