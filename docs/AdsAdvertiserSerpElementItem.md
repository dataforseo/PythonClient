# AdsAdvertiserSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the element | [optional] 
**advertiser_id** | **str** | unique identifier of the advertiser account can be used to obtain data on advertising campaigns from the Google Ads Search endpoint | [optional] 
**location** | **str** | advertiser location | [optional] 
**verified** | **bool** | verified advertiser account equals true if advertiser account is verified by Google Ads | [optional] 
**approx_ads_count** | **int** | ads count the approximate number of ads that are run by the advertiser across all available Google Ads platforms | [optional] 

## Example

```python
from dataforseo_client.models.ads_advertiser_serp_element_item import AdsAdvertiserSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of AdsAdvertiserSerpElementItem from a JSON string
ads_advertiser_serp_element_item_instance = AdsAdvertiserSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(AdsAdvertiserSerpElementItem.to_json())

# convert the object into a dict
ads_advertiser_serp_element_item_dict = ads_advertiser_serp_element_item_instance.to_dict()
# create an instance of AdsAdvertiserSerpElementItem from a dict
ads_advertiser_serp_element_item_from_dict = AdsAdvertiserSerpElementItem.from_dict(ads_advertiser_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


