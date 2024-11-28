# KeywordsDataGoogleAdsLocationsCountryResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_code** | **int** | location code | [optional] 
**location_name** | **str** | full name of the location | [optional] 
**location_code_parent** | **int** | the code of the superordinate location example: \&quot;location_code\&quot;: 9041134, \&quot;location_name\&quot;: \&quot;Vienna International Airport,Lower Austria,Austria\&quot;, \&quot;location_code_parent\&quot;: 20044 where location_code_parent corresponds to: \&quot;location_code\&quot;: 20044, \&quot;location_name\&quot;: \&quot;Lower Austria,Austria\&quot; | [optional] 
**country_iso_code** | **str** | ISO country code of the location | [optional] 
**location_type** | **str** | location type possible values according to Google’s target types | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_google_ads_locations_country_result_info import KeywordsDataGoogleAdsLocationsCountryResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataGoogleAdsLocationsCountryResultInfo from a JSON string
keywords_data_google_ads_locations_country_result_info_instance = KeywordsDataGoogleAdsLocationsCountryResultInfo.from_json(json)
# print the JSON string representation of the object
print(KeywordsDataGoogleAdsLocationsCountryResultInfo.to_json())

# convert the object into a dict
keywords_data_google_ads_locations_country_result_info_dict = keywords_data_google_ads_locations_country_result_info_instance.to_dict()
# create an instance of KeywordsDataGoogleAdsLocationsCountryResultInfo from a dict
keywords_data_google_ads_locations_country_result_info_from_dict = KeywordsDataGoogleAdsLocationsCountryResultInfo.from_dict(keywords_data_google_ads_locations_country_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


