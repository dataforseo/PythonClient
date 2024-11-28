# CoursesElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of a given link element | [optional] 
**url** | **str** | URL | [optional] 
**domain** | **str** | website domain | [optional] 
**source** | **str** | source of the element indicates the source of information included in the top_stories_element | [optional] 
**description** | **str** | description | [optional] 
**var_date** | **str** | the date when the page source of the element was published | [optional] 
**image_url** | **str** | URL of the image the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available) | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.courses_element import CoursesElement

# TODO update the JSON string below
json = "{}"
# create an instance of CoursesElement from a JSON string
courses_element_instance = CoursesElement.from_json(json)
# print the JSON string representation of the object
print(CoursesElement.to_json())

# convert the object into a dict
courses_element_dict = courses_element_instance.to_dict()
# create an instance of CoursesElement from a dict
courses_element_from_dict = CoursesElement.from_dict(courses_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


