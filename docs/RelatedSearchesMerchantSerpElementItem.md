# RelatedSearchesMerchantSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**xpath** | **str** | XPath of the element | [optional] 
**items** | **List[Optional[str]]** | additional items present in the element if there are none, equals null | [optional] 

## Example

```python
from dataforseo_client.models.related_searches_merchant_serp_element_item import RelatedSearchesMerchantSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedSearchesMerchantSerpElementItem from a JSON string
related_searches_merchant_serp_element_item_instance = RelatedSearchesMerchantSerpElementItem.from_json(json)
# print the JSON string representation of the object
print RelatedSearchesMerchantSerpElementItem.to_json()

# convert the object into a dict
related_searches_merchant_serp_element_item_dict = related_searches_merchant_serp_element_item_instance.to_dict()
# create an instance of RelatedSearchesMerchantSerpElementItem from a dict
related_searches_merchant_serp_element_item_form_dict = related_searches_merchant_serp_element_item.from_dict(related_searches_merchant_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


