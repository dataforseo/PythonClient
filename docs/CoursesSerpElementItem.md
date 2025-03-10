# CoursesSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**title** | **str** | title of the row | [optional] 
**categories** | **List[Optional[str]]** | array of course categories contains a list of categories relevant to courses | [optional] 
**items** | [**List[CoursesElement]**](CoursesElement.md) | contains arrays of specific images | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.courses_serp_element_item import CoursesSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of CoursesSerpElementItem from a JSON string
courses_serp_element_item_instance = CoursesSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(CoursesSerpElementItem.to_json())

# convert the object into a dict
courses_serp_element_item_dict = courses_serp_element_item_instance.to_dict()
# create an instance of CoursesSerpElementItem from a dict
courses_serp_element_item_from_dict = CoursesSerpElementItem.from_dict(courses_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


