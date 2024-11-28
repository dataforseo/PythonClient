# KeywordsDataDataforseoTrendsDemographyLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keywords** | **List[Optional[str]]** | keywords in a POST array | [optional] 
**type** | **str** | type of element | [optional] 
**location_code** | **int** | location code in a POST array if there is no data, then the value is null | [optional] 
**language_code** | **str** | language code in a POST array if there is no data, then the value is null | [optional] 
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[DataforseoTrendsDemographyInfo]**](DataforseoTrendsDemographyInfo.md) | contains keyword popularity and related data | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_dataforseo_trends_demography_live_result_info import KeywordsDataDataforseoTrendsDemographyLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataDataforseoTrendsDemographyLiveResultInfo from a JSON string
keywords_data_dataforseo_trends_demography_live_result_info_instance = KeywordsDataDataforseoTrendsDemographyLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(KeywordsDataDataforseoTrendsDemographyLiveResultInfo.to_json())

# convert the object into a dict
keywords_data_dataforseo_trends_demography_live_result_info_dict = keywords_data_dataforseo_trends_demography_live_result_info_instance.to_dict()
# create an instance of KeywordsDataDataforseoTrendsDemographyLiveResultInfo from a dict
keywords_data_dataforseo_trends_demography_live_result_info_from_dict = KeywordsDataDataforseoTrendsDemographyLiveResultInfo.from_dict(keywords_data_dataforseo_trends_demography_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


