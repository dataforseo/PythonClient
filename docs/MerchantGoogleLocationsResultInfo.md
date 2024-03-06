[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# MerchantGoogleLocationsResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_code** | **int** | location code | [optional]
**location_name** | **str** | full name of the location | [optional]
**location_name_parent** | **str** | the name of the superordinate location example: \&quot;location_name\&quot;: \&quot;Arkansas,United States\&quot;, \&quot;location_name_parent\&quot;: \&quot;United States\&quot; | [optional]
**country_iso_code** | **str** | ISO country code of the location | [optional]
**location_type** | **str** | location type | [optional]

## Example

```python
from dataforseo_client.models.merchant_google_locations_result_info import MerchantGoogleLocationsResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantGoogleLocationsResultInfo from a JSON string
merchant_google_locations_result_info_instance = MerchantGoogleLocationsResultInfo.from_json(json)
# print the JSON string representation of the object
print MerchantGoogleLocationsResultInfo.to_json()

# convert the object into a dict
merchant_google_locations_result_info_dict = merchant_google_locations_result_info_instance.to_dict()
# create an instance of MerchantGoogleLocationsResultInfo from a dict
merchant_google_locations_result_info_form_dict = merchant_google_locations_result_info.from_dict(merchant_google_locations_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")