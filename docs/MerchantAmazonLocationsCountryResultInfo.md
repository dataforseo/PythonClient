# MerchantAmazonLocationsCountryResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_code** | **int** | location code | [optional] 
**location_name** | **str** | full name of the location | [optional] 
**location_name_parent** | **str** | the name of the superordinate location example: \&quot;location_code\&quot;: 9041134, \&quot;location_name\&quot;: \&quot;90290,California,United States\&quot;, \&quot;location_name_parent\&quot;: \&quot;California,United States\&quot; | [optional] 
**country_iso_code** | **str** | ISO country code of the location | [optional] 
**location_type** | **str** | location type | [optional] 

## Example

```python
from dataforseo_client.models.merchant_amazon_locations_country_result_info import MerchantAmazonLocationsCountryResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantAmazonLocationsCountryResultInfo from a JSON string
merchant_amazon_locations_country_result_info_instance = MerchantAmazonLocationsCountryResultInfo.from_json(json)
# print the JSON string representation of the object
print(MerchantAmazonLocationsCountryResultInfo.to_json())

# convert the object into a dict
merchant_amazon_locations_country_result_info_dict = merchant_amazon_locations_country_result_info_instance.to_dict()
# create an instance of MerchantAmazonLocationsCountryResultInfo from a dict
merchant_amazon_locations_country_result_info_from_dict = MerchantAmazonLocationsCountryResultInfo.from_dict(merchant_amazon_locations_country_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


