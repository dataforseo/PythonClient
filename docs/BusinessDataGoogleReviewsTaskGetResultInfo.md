# BusinessDataGoogleReviewsTaskGetResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword received in a POST array keyword is returned with decoded %## (plus character ‘+’ will be decoded to a space character) | [optional] 
**type** | **str** | type of element | [optional] 
**se_domain** | **str** | search engine domain in a POST array | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**check_url** | **str** | direct URL to search engine results you can use it to make sure that we provided accurate results | [optional] 
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**title** | **str** | title of the ‘reviews’ element in SERP the name of the local establishment for which the reviews are collected | [optional] 
**sub_title** | **str** | subtitle of the ‘reviews’ element in SERP additional information (e.g., address) on the ‘reviews’ element for which the reviews are collected | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 
**feature_id** | **str** | the unique identifier of the ‘reviews’ element in SERP learn more about the identifier in this help center article | [optional] 
**place_id** | **str** | unique identifier of a business location assigned by Google learn more about the identifier in this help center article | [optional] 
**cid** | **str** | google-defined client id unique id of a local establishment learn more about the identifier in this help center article | [optional] 
**reviews_count** | **int** | the total number of reviews | [optional] 
**items_count** | **int** | the number of reviews items in the results array you can get more results by using the depth parameter when setting a task | [optional] 
**items** | [**List[BaseBusinessDataSerpElementItem]**](BaseBusinessDataSerpElementItem.md) | found reviews you can get more results by using the depth parameter when setting a task | [optional] 

## Example

```python
from dataforseo_client.models.business_data_google_reviews_task_get_result_info import BusinessDataGoogleReviewsTaskGetResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataGoogleReviewsTaskGetResultInfo from a JSON string
business_data_google_reviews_task_get_result_info_instance = BusinessDataGoogleReviewsTaskGetResultInfo.from_json(json)
# print the JSON string representation of the object
print(BusinessDataGoogleReviewsTaskGetResultInfo.to_json())

# convert the object into a dict
business_data_google_reviews_task_get_result_info_dict = business_data_google_reviews_task_get_result_info_instance.to_dict()
# create an instance of BusinessDataGoogleReviewsTaskGetResultInfo from a dict
business_data_google_reviews_task_get_result_info_from_dict = BusinessDataGoogleReviewsTaskGetResultInfo.from_dict(business_data_google_reviews_task_get_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


