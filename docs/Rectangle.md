# Rectangle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **float** | x-axis coordinate x-axis coordinate of the top-left corner of the result’s snippet, where top-left corner of the screen is the origin | [optional] 
**y** | **float** | y-axis coordinate y-axis coordinate of the top-left corner of the result’s snippet, where top-left corner of the screen is the origin | [optional] 
**width** | **float** | width of the element in pixels | [optional] 
**height** | **float** | height of the element in pixels | [optional] 

## Example

```python
from dataforseo_client.models.rectangle import Rectangle

# TODO update the JSON string below
json = "{}"
# create an instance of Rectangle from a JSON string
rectangle_instance = Rectangle.from_json(json)
# print the JSON string representation of the object
print(Rectangle.to_json())

# convert the object into a dict
rectangle_dict = rectangle_instance.to_dict()
# create an instance of Rectangle from a dict
rectangle_form_dict = rectangle.from_dict(rectangle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


