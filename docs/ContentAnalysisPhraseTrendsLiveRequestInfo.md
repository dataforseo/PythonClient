# ContentAnalysisPhraseTrendsLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | target keyword required field UTF-8 encoding the keywords will be converted to a lowercase format; Note: to match an exact phrase instead of a stand-alone keyword, use double quotes and backslashes; example: \&quot;keyword\&quot;: \&quot;\\\&quot;tesla palo alto\\\&quot;\&quot; learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article | [optional] 
**keyword_fields** | **Dict[str, Optional[str]]** | target keyword fields and target keywords optional field use this parameter to filter the dataset by keywords that certain fields should contain; fields you can specify: title, main_title, previous_title, snippet you can indicate several fields; Note: to match an exact phrase instead of a stand-alone keyword, use double quotes and backslashes; example: \&quot;keyword_fields\&quot;: {     \&quot;snippet\&quot;: \&quot;\\\&quot;logitech mouse\\\&quot;\&quot;,     \&quot;main_title\&quot;: \&quot;sale\&quot; } | [optional] 
**page_type** | **List[str]** | target page types optional field use this parameter to filter the dataset by page types possible values: \&quot;ecommerce\&quot;, \&quot;news\&quot;, \&quot;blogs\&quot;, \&quot;message-boards\&quot;, \&quot;organization\&quot; | [optional] 
**search_mode** | **str** | results grouping type optional field possible grouping types: as_is – returns data on all citations for the target keyword one_per_domain – returns data on one citation of the keyword per domain default value: as_is | [optional] 
**internal_list_limit** | **int** | maximum number of elements within internal arrays optional field you can use this field to limit the number of elements within the following arrays: top_domains text_categories page_categories countries languages default value: 1 maximum value: 20 | [optional] 
**date_from** | **str** | starting date of the time range required field date format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2019-01-15\&quot; | [optional] 
**date_to** | **str** | ending date of the time range optional field if you don’t specify this field, today’s date will be used by default date format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2019-01-15\&quot; | [optional] 
**date_group** | **str** | time range which will be used to group the results optional field default value: month possible values: day, week, month | [optional] 
**initial_dataset_filter** | **List[str]** | initial dataset filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, not_regex, &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, &#x3D;, &lt;&gt;, in, not_in, like,not_like, has, has_not, match, not_match you can use the % operator with like and not_like to match any string of zero or more characters example: [\&quot;domain\&quot;,\&quot;&lt;&gt;\&quot;, \&quot;logitech.com\&quot;] [[\&quot;domain\&quot;,\&quot;&lt;&gt;\&quot;,\&quot;logitech.com\&quot;],\&quot;and\&quot;,[\&quot;content_info.connotation_types.negative\&quot;,\&quot;&gt;\&quot;,1000]] [[\&quot;domain\&quot;,\&quot;&lt;&gt;\&quot;,\&quot;logitech.com\&quot;]], \&quot;and\&quot;, [[\&quot;content_info.connotation_types.negative\&quot;,\&quot;&gt;\&quot;,1000], \&quot;or\&quot;, [\&quot;content_info.text_category\&quot;,\&quot;has\&quot;,10994]]] for more information about filters, please refer to Content Analysis API – Filters | [optional] 
**rank_scale** | **str** | defines the scale used for calculating and displaying the rank values optional field you can use this parameter to choose whether rank values are presented on a 0–100 or 0–1000 scale possible values: one_hundred — rank values are displayed on a 0–100 scale one_thousand — rank values are displayed on a 0–1000 scale default value: one_thousand learn more about how this parameter works in this Help Center article | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.content_analysis_phrase_trends_live_request_info import ContentAnalysisPhraseTrendsLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentAnalysisPhraseTrendsLiveRequestInfo from a JSON string
content_analysis_phrase_trends_live_request_info_instance = ContentAnalysisPhraseTrendsLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(ContentAnalysisPhraseTrendsLiveRequestInfo.to_json())

# convert the object into a dict
content_analysis_phrase_trends_live_request_info_dict = content_analysis_phrase_trends_live_request_info_instance.to_dict()
# create an instance of ContentAnalysisPhraseTrendsLiveRequestInfo from a dict
content_analysis_phrase_trends_live_request_info_from_dict = ContentAnalysisPhraseTrendsLiveRequestInfo.from_dict(content_analysis_phrase_trends_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


