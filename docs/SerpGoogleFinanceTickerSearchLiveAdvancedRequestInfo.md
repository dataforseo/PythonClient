# SerpGoogleFinanceTickerSearchLiveAdvancedRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | company or financial instrument name required field in this field, you can enter the name of a company or financial instrument to search for relevant tickers; you can specify up to 700 characters in the keyword field; all %## will be decoded (plus character ‘+’ will be decoded to a space character) if you need to use the “%” character for your keyword, please specify it as “%25”; if you need to use the “+” character for your keyword, please specify it as “%2B”; learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article | [optional] 
**location_name** | **str** | full name of search engine location required field if you don’t specify location_code if you use this field, you don’t need to specify location_code you can receive the list of available locations of the search engine with their location_name by making a separate request to  https://api.dataforseo.com/v3/serp/google/locations example: London,England,United Kingdom | [optional] 
**location_code** | **int** | search engine location code required field if you don’t specify location_name if you use this field, you don’t need to specify location_name you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/serp/google/locations example: 2840 | [optional] 
**language_name** | **str** | full name of search engine language required field if you don’t specify language_code  if you use this field, you don’t need to specify language_code you can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/serp/google/languages example: English | [optional] 
**language_code** | **str** | search engine language code required field if you don’t specify language_name if you use this field, you don’t need to specify language_name you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/languages example: en | [optional] 
**category** | **str** | category of financial instruments to search for optional field possible values: all, stock, index, mutual_fund, currency, futures default value: all | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.serp_google_finance_ticker_search_live_advanced_request_info import SerpGoogleFinanceTickerSearchLiveAdvancedRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpGoogleFinanceTickerSearchLiveAdvancedRequestInfo from a JSON string
serp_google_finance_ticker_search_live_advanced_request_info_instance = SerpGoogleFinanceTickerSearchLiveAdvancedRequestInfo.from_json(json)
# print the JSON string representation of the object
print(SerpGoogleFinanceTickerSearchLiveAdvancedRequestInfo.to_json())

# convert the object into a dict
serp_google_finance_ticker_search_live_advanced_request_info_dict = serp_google_finance_ticker_search_live_advanced_request_info_instance.to_dict()
# create an instance of SerpGoogleFinanceTickerSearchLiveAdvancedRequestInfo from a dict
serp_google_finance_ticker_search_live_advanced_request_info_from_dict = SerpGoogleFinanceTickerSearchLiveAdvancedRequestInfo.from_dict(serp_google_finance_ticker_search_live_advanced_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


