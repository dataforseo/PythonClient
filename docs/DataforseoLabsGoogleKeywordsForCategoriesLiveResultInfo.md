# DataforseoLabsGoogleKeywordsForCategoriesLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**seed_categories** | **List[Optional[int]]** | categories in a POST array | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**total_count** | **int** | the total amount of results in our database relevant to your request | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**offset** | **int** | current offset value | [optional] 
**offset_token** | **str** | offset token for subsequent requests you can use the string provided in this field to get the subsequent results of the initial task; note: offset_token values are unique for each subsequent task | [optional] 
**items** | [**List[KeywordDataInfo]**](KeywordDataInfo.md) | contains keyword ideas and related data | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_keywords_for_categories_live_result_info import DataforseoLabsGoogleKeywordsForCategoriesLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleKeywordsForCategoriesLiveResultInfo from a JSON string
dataforseo_labs_google_keywords_for_categories_live_result_info_instance = DataforseoLabsGoogleKeywordsForCategoriesLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsGoogleKeywordsForCategoriesLiveResultInfo.to_json())

# convert the object into a dict
dataforseo_labs_google_keywords_for_categories_live_result_info_dict = dataforseo_labs_google_keywords_for_categories_live_result_info_instance.to_dict()
# create an instance of DataforseoLabsGoogleKeywordsForCategoriesLiveResultInfo from a dict
dataforseo_labs_google_keywords_for_categories_live_result_info_from_dict = DataforseoLabsGoogleKeywordsForCategoriesLiveResultInfo.from_dict(dataforseo_labs_google_keywords_for_categories_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


