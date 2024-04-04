# ProductVariation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**product_id** | **str** | product ID in a POST array learn more about the parameter in this help center guide | [optional] 
**title** | **str** | name of the product seller | [optional] 
**url** | **str** | seller url url of the webpage on the seller’s website where the product is sold | [optional] 

## Example

```python
from dataforseo_client.models.product_variation import ProductVariation

# TODO update the JSON string below
json = "{}"
# create an instance of ProductVariation from a JSON string
product_variation_instance = ProductVariation.from_json(json)
# print the JSON string representation of the object
print ProductVariation.to_json()

# convert the object into a dict
product_variation_dict = product_variation_instance.to_dict()
# create an instance of ProductVariation from a dict
product_variation_form_dict = product_variation.from_dict(product_variation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


