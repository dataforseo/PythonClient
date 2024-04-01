# ProductCategoryInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | product category name | [optional] 
**url** | **str** | product category URL indicates the browse path on Amazon with the unique browse node ID (product category ID on Amazon) | [optional] 

## Example

```python
from dataforseo_client.models.product_category_info import ProductCategoryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCategoryInfo from a JSON string
product_category_info_instance = ProductCategoryInfo.from_json(json)
# print the JSON string representation of the object
print(ProductCategoryInfo.to_json())

# convert the object into a dict
product_category_info_dict = product_category_info_instance.to_dict()
# create an instance of ProductCategoryInfo from a dict
product_category_info_form_dict = product_category_info.from_dict(product_category_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


