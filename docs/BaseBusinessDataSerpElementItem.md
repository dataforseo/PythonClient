# BaseBusinessDataSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from the rank_group | [optional] 
**rank_absolute** | **int** | absolute rank among all the elements | [optional] 

## Example

```python
from dataforseo_client.models.base_business_data_serp_element_item import BaseBusinessDataSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of BaseBusinessDataSerpElementItem from a JSON string
base_business_data_serp_element_item_instance = BaseBusinessDataSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(BaseBusinessDataSerpElementItem.to_json())

# convert the object into a dict
base_business_data_serp_element_item_dict = base_business_data_serp_element_item_instance.to_dict()
# create an instance of BaseBusinessDataSerpElementItem from a dict
base_business_data_serp_element_item_from_dict = BaseBusinessDataSerpElementItem.from_dict(base_business_data_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


