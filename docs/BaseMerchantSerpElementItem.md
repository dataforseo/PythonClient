# BaseMerchantSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements found in Google Shopping SERP | [optional] 
**position** | **str** | alignment of the element in SERP can take the following values: left, right | [optional] 

## Example

```python
from dataforseo_client.models.base_merchant_serp_element_item import BaseMerchantSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of BaseMerchantSerpElementItem from a JSON string
base_merchant_serp_element_item_instance = BaseMerchantSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(BaseMerchantSerpElementItem.to_json())

# convert the object into a dict
base_merchant_serp_element_item_dict = base_merchant_serp_element_item_instance.to_dict()
# create an instance of BaseMerchantSerpElementItem from a dict
base_merchant_serp_element_item_from_dict = BaseMerchantSerpElementItem.from_dict(base_merchant_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


