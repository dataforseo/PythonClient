# BaseAmazonSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in Amazon SERP absolute position among all the elements in SERP | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 

## Example

```python
from dataforseo_client.models.base_amazon_serp_element_item import BaseAmazonSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of BaseAmazonSerpElementItem from a JSON string
base_amazon_serp_element_item_instance = BaseAmazonSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(BaseAmazonSerpElementItem.to_json())

# convert the object into a dict
base_amazon_serp_element_item_dict = base_amazon_serp_element_item_instance.to_dict()
# create an instance of BaseAmazonSerpElementItem from a dict
base_amazon_serp_element_item_from_dict = BaseAmazonSerpElementItem.from_dict(base_amazon_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


