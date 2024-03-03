# ExploreBrandsElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of the row | [optional] 
**url** | **str** | URL | [optional] 
**domain** | **str** | domain where a link points | [optional] 
**description** | **str** | description of the results element in SERP | [optional] 
**image_url** | **str** | URL of the image | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 

## Example

```python
from dataforseo_client.models.explore_brands_element import ExploreBrandsElement

# TODO update the JSON string below
json = "{}"
# create an instance of ExploreBrandsElement from a JSON string
explore_brands_element_instance = ExploreBrandsElement.from_json(json)
# print the JSON string representation of the object
print ExploreBrandsElement.to_json()

# convert the object into a dict
explore_brands_element_dict = explore_brands_element_instance.to_dict()
# create an instance of ExploreBrandsElement from a dict
explore_brands_element_form_dict = explore_brands_element.from_dict(explore_brands_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


