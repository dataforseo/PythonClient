# DataforseoLabsGoogleKeywordSuggestionsLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword required field UTF-8 encoding a keyword should be at least 3 characters long; the keywords will be converted to lowercase format | [optional] 
**location_name** | **str** | full name of the location optional field if you use this field, you don’t need to specify location_code you can receive the list of available locations with their location_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages ignore this field to get the results for all available locations example: United Kingdom | [optional] 
**location_code** | **int** | location code optional field if you use this field, you don’t need to specify location_name you can receive the list of available locations with their location_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages ignore this field to get the results for all available locations example: 2840 | [optional] 
**language_name** | **str** | full name of the language optional field if you use this field, you don’t need to specify language_code you can receive the list of available languages with their language_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages ignore this field to get the results for all available languages example: English | [optional] 
**language_code** | **str** | language code optional field if you use this field, you don’t need to specify language_name you can receive the list of available languages with their language_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages ignore this field to get the results for all available languages example: en | [optional] 
**include_seed_keyword** | **bool** | include data for the seed keyword optional field if set to true, data for the seed keyword specified in the keyword field will be provided in the seed_keyword_data array of the response default value: false | [optional] 
**include_serp_info** | **bool** | include data from SERP for each keyword optional field if set to true, we will return a serp_info array containing SERP data (number of search results, relevant URL, and SERP features) for every keyword in the response default value: false | [optional] 
**exact_match** | **bool** | search for the exact phrase optional field if set to true, the returned keywords will include the exact keyword phrase you specified, with potentially other words before or after that phrase default value: false | [optional] 
**ignore_synonyms** | **bool** | ignore highly similar keywords optional field if set to true only core keywords will be returned, all highly similar keywords will be excluded; default value: false | [optional] 
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, &#x3D;, &lt;&gt;, in, not_in, like, not_like you can use the % operator with like and not_like to match any string of zero or more characters example: [\&quot;keyword_info.search_volume\&quot;,\&quot;&gt;\&quot;,0] [[\&quot;keyword_info.search_volume\&quot;,\&quot;in\&quot;,[0,1000]], \&quot;and\&quot;, [\&quot;keyword_info.competition_level\&quot;,\&quot;&#x3D;\&quot;,\&quot;LOW\&quot;]][[\&quot;keyword_info.search_volume\&quot;,\&quot;&gt;\&quot;,100], \&quot;and\&quot;, [[\&quot;keyword_info.cpc\&quot;,\&quot;&lt;\&quot;,0.5], \&quot;or\&quot;, [\&quot;keyword_info.high_top_of_page_bid\&quot;,\&quot;&lt;&#x3D;\&quot;,0.5]]] for more information about filters, please refer to Dataforseo Labs – Filters or this help center guide | [optional] 
**order_by** | **List[str]** | results sorting rules optional field you can use the same values as in the filters array to sort the results possible sorting types: asc – results will be sorted in the ascending order desc – results will be sorted in the descending order a comma is used as a separator example: [\&quot;keyword_info.competition,desc\&quot;] default rule: [\&quot;keyword_info.search_volume,desc\&quot;] note that you can set no more than three sorting rules in a single request you should use a comma to separate several sorting rules example: [\&quot;keyword_info.search_volume,desc\&quot;,\&quot;keyword_info.cpc,desc\&quot;] | [optional] 
**limit** | **int** | the maximum number of returned keywords optional field default value: 100 maximum value: 1000 | [optional] 
**offset** | **int** | offset in the results array of returned keywords optional field default value: 0 if you specify the 10 value, the first ten keywords in the results array will be omitted and the data will be provided for the successive keywords | [optional] 
**offset_token** | **str** | offset token for subsequent requests optional field provided in the identical filed of the response to each request; use this parameter to avoid timeouts while trying to obtain over 10,000 results in a single request; by specifying the unique offset_token value from the response array, you will get the subsequent results of the initial task; offset_token values are unique for each subsequent task Note: if the offset_token is specified in the request, all other parameters except limit will not be taken into account when processing a task. | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_keyword_suggestions_live_request_info import DataforseoLabsGoogleKeywordSuggestionsLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleKeywordSuggestionsLiveRequestInfo from a JSON string
dataforseo_labs_google_keyword_suggestions_live_request_info_instance = DataforseoLabsGoogleKeywordSuggestionsLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsGoogleKeywordSuggestionsLiveRequestInfo.to_json()

# convert the object into a dict
dataforseo_labs_google_keyword_suggestions_live_request_info_dict = dataforseo_labs_google_keyword_suggestions_live_request_info_instance.to_dict()
# create an instance of DataforseoLabsGoogleKeywordSuggestionsLiveRequestInfo from a dict
dataforseo_labs_google_keyword_suggestions_live_request_info_form_dict = dataforseo_labs_google_keyword_suggestions_live_request_info.from_dict(dataforseo_labs_google_keyword_suggestions_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


