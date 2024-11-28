# Advertiser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**advertiser_id** | **str** | unique identifier of the advertiser account can be used to obtain data on advertising campaigns from the Google Ads Search endpoint | [optional] 
**location** | **str** | location of the advertiser account country code associated with the advertiser account | [optional] 
**verified** | **bool** | verified advertiser account equals true if advertiser account is verified by Google Ads | [optional] 
**approx_ads_count** | **int** | ads count the approximate number of ads that are run by the advertiser account across all available Google Ads platforms | [optional] 

## Example

```python
from dataforseo_client.models.advertiser import Advertiser

# TODO update the JSON string below
json = "{}"
# create an instance of Advertiser from a JSON string
advertiser_instance = Advertiser.from_json(json)
# print the JSON string representation of the object
print(Advertiser.to_json())

# convert the object into a dict
advertiser_dict = advertiser_instance.to_dict()
# create an instance of Advertiser from a dict
advertiser_from_dict = Advertiser.from_dict(advertiser_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


