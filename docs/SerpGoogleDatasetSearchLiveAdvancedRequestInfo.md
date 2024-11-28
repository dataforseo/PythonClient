# SerpGoogleDatasetSearchLiveAdvancedRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword required field you can specify up to 700 characters in the keyword field all %## will be decoded (plus character ‘+’ will be decoded to a space character) if you need to use the “%” character for your keyword, please specify it as “%25”; if you need to use the “+” character for your keyword, please specify it as “%2B”; learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article | [optional] 
**language_name** | **str** | full name of search engine language optional field if you use this field, you don’t need to specify language_code possible value: English | [optional] 
**language_code** | **str** | search engine language code optional field if you don’t specify language_name if you use this field, you don’t need to specify language_name possible value: en | [optional] 
**device** | **str** | device type optional field possible value: desktop | [optional] 
**os** | **str** | device operating system optional field choose from the following values: windows, macos default value: windows | [optional] 
**depth** | **int** | parsing depth optional field number of results in SERP default value: 20 max value: 700 Note: your account will be billed per each SERP containing up to 20 results; thus, setting a depth above 20 may result in additional charges if the search engine returns more than 20 results; if the specified depth is higher than the number of results in the response, the difference will be refunded automatically to your account balance | [optional] 
**last_updated** | **str** | last time the dataset was updated optional field possible values: 1m, 1y, 3y | [optional] 
**file_formats** | **List[str]** | file formats of the dataset optional field possible values: other, archive, text, image, document, tabular | [optional] 
**usage_rights** | **str** | usage rights of the dataset optional field possible values: commercial, noncommercial | [optional] 
**is_free** | **bool** | indicates whether displayed datasets are free optional field possible values: true, false | [optional] 
**topics** | **List[str]** | dataset topics optional field possible values: humanities, social_sciences, life_sciences, agriculture, natural_sciences, geo, computer, architecture_and_urban_planning, engineering | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.serp_google_dataset_search_live_advanced_request_info import SerpGoogleDatasetSearchLiveAdvancedRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpGoogleDatasetSearchLiveAdvancedRequestInfo from a JSON string
serp_google_dataset_search_live_advanced_request_info_instance = SerpGoogleDatasetSearchLiveAdvancedRequestInfo.from_json(json)
# print the JSON string representation of the object
print(SerpGoogleDatasetSearchLiveAdvancedRequestInfo.to_json())

# convert the object into a dict
serp_google_dataset_search_live_advanced_request_info_dict = serp_google_dataset_search_live_advanced_request_info_instance.to_dict()
# create an instance of SerpGoogleDatasetSearchLiveAdvancedRequestInfo from a dict
serp_google_dataset_search_live_advanced_request_info_from_dict = SerpGoogleDatasetSearchLiveAdvancedRequestInfo.from_dict(serp_google_dataset_search_live_advanced_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


