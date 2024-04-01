# ProductInformationRows


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title under which related product information appears on the Amazon product page | [optional] 
**rows** | [**List[BaseProductInformationRowItem]**](BaseProductInformationRowItem.md) | rows containing related product information | [optional] 

## Example

```python
from dataforseo_client.models.product_information_rows import ProductInformationRows

# TODO update the JSON string below
json = "{}"
# create an instance of ProductInformationRows from a JSON string
product_information_rows_instance = ProductInformationRows.from_json(json)
# print the JSON string representation of the object
print(ProductInformationRows.to_json())

# convert the object into a dict
product_information_rows_dict = product_information_rows_instance.to_dict()
# create an instance of ProductInformationRows from a dict
product_information_rows_form_dict = product_information_rows.from_dict(product_information_rows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


