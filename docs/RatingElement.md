# RatingElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rating_type** | **str** | the type of rating here you can find the following elements: Max5, Percents, CustomMax | [optional] 
**value** | **float** | the value of the rating | [optional] 
**votes_count** | **int** | the amount of feedbac | [optional] 
**rating_max** | **float** | the maximum value for a rating_type | [optional] 
**type** | **str** | type of element | [optional] 
**position** | **str** | the alignment of the element in Google Shopping SERP possible values: left, right | [optional] 

## Example

```python
from dataforseo_client.models.rating_element import RatingElement

# TODO update the JSON string below
json = "{}"
# create an instance of RatingElement from a JSON string
rating_element_instance = RatingElement.from_json(json)
# print the JSON string representation of the object
print(RatingElement.to_json())

# convert the object into a dict
rating_element_dict = rating_element_instance.to_dict()
# create an instance of RatingElement from a dict
rating_element_from_dict = RatingElement.from_dict(rating_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


