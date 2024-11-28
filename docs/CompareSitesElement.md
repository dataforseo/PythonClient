# CompareSitesElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of a given link element | [optional] 
**url** | **str** | URL | [optional] 
**domain** | **str** | website domain | [optional] 
**image_url** | **str** | URL of the image the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available) | [optional] 
**source** | **str** | source of the element indicates the source of information included in the top_stories_element | [optional] 

## Example

```python
from dataforseo_client.models.compare_sites_element import CompareSitesElement

# TODO update the JSON string below
json = "{}"
# create an instance of CompareSitesElement from a JSON string
compare_sites_element_instance = CompareSitesElement.from_json(json)
# print the JSON string representation of the object
print(CompareSitesElement.to_json())

# convert the object into a dict
compare_sites_element_dict = compare_sites_element_instance.to_dict()
# create an instance of CompareSitesElement from a dict
compare_sites_element_from_dict = CompareSitesElement.from_dict(compare_sites_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


