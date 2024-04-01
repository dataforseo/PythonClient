# DataforseoLabsGoogleKeywordIdeasLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keywords** | **List[str]** | keywords required field UTF-8 encoding The maximum number of keywords you can specify: 200. The minimum number of characters for each keyword: 3. The keywords will be converted to lowercase format | [optional] 
**location_name** | **str** | full name of the location required field if you don’t specify location_code Note: it is required to specify either location_name or location_code you can receive the list of available locations with their location_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: United Kingdom | [optional] 
**location_code** | **int** | unique location identifier required field if you don’t specify location_name Note: it is required to specify either location_name or location_code you can receive the list of available locations with their location_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: 2840 | [optional] 
**language_name** | **str** | full name of the language optional field if you use this field, you don’t need to specify language_code you can receive the list of available languages with their language_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages ignore this field to get the results for all available languages example: English | [optional] 
**language_code** | **str** | language code optional field if you use this field, you don’t need to specify language_name you can receive the list of available languages with their language_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages ignore this field to get the results for all available languages example: en | [optional] 
**closely_variants** | **bool** | search mode optional field if set to true the results will be based on the phrase-match search algorithm if set to false the results will be based on the broad-match search algorithm default value: false | [optional] 
**ignore_synonyms** | **bool** | ignore highly similar keywords optional field if set to true only core keywords will be returned, all highly similar keywords will be excluded; default value: false | [optional] 
**include_serp_info** | **bool** | include data from SERP for each keyword optional field if set to true, we will return a serp_info array containing SERP data (number of search results, relevant URL, and SERP features) for every keyword in the response default value: false | [optional] 
**limit** | **int** | the maximum number of keywords in the results array optional field default value: 700 maximum value: 1000 | [optional] 
**offset** | **int** | offset in the results array of returned keywords optional field default value: 0 if you specify the 10 value, the first ten keywords in the results array will be omitted and the data will be provided for the successive keywords | [optional] 
**offset_token** | **str** | offset token for subsequent requests optional field provided in the identical filed of the response to each request; use this parameter to avoid timeouts while trying to obtain over 10,000 results in a single request; by specifying the unique offset_token value from the response array, you will get the subsequent results of the initial task; offset_token values are unique for each subsequent task Note: if the offset_token is specified in the request, all other parameters except limit will not be taken into account when processing a task. | [optional] 
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, &#x3D;, &lt;&gt;, in, not_in, like, not_like you can use the % operator with like and not_like to match any string of zero or more characters note that you can not filter the results by relevance example: [\&quot;keyword_info.search_volume\&quot;,\&quot;&gt;\&quot;,0] [[\&quot;keyword_info.search_volume\&quot;,\&quot;in\&quot;,[0,1000]], \&quot;and\&quot;, [\&quot;keyword_info.competition_level\&quot;,\&quot;&#x3D;\&quot;,\&quot;LOW\&quot;]] [[\&quot;keyword_info.search_volume\&quot;,\&quot;&gt;\&quot;,100], \&quot;and\&quot;, [[\&quot;keyword_info.cpc\&quot;,\&quot;&lt;\&quot;,0.5], \&quot;or\&quot;, [\&quot;keyword_info.high_top_of_page_bid\&quot;,\&quot;&lt;&#x3D;\&quot;,0.5]]] for more information about filters, please refer to Dataforseo Labs – Filters or this help center guide | [optional] 
**order_by** | **List[str]** | results sorting rules optional field you can use the same values as in the filters array to sort the results possible sorting types: asc – results will be sorted in the ascending order desc – results will be sorted in the descending order you should use a comma to set up a sorting parameter example: [\&quot;keyword_info.competition,desc\&quot;] default rule: [\&quot;relevance,desc\&quot;] relevance is used as the default sorting rule to provide you with the closest keyword ideas. We recommend using this sorting rule to get highly-relevant search terms. Note that relevance is only our internal system identifier, so it can not be used as a filter, and you will not find this field in the result array. The relevance score is based on a similar principle as used in the Keywords For Keywords endpoint. note that you can set no more than three sorting rules in a single request you should use a comma to separate several sorting rules example: [\&quot;keyword_info.search_volume,desc\&quot;,\&quot;keyword_info.cpc,desc\&quot;] | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_keyword_ideas_live_request_info import DataforseoLabsGoogleKeywordIdeasLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleKeywordIdeasLiveRequestInfo from a JSON string
dataforseo_labs_google_keyword_ideas_live_request_info_instance = DataforseoLabsGoogleKeywordIdeasLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsGoogleKeywordIdeasLiveRequestInfo.to_json())

# convert the object into a dict
dataforseo_labs_google_keyword_ideas_live_request_info_dict = dataforseo_labs_google_keyword_ideas_live_request_info_instance.to_dict()
# create an instance of DataforseoLabsGoogleKeywordIdeasLiveRequestInfo from a dict
dataforseo_labs_google_keyword_ideas_live_request_info_form_dict = dataforseo_labs_google_keyword_ideas_live_request_info.from_dict(dataforseo_labs_google_keyword_ideas_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


