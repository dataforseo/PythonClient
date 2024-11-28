# RelatedSearchesElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | product title | [optional] 
**url** | **str** | the URL of the product page | [optional] 
**image_alt** | **str** | the alt tag of the product image featured in the results | [optional] 
**image_url** | **str** | URL of the product image featured in the results | [optional] 

## Example

```python
from dataforseo_client.models.related_searches_element import RelatedSearchesElement

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedSearchesElement from a JSON string
related_searches_element_instance = RelatedSearchesElement.from_json(json)
# print the JSON string representation of the object
print(RelatedSearchesElement.to_json())

# convert the object into a dict
related_searches_element_dict = related_searches_element_instance.to_dict()
# create an instance of RelatedSearchesElement from a dict
related_searches_element_from_dict = RelatedSearchesElement.from_dict(related_searches_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


