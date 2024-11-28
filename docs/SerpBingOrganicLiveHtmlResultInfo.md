# SerpBingOrganicLiveHtmlResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword received in a POST array keyword is returned with decoded %## (plus character ‘+’ will be decoded to a space character) | [optional] 
**type** | **str** | type of element | [optional] 
**se_domain** | **str** | search engine domain in a POST array | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[HtmlItem]**](HtmlItem.md) | elements of search results found in SERP | [optional] 

## Example

```python
from dataforseo_client.models.serp_bing_organic_live_html_result_info import SerpBingOrganicLiveHtmlResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpBingOrganicLiveHtmlResultInfo from a JSON string
serp_bing_organic_live_html_result_info_instance = SerpBingOrganicLiveHtmlResultInfo.from_json(json)
# print the JSON string representation of the object
print(SerpBingOrganicLiveHtmlResultInfo.to_json())

# convert the object into a dict
serp_bing_organic_live_html_result_info_dict = serp_bing_organic_live_html_result_info_instance.to_dict()
# create an instance of SerpBingOrganicLiveHtmlResultInfo from a dict
serp_bing_organic_live_html_result_info_from_dict = SerpBingOrganicLiveHtmlResultInfo.from_dict(serp_bing_organic_live_html_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


