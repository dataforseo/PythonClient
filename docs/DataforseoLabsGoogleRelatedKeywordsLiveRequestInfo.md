# DataforseoLabsGoogleRelatedKeywordsLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword required field UTF-8 encoding the keywords will be converted to lowercase format learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article | [optional] 
**location_name** | **str** | full name of the location required field if you don’t specify location_code Note: it is required to specify either location_name or location_code you can receive the list of available locations with their location_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: United Kingdom | [optional] 
**location_code** | **int** | location code required field if you don’t specify location_name Note: it is required to specify either location_name or location_code you can receive the list of available locations with their location_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: 2840 | [optional] 
**language_name** | **str** | full name of the language required field if you don’t specify language_code Note: it is required to specify either language_name or language_code you can receive the list of available locations with their language_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: English | [optional] 
**language_code** | **str** | language code required field if you don’t specify language_name Note: it is required to specify either language_name or language_code you can receive the list of available locations with their language_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: en | [optional] 
**depth** | **int** | keyword search depth optional field default value: 1 number of the returned results depends on the value you set in this field you can specify a level from 0 to 4 estimated number of keywords for each level (maximum): 0 – the keyword set in the keyword field 1 – 8 keywords 2 – 72 keywords 3 – 584 keywords 4 – 4680 keywords | [optional] 
**include_seed_keyword** | **bool** | include data for the seed keyword optional field if set to true, data for the seed keyword specified in the keyword field will be provided in the seed_keyword_data array of the response default value: false | [optional] 
**include_serp_info** | **bool** | include data from SERP for each keyword optional field if set to true, we will return a serp_info array containing SERP data (number of search results, relevant URL, and SERP features) for every keyword in the response default value: false | [optional] 
**include_clickstream_data** | **bool** | include or exclude data from clickstream-based metrics in the result optional field if the parameter is set to true, you will receive clickstream_keyword_info, keyword_info_normalized_with_clickstream, and keyword_info_normalized_with_bing fields in the response default value: false with this parameter enabled, you will be charged double the price for the request learn more about how clickstream-based metrics are calculated in this help center article | [optional] 
**ignore_synonyms** | **bool** | ignore highly similar keywords optional field if set to true only core keywords will be returned, all highly similar keywords will be excluded; default value: false | [optional] 
**replace_with_core_keyword** | **bool** | return data for core keyword optional field if true, serp_info and related_keywords will be returned for the main keyword in the group that the specified keyword belongs to; if false, serp_info and related_keywords will be returned for the specified keyword (if available); refer to this help center article for more details; default value: false | [optional] 
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, not_regex, &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, &#x3D;, &lt;&gt;, in, not_in, match, not_match, ilike, not_ilike, like,not_like you can use the % operator with like and not_like, as well as ilike and not_ilike to match any string of zero or more characters example: [\&quot;keyword_data.keyword_info.search_volume\&quot;,\&quot;&gt;\&quot;,0] [[\&quot;keyword_info.search_volume\&quot;,\&quot;in\&quot;,[0,1000]], \&quot;and\&quot;, [\&quot;keyword_data.keyword_info.competition_level\&quot;,\&quot;&#x3D;\&quot;,\&quot;LOW\&quot;]] [[\&quot;keyword_data.keyword_info.search_volume\&quot;,\&quot;&gt;\&quot;,100], \&quot;and\&quot;, [[\&quot;keyword_data.keyword_info.cpc\&quot;,\&quot;&lt;\&quot;,0.5], \&quot;or\&quot;, [\&quot;keyword_info.high_top_of_page_bid\&quot;,\&quot;&lt;&#x3D;\&quot;,0.5]]] for more information about filters, please refer to Dataforseo Labs – Filters or this help center guide | [optional] 
**order_by** | **List[str]** | results sorting rules optional field you can use the same values as in the filters array to sort the results possible sorting types: asc – results will be sorted in the ascending order desc – results will be sorted in the descending order you should use a comma to set up a sorting type example: [\&quot;keyword_data.keyword_info.competition,desc\&quot;] default rule: [\&quot;keyword_data.keyword_info.search_volume,desc\&quot;] note that you can set no more than three sorting rules in a single request you should use a comma to separate several sorting rules example: [\&quot;keyword_data.keyword_info.search_volume,desc\&quot;,\&quot;keyword_data.keyword_info.cpc,desc\&quot;] | [optional] 
**limit** | **int** | the maximum number of returned keywords optional field default value: 100 maximum value: 1000 | [optional] 
**offset** | **int** | offset in the results array of returned keywords optional field default value: 0 if you specify the 10 value, the first ten keywords in the results array will be omitted and the data will be provided for the successive keywords | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_related_keywords_live_request_info import DataforseoLabsGoogleRelatedKeywordsLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleRelatedKeywordsLiveRequestInfo from a JSON string
dataforseo_labs_google_related_keywords_live_request_info_instance = DataforseoLabsGoogleRelatedKeywordsLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsGoogleRelatedKeywordsLiveRequestInfo.to_json())

# convert the object into a dict
dataforseo_labs_google_related_keywords_live_request_info_dict = dataforseo_labs_google_related_keywords_live_request_info_instance.to_dict()
# create an instance of DataforseoLabsGoogleRelatedKeywordsLiveRequestInfo from a dict
dataforseo_labs_google_related_keywords_live_request_info_from_dict = DataforseoLabsGoogleRelatedKeywordsLiveRequestInfo.from_dict(dataforseo_labs_google_related_keywords_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


