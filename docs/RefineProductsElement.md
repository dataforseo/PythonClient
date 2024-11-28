# RefineProductsElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of a given link element | [optional] 
**image_url** | **str** | URL of the image the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available) | [optional] 
**keyword** | **str** | keyword for the related refined search | [optional] 
**refine_type** | **str** | type of search refinement | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 

## Example

```python
from dataforseo_client.models.refine_products_element import RefineProductsElement

# TODO update the JSON string below
json = "{}"
# create an instance of RefineProductsElement from a JSON string
refine_products_element_instance = RefineProductsElement.from_json(json)
# print the JSON string representation of the object
print(RefineProductsElement.to_json())

# convert the object into a dict
refine_products_element_dict = refine_products_element_instance.to_dict()
# create an instance of RefineProductsElement from a dict
refine_products_element_from_dict = RefineProductsElement.from_dict(refine_products_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


