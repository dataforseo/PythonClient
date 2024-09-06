# DataAmazonRelatedSearchesSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment of the element in Amazon SERP possible values: left, right | [optional] 
**items** | [**List[RelatedSearchesElement]**](RelatedSearchesElement.md) | Amazon product items | [optional] 

## Example

```python
from dataforseo_client.models.data_amazon_related_searches_serp_element_item import DataAmazonRelatedSearchesSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataAmazonRelatedSearchesSerpElementItem from a JSON string
data_amazon_related_searches_serp_element_item_instance = DataAmazonRelatedSearchesSerpElementItem.from_json(json)
# print the JSON string representation of the object
print DataAmazonRelatedSearchesSerpElementItem.to_json()

# convert the object into a dict
data_amazon_related_searches_serp_element_item_dict = data_amazon_related_searches_serp_element_item_instance.to_dict()
# create an instance of DataAmazonRelatedSearchesSerpElementItem from a dict
data_amazon_related_searches_serp_element_item_form_dict = data_amazon_related_searches_serp_element_item.from_dict(data_amazon_related_searches_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


