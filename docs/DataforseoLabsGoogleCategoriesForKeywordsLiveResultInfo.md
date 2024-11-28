# DataforseoLabsGoogleCategoriesForKeywordsLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_code** | **str** | language code in a POST array if there is no data, then the value is null | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[DataforseoLabsGoogleCategoriesForKeywordsLiveItem]**](DataforseoLabsGoogleCategoriesForKeywordsLiveItem.md) | contains keywords and related keyword difficulty scores | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_categories_for_keywords_live_result_info import DataforseoLabsGoogleCategoriesForKeywordsLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleCategoriesForKeywordsLiveResultInfo from a JSON string
dataforseo_labs_google_categories_for_keywords_live_result_info_instance = DataforseoLabsGoogleCategoriesForKeywordsLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsGoogleCategoriesForKeywordsLiveResultInfo.to_json())

# convert the object into a dict
dataforseo_labs_google_categories_for_keywords_live_result_info_dict = dataforseo_labs_google_categories_for_keywords_live_result_info_instance.to_dict()
# create an instance of DataforseoLabsGoogleCategoriesForKeywordsLiveResultInfo from a dict
dataforseo_labs_google_categories_for_keywords_live_result_info_from_dict = DataforseoLabsGoogleCategoriesForKeywordsLiveResultInfo.from_dict(dataforseo_labs_google_categories_for_keywords_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


