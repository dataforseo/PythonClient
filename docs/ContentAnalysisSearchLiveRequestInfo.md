# ContentAnalysisSearchLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | target keyword required field UTF-8 encoding the keywords will be converted to a lowercase format; Note: to match an exact phrase instead of a stand-alone keyword, use double quotes and backslashes; example: \&quot;keyword\&quot;: \&quot;\\\&quot;tesla palo alto\\\&quot;\&quot; learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article | [optional] 
**keyword_fields** | **Dict[str, Optional[str]]** | target keyword fields and target keywords optional field use this parameter to filter the dataset by keywords that certain fields should contain; fields you can specify: title, main_title, previous_title, snippet you can indicate several fields; Note: to match an exact phrase instead of a stand-alone keyword, use double quotes and backslashes; example: \&quot;keyword_fields\&quot;: {     \&quot;snippet\&quot;: \&quot;\\\&quot;logitech mouse\\\&quot;\&quot;,     \&quot;main_title\&quot;: \&quot;sale\&quot; } | [optional] 
**page_type** | **List[str]** | target page types optional field use this parameter to filter the dataset by page types possible values: \&quot;ecommerce\&quot;, \&quot;news\&quot;, \&quot;blogs\&quot;, \&quot;message-boards\&quot;, \&quot;organization\&quot; | [optional] 
**search_mode** | **str** | results grouping type optional field possible grouping types: as_is – returns all citations for the target keyword one_per_domain – returns one citation of the keyword per domain default value: as_is | [optional] 
**limit** | **int** | the maximum number of returned citations optional field default value: 100 maximum value: 1000 | [optional] 
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, not_regex, &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, &#x3D;, &lt;&gt;, in, not_in, like,not_like, match, not_match you can use the % operator with like and not_like to match any string of zero or more characters example: [\&quot;country\&quot;,\&quot;&#x3D;\&quot;, \&quot;US\&quot;] [[\&quot;domain_rank\&quot;,\&quot;&gt;\&quot;,800],\&quot;and\&quot;,[\&quot;content_info.connotation_types.negative\&quot;,\&quot;&gt;\&quot;,0.9]] [[\&quot;domain_rank\&quot;,\&quot;&gt;\&quot;,800], \&quot;and\&quot;, [[\&quot;page_types\&quot;,\&quot;has\&quot;,\&quot;ecommerce\&quot;], \&quot;or\&quot;, [\&quot;content_info.text_category\&quot;,\&quot;has\&quot;,10994]]] for more information about filters, please refer to Content Analysis API – Filters | [optional] 
**order_by** | **List[str]** | results sorting rules optional field you can use the same values as in the filters array to sort the results possible sorting types: asc – results will be sorted in the ascending order desc – results will be sorted in the descending order you should use a comma to set up a sorting type example: [\&quot;content_info.sentiment_connotations.anger,desc\&quot;] default rule: [\&quot;content_info.sentiment_connotations.anger,desc\&quot;] note that you can set no more than three sorting rules in a single request you should use a comma to separate several sorting rules example: [\&quot;content_info.sentiment_connotations.anger,desc\&quot;,\&quot;keyword_data.keyword_info.cpc,desc\&quot;] | [optional] 
**offset** | **int** | offset in the results array of returned citations optional field default value: 0 if you specify the 10 value, the first ten citations in the results array will be omitted and the data will be provided for the successive citations | [optional] 
**offset_token** | **str** | offset token for subsequent requests optional field provided in the identical field of the response to each request; use this parameter to avoid timeouts while trying to obtain over 10,000 results in a single request; by specifying the unique offset_token value from the response array, you will get the subsequent results of the initial task; offset_token values are unique for each subsequent task Note: if the offset_token is specified in the request, all other parameters except limit will not be taken into account when processing a task | [optional] 
**rank_scale** | **str** | defines the scale used for calculating and displaying the domain_rank, and url_rank values optional field you can use this parameter to choose whether rank values are presented on a 0–100 or 0–1000 scale possible values: one_hundred — rank values are displayed on a 0–100 scale one_thousand — rank values are displayed on a 0–1000 scale default value: one_thousand learn more about how this parameter works in this Help Center article | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.content_analysis_search_live_request_info import ContentAnalysisSearchLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentAnalysisSearchLiveRequestInfo from a JSON string
content_analysis_search_live_request_info_instance = ContentAnalysisSearchLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(ContentAnalysisSearchLiveRequestInfo.to_json())

# convert the object into a dict
content_analysis_search_live_request_info_dict = content_analysis_search_live_request_info_instance.to_dict()
# create an instance of ContentAnalysisSearchLiveRequestInfo from a dict
content_analysis_search_live_request_info_from_dict = ContentAnalysisSearchLiveRequestInfo.from_dict(content_analysis_search_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


