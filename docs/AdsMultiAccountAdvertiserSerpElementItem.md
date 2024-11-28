# AdsMultiAccountAdvertiserSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the element | [optional] 
**location** | **str** | advertiser location | [optional] 
**approx_ads_count** | **int** | ads count the approximate number of ads that are run by the advertiser across all available Google Ads platforms | [optional] 
**advertisers** | [**List[Advertiser]**](Advertiser.md) | associated advertiser accounts contains objects with data on associated advertiser accounts | [optional] 

## Example

```python
from dataforseo_client.models.ads_multi_account_advertiser_serp_element_item import AdsMultiAccountAdvertiserSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of AdsMultiAccountAdvertiserSerpElementItem from a JSON string
ads_multi_account_advertiser_serp_element_item_instance = AdsMultiAccountAdvertiserSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(AdsMultiAccountAdvertiserSerpElementItem.to_json())

# convert the object into a dict
ads_multi_account_advertiser_serp_element_item_dict = ads_multi_account_advertiser_serp_element_item_instance.to_dict()
# create an instance of AdsMultiAccountAdvertiserSerpElementItem from a dict
ads_multi_account_advertiser_serp_element_item_from_dict = AdsMultiAccountAdvertiserSerpElementItem.from_dict(ads_multi_account_advertiser_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


