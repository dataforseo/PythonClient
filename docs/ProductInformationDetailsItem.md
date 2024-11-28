# ProductInformationDetailsItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **Dict[str, Optional[str]]** | contains information specified about the product within the section_name | [optional] 

## Example

```python
from dataforseo_client.models.product_information_details_item import ProductInformationDetailsItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProductInformationDetailsItem from a JSON string
product_information_details_item_instance = ProductInformationDetailsItem.from_json(json)
# print the JSON string representation of the object
print(ProductInformationDetailsItem.to_json())

# convert the object into a dict
product_information_details_item_dict = product_information_details_item_instance.to_dict()
# create an instance of ProductInformationDetailsItem from a dict
product_information_details_item_from_dict = ProductInformationDetailsItem.from_dict(product_information_details_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


