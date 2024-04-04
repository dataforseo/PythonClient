# ProductInformationExtendedItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**section_name** | **str** | name of the section related to product information specified in the contents | [optional] 
**contents** | [**List[ProductInformationRows]**](ProductInformationRows.md) | contains information specified about the product within the section_name | [optional] 

## Example

```python
from dataforseo_client.models.product_information_extended_item import ProductInformationExtendedItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProductInformationExtendedItem from a JSON string
product_information_extended_item_instance = ProductInformationExtendedItem.from_json(json)
# print the JSON string representation of the object
print ProductInformationExtendedItem.to_json()

# convert the object into a dict
product_information_extended_item_dict = product_information_extended_item_instance.to_dict()
# create an instance of ProductInformationExtendedItem from a dict
product_information_extended_item_form_dict = product_information_extended_item.from_dict(product_information_extended_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


