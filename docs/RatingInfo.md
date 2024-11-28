# RatingInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rating_type** | **str** | the type of rating here you can find the following elements: Max5, Percents, CustomMax | [optional] 
**value** | **float** | the value of the rating | [optional] 
**votes_count** | **int** | the amount of feedback | [optional] 
**rating_max** | **int** | the maximum value for a rating_type | [optional] 

## Example

```python
from dataforseo_client.models.rating_info import RatingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RatingInfo from a JSON string
rating_info_instance = RatingInfo.from_json(json)
# print the JSON string representation of the object
print(RatingInfo.to_json())

# convert the object into a dict
rating_info_dict = rating_info_instance.to_dict()
# create an instance of RatingInfo from a dict
rating_info_from_dict = RatingInfo.from_dict(rating_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


