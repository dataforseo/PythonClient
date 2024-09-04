# ShoppingSpecificationMerchantSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**xpath** | **str** | XPath of the element | [optional] 
**block_name** | **str** | name of the block of product attributes indicates the name of the product specification section in which the related element is listed | [optional] 
**specification_name** | **str** | product attribute attribute name of the product data specification | [optional] 
**specification_value** | **str** | content of the specification | [optional] 

## Example

```python
from dataforseo_client.models.shopping_specification_merchant_serp_element_item import ShoppingSpecificationMerchantSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of ShoppingSpecificationMerchantSerpElementItem from a JSON string
shopping_specification_merchant_serp_element_item_instance = ShoppingSpecificationMerchantSerpElementItem.from_json(json)
# print the JSON string representation of the object
print ShoppingSpecificationMerchantSerpElementItem.to_json()

# convert the object into a dict
shopping_specification_merchant_serp_element_item_dict = shopping_specification_merchant_serp_element_item_instance.to_dict()
# create an instance of ShoppingSpecificationMerchantSerpElementItem from a dict
shopping_specification_merchant_serp_element_item_form_dict = shopping_specification_merchant_serp_element_item.from_dict(shopping_specification_merchant_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


