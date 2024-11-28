# SerpGoogleAdsAdvertisersLocationsResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_code** | **int** | location code | [optional] 
**location_name** | **str** | full name of the location | [optional] 
**location_code_parent** | **int** | the code of the superordinate location example: \&quot;location_code\&quot;: 9041134, \&quot;location_name\&quot;: \&quot;Vienna International Airport,Lower Austria,Austria\&quot;, \&quot;location_code_parent\&quot;: 20044 where location_code_parent corresponds to: \&quot;location_code\&quot;: 20044, \&quot;location_name\&quot;: \&quot;Lower Austria,Austria\&quot; | [optional] 
**country_iso_code** | **str** | ISO country code of the location | [optional] 
**location_type** | **str** | location type | [optional] 

## Example

```python
from dataforseo_client.models.serp_google_ads_advertisers_locations_result_info import SerpGoogleAdsAdvertisersLocationsResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpGoogleAdsAdvertisersLocationsResultInfo from a JSON string
serp_google_ads_advertisers_locations_result_info_instance = SerpGoogleAdsAdvertisersLocationsResultInfo.from_json(json)
# print the JSON string representation of the object
print(SerpGoogleAdsAdvertisersLocationsResultInfo.to_json())

# convert the object into a dict
serp_google_ads_advertisers_locations_result_info_dict = serp_google_ads_advertisers_locations_result_info_instance.to_dict()
# create an instance of SerpGoogleAdsAdvertisersLocationsResultInfo from a dict
serp_google_ads_advertisers_locations_result_info_from_dict = SerpGoogleAdsAdvertisersLocationsResultInfo.from_dict(serp_google_ads_advertisers_locations_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


