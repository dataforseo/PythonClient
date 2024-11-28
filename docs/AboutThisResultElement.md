# AboutThisResultElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**url** | **str** | result’s URL | [optional] 
**source** | **str** | source of additional information about the result | [optional] 
**source_info** | **str** | additional information about the result description of the website from Wikipedia or another additional context | [optional] 
**source_url** | **str** | URL to full information from the &#39;source&#39; | [optional] 
**language** | **str** | the language of the result | [optional] 
**location** | **str** | location for which the result is relevant | [optional] 
**search_terms** | **List[Optional[str]]** | matching search terms that appear in the result | [optional] 
**related_terms** | **List[Optional[str]]** | related search terms that appear in the result | [optional] 

## Example

```python
from dataforseo_client.models.about_this_result_element import AboutThisResultElement

# TODO update the JSON string below
json = "{}"
# create an instance of AboutThisResultElement from a JSON string
about_this_result_element_instance = AboutThisResultElement.from_json(json)
# print the JSON string representation of the object
print(AboutThisResultElement.to_json())

# convert the object into a dict
about_this_result_element_dict = about_this_result_element_instance.to_dict()
# create an instance of AboutThisResultElement from a dict
about_this_result_element_from_dict = AboutThisResultElement.from_dict(about_this_result_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


