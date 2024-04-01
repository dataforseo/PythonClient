# AmazonProductNewerModelInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | product title | [optional] 
**newer_model_asin** | **str** | ASIN of the newer product model | [optional] 

## Example

```python
from dataforseo_client.models.amazon_product_newer_model_info import AmazonProductNewerModelInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonProductNewerModelInfo from a JSON string
amazon_product_newer_model_info_instance = AmazonProductNewerModelInfo.from_json(json)
# print the JSON string representation of the object
print(AmazonProductNewerModelInfo.to_json())

# convert the object into a dict
amazon_product_newer_model_info_dict = amazon_product_newer_model_info_instance.to_dict()
# create an instance of AmazonProductNewerModelInfo from a dict
amazon_product_newer_model_info_form_dict = amazon_product_newer_model_info.from_dict(amazon_product_newer_model_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


