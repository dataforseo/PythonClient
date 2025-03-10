# SerpGoogleFinanceQuoteLiveHtmlRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | ticker or stock symbol required field in this field you can pass the ticker symbol of publicly traded shares of a particular stock or security on a particular stock exchange; you can specify up to 700 characters in the keyword field; all %## will be decoded (plus character ‘+’ will be decoded to a space character) if you need to use the “%” character for your keyword, please specify it as “%25”; if you need to use the “+” character for your keyword, please specify it as “%2B”; learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article | [optional] 
**location_name** | **str** | full name of search engine location required field if you don’t specify location_code if you use this field, you don’t need to specify location_code you can receive the list of available locations of the search engine with their location_name by making a separate request to  https://api.dataforseo.com/v3/serp/google/locations example: London,England,United Kingdom | [optional] 
**location_code** | **int** | search engine location code required field if you don’t specify location_name if you use this field, you don’t need to specify location_name you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/serp/google/locations example: 2840 | [optional] 
**language_name** | **str** | full name of search engine language required field if you don’t specify language_code  if you use this field, you don’t need to specify language_code you can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/serp/google/languages example: English | [optional] 
**language_code** | **str** | search engine language code required field if you don’t specify language_name if you use this field, you don’t need to specify language_name you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/languages example: en | [optional] 
**device** | **str** | device type optional field possible value: desktop | [optional] 
**os** | **str** | device operating system optional field possible values: windows | [optional] 
**window** | **str** | time window for google_finance_quote graph optional field possible values: 1D, 5D, 1M, 6M, YTD, 1Y, 5Y, MAX default value: 1D | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.serp_google_finance_quote_live_html_request_info import SerpGoogleFinanceQuoteLiveHtmlRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpGoogleFinanceQuoteLiveHtmlRequestInfo from a JSON string
serp_google_finance_quote_live_html_request_info_instance = SerpGoogleFinanceQuoteLiveHtmlRequestInfo.from_json(json)
# print the JSON string representation of the object
print(SerpGoogleFinanceQuoteLiveHtmlRequestInfo.to_json())

# convert the object into a dict
serp_google_finance_quote_live_html_request_info_dict = serp_google_finance_quote_live_html_request_info_instance.to_dict()
# create an instance of SerpGoogleFinanceQuoteLiveHtmlRequestInfo from a dict
serp_google_finance_quote_live_html_request_info_from_dict = SerpGoogleFinanceQuoteLiveHtmlRequestInfo.from_dict(serp_google_finance_quote_live_html_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


