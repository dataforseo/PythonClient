# ContentRatingInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | rating name here you can find the following elements: Max5, Percents, CustomMax | [optional] 
**rating_value** | **str** | the value of the rating | [optional] 
**rating_count** | **str** | number of votes | [optional] 
**max_rating_value** | **str** | maximum value for the rating name | [optional] 
**relative_rating** | **str** | relative rating | [optional] 

## Example

```python
from dataforseo_client.models.content_rating_info import ContentRatingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentRatingInfo from a JSON string
content_rating_info_instance = ContentRatingInfo.from_json(json)
# print the JSON string representation of the object
print(ContentRatingInfo.to_json())

# convert the object into a dict
content_rating_info_dict = content_rating_info_instance.to_dict()
# create an instance of ContentRatingInfo from a dict
content_rating_info_from_dict = ContentRatingInfo.from_dict(content_rating_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


