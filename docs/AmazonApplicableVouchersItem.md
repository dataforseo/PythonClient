# AmazonApplicableVouchersItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**text** | **str** | text of the voucher | [optional] 
**fixed_discount** | **float** | value of the fixed discount | [optional] 
**fixed_discount_currency** | **str** | currency code of the fixed discount | [optional] 
**percentage_discount** | **float** | value of the percentage discount if the discount is fixed, the value will be null | [optional] 
**important_details** | **str** | important details about the terms of discount vouchers | [optional] 

## Example

```python
from dataforseo_client.models.amazon_applicable_vouchers_item import AmazonApplicableVouchersItem

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonApplicableVouchersItem from a JSON string
amazon_applicable_vouchers_item_instance = AmazonApplicableVouchersItem.from_json(json)
# print the JSON string representation of the object
print(AmazonApplicableVouchersItem.to_json())

# convert the object into a dict
amazon_applicable_vouchers_item_dict = amazon_applicable_vouchers_item_instance.to_dict()
# create an instance of AmazonApplicableVouchersItem from a dict
amazon_applicable_vouchers_item_from_dict = AmazonApplicableVouchersItem.from_dict(amazon_applicable_vouchers_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


