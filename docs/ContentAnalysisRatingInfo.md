# ContentAnalysisRatingInfo

content rating rating related to content_info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | rating name here you can find the following elements: Max5, Percents, CustomMax | [optional] 
**rating_value** | **float** | the value of the rating | [optional] 
**rating_count** | **int** | number of votes | [optional] 
**max_rating_value** | **str** |  maximum value for the rating name | [optional] 
**relative_rating** | **float** | relative rating | [optional] 

## Example

```python
from dataforseo_client.models.content_analysis_rating_info import ContentAnalysisRatingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentAnalysisRatingInfo from a JSON string
content_analysis_rating_info_instance = ContentAnalysisRatingInfo.from_json(json)
# print the JSON string representation of the object
print(ContentAnalysisRatingInfo.to_json())

# convert the object into a dict
content_analysis_rating_info_dict = content_analysis_rating_info_instance.to_dict()
# create an instance of ContentAnalysisRatingInfo from a dict
content_analysis_rating_info_from_dict = ContentAnalysisRatingInfo.from_dict(content_analysis_rating_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


