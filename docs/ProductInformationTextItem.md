# ProductInformationTextItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**section_name** | **str** | name of the section related to product information specified in the contents | [optional] 
**text** | **str** | text specified under the given title within the section_name | [optional] 

## Example

```python
from dataforseo_client.models.product_information_text_item import ProductInformationTextItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProductInformationTextItem from a JSON string
product_information_text_item_instance = ProductInformationTextItem.from_json(json)
# print the JSON string representation of the object
print ProductInformationTextItem.to_json()

# convert the object into a dict
product_information_text_item_dict = product_information_text_item_instance.to_dict()
# create an instance of ProductInformationTextItem from a dict
product_information_text_item_form_dict = product_information_text_item.from_dict(product_information_text_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


