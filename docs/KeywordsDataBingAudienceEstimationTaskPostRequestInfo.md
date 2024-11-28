# KeywordsDataBingAudienceEstimationTaskPostRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_name** | **str** | full name of search engine location required field if you don’t specify location_code or location_coordinate if you use this field, you don’t need to specify location_code or location_coordinate you can receive the list of available locations of the search engine with their location_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/bing/locations example: London,England,United Kingdom | [optional] 
**location_code** | **int** | search engine location code required field if you don’t specify location_name or location_coordinate if you use this field, you don’t need to specify location_name or location_coordinate you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/bing/locations example: 2840 | [optional] 
**location_coordinate** | **str** | GPS coordinates of a location required field if you don’t specify location_name or location_code if you use this field, you don’t need to specify location_name or location_code location_coordinate parameter should be specified in the “latitude,longitude,radius (in km)” format the data will be provided for the country the specified coordinates belong to example: 29.6821525,-82.4098881,100 | [optional] 
**age** | **List[str]** | selection of age ranges for targeting possible values: eighteen_to_twenty_four, fifty_to_sixty_four, sixty_five_and_above, thirteen_to_seventeen, thirty_five_to_forty_nine, twenty_five_to_thirty_four, unknown, zero_to_twelve | [optional] 
**bid** | **float** | desired bid setting value in USD maximum value: 1000 | [optional] 
**daily_budget** | **float** | daily campaign budget value in USD maximum value: 10000 | [optional] 
**gender** | **List[str]** | gender to target possible values: male, female, unknown | [optional] 
**industry** | **List[str]** | industry of LinkedIn profile targeting if you use this field, you can receive the list of available industry names  with industry_id by making a separate request to the https://api.dataforseo.com/v3/keywords_data/bing/audience_estimation/industries example: 806301758 | [optional] 
**job_function** | **List[str]** | job function of LinkedIn profile targeting if you use this field, you can receive the list of available job function names  with job_function_id by making a separate request to the https://api.dataforseo.com/v3/keywords_data/bing/audience_estimation/job_functions example: 806300451 | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_bing_audience_estimation_task_post_request_info import KeywordsDataBingAudienceEstimationTaskPostRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataBingAudienceEstimationTaskPostRequestInfo from a JSON string
keywords_data_bing_audience_estimation_task_post_request_info_instance = KeywordsDataBingAudienceEstimationTaskPostRequestInfo.from_json(json)
# print the JSON string representation of the object
print(KeywordsDataBingAudienceEstimationTaskPostRequestInfo.to_json())

# convert the object into a dict
keywords_data_bing_audience_estimation_task_post_request_info_dict = keywords_data_bing_audience_estimation_task_post_request_info_instance.to_dict()
# create an instance of KeywordsDataBingAudienceEstimationTaskPostRequestInfo from a dict
keywords_data_bing_audience_estimation_task_post_request_info_from_dict = KeywordsDataBingAudienceEstimationTaskPostRequestInfo.from_dict(keywords_data_bing_audience_estimation_task_post_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


