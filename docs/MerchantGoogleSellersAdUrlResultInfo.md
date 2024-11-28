# MerchantGoogleSellersAdUrlResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_aclk** | **str** | unique ad click referral parameter | [optional] 
**ad_url** | **str** | full URL of the advertisement | [optional] 
**ad_url_redirects** | **List[Optional[str]]** | URLs where the link from Google Shopping redirects before reaching a final URL includes up to 10 URLs of the ad’s redirect path to the seller’s ad_url | [optional] 

## Example

```python
from dataforseo_client.models.merchant_google_sellers_ad_url_result_info import MerchantGoogleSellersAdUrlResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantGoogleSellersAdUrlResultInfo from a JSON string
merchant_google_sellers_ad_url_result_info_instance = MerchantGoogleSellersAdUrlResultInfo.from_json(json)
# print the JSON string representation of the object
print(MerchantGoogleSellersAdUrlResultInfo.to_json())

# convert the object into a dict
merchant_google_sellers_ad_url_result_info_dict = merchant_google_sellers_ad_url_result_info_instance.to_dict()
# create an instance of MerchantGoogleSellersAdUrlResultInfo from a dict
merchant_google_sellers_ad_url_result_info_from_dict = MerchantGoogleSellersAdUrlResultInfo.from_dict(merchant_google_sellers_ad_url_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


