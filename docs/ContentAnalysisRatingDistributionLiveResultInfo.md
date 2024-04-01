# ContentAnalysisRatingDistributionLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**min** | **float** | min rating on a distribution scale | [optional] 
**max** | **float** | max rating on a distribution scale | [optional] 
**metrics** | [**ContentAnalysisSummaryInfo**](ContentAnalysisSummaryInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.content_analysis_rating_distribution_live_result_info import ContentAnalysisRatingDistributionLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentAnalysisRatingDistributionLiveResultInfo from a JSON string
content_analysis_rating_distribution_live_result_info_instance = ContentAnalysisRatingDistributionLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(ContentAnalysisRatingDistributionLiveResultInfo.to_json())

# convert the object into a dict
content_analysis_rating_distribution_live_result_info_dict = content_analysis_rating_distribution_live_result_info_instance.to_dict()
# create an instance of ContentAnalysisRatingDistributionLiveResultInfo from a dict
content_analysis_rating_distribution_live_result_info_form_dict = content_analysis_rating_distribution_live_result_info.from_dict(content_analysis_rating_distribution_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


