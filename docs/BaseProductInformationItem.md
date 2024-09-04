# BaseProductInformationItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**section_name** | **str** | name of the section related to product information specified in the contents | [optional] 

## Example

```python
from dataforseo_client.models.base_product_information_item import BaseProductInformationItem

# TODO update the JSON string below
json = "{}"
# create an instance of BaseProductInformationItem from a JSON string
base_product_information_item_instance = BaseProductInformationItem.from_json(json)
# print the JSON string representation of the object
print BaseProductInformationItem.to_json()

# convert the object into a dict
base_product_information_item_dict = base_product_information_item_instance.to_dict()
# create an instance of BaseProductInformationItem from a dict
base_product_information_item_form_dict = base_product_information_item.from_dict(base_product_information_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


