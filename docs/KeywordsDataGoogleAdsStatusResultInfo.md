# KeywordsDataGoogleAdsStatusResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_data** | **bool** | indicates whether Google updated keyword data for the previous month generally, Google updates keyword data in the middle of the month if the value is true, Google currently provides up-to-date data for the previous month if the value is false, we are not able to provide data for the previous month | [optional] 
**date_update** | **str** | date of the latest update of Google Ads data indicates the latest date when Google updated search volume, CPC, and other keyword metrics example: 2020-05-15 | [optional] 
**last_year_in_monthly_searches** | **int** | the latest year for which search volume data is available | [optional] 
**last_month_in_monthly_searches** | **int** | the latest month for which search volume data is available | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_google_ads_status_result_info import KeywordsDataGoogleAdsStatusResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataGoogleAdsStatusResultInfo from a JSON string
keywords_data_google_ads_status_result_info_instance = KeywordsDataGoogleAdsStatusResultInfo.from_json(json)
# print the JSON string representation of the object
print KeywordsDataGoogleAdsStatusResultInfo.to_json()

# convert the object into a dict
keywords_data_google_ads_status_result_info_dict = keywords_data_google_ads_status_result_info_instance.to_dict()
# create an instance of KeywordsDataGoogleAdsStatusResultInfo from a dict
keywords_data_google_ads_status_result_info_form_dict = keywords_data_google_ads_status_result_info.from_dict(keywords_data_google_ads_status_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


