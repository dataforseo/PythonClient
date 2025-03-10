# DictionarySerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**title** | **str** | title of the result in SERP | [optional] 
**url** | **str** | relevant URL of the Ad element in SERP | [optional] 
**domain** | **str** | domain in SERP | [optional] 
**breadcrumb** | **str** | breadcrumb of the Ad element in SERP | [optional] 
**keyword** | **str** | keyword highlighted in the result | [optional] 
**snippet** | **str** | snippet of the element | [optional] 
**text** | **str** | description of the results element in SERP | [optional] 
**links** | [**List[LinkElement]**](LinkElement.md) | sitelinks the links shown below some of search results if there are none, equals null | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.dictionary_serp_element_item import DictionarySerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of DictionarySerpElementItem from a JSON string
dictionary_serp_element_item_instance = DictionarySerpElementItem.from_json(json)
# print the JSON string representation of the object
print(DictionarySerpElementItem.to_json())

# convert the object into a dict
dictionary_serp_element_item_dict = dictionary_serp_element_item_instance.to_dict()
# create an instance of DictionarySerpElementItem from a dict
dictionary_serp_element_item_from_dict = DictionarySerpElementItem.from_dict(dictionary_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


