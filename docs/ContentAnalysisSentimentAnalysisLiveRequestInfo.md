# ContentAnalysisSentimentAnalysisLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | target keyword required field UTF-8 encoding a keyword should be at least 3 characters long; the keywords will be converted to a lowercase format; Note: to match an exact phrase instead of a stand-alone keyword, use double quotes and backslashes; example: \&quot;keyword\&quot;: \&quot;\\\&quot;tesla palo alto\\\&quot;\&quot; | [optional] 
**keyword_fields** | **Dict[str, Optional[str]]** | target keyword fields and target keywords optional field use this parameter to filter the dataset by keywords that certain fields should contain; fields you can specify: title, main_title, previous_title, snippet you can indicate several fields; Note: to match an exact phrase instead of a stand-alone keyword, use double quotes and backslashes; example: \&quot;keyword_fields\&quot;: {     \&quot;snippet\&quot;: \&quot;\\\&quot;logitech mouse\\\&quot;\&quot;,     \&quot;main_title\&quot;: \&quot;sale\&quot; } | [optional] 
**page_type** | **List[str]** | target page types optional field use this parameter to filter the dataset by page types possible values: \&quot;ecommerce\&quot;, \&quot;news\&quot;, \&quot;blogs\&quot;, \&quot;message-boards\&quot;, \&quot;organization\&quot; | [optional] 
**internal_list_limit** | **int** | maximum number of elements within internal arrays optional field you can use this field to limit the number of elements within the following arrays: top_domains text_categories page_categories countries languages default value: 1 maximum value: 20 | [optional] 
**positive_connotation_threshold** | **float** | positive connotation threshold optional field specified as the probability index threshold for positive sentiment related to the citation content if you specify this field, connotation_types object in the response will only contain data on citations with positive sentiment probability more than or equal to the specified value possible values: from 0 to 1 default value: 0.4 | [optional] 
**sentiments_connotation_threshold** | **float** | sentiment connotation threshold optional field specified as the probability index threshold for sentiment connotations related to the citation content if you specify this field, sentiment_connotations object in the response will only contain data on citations where the probability per each sentiment is more than or equal to the specified value possible values: from 0 to 1 default value: 0.4 | [optional] 
**initial_dataset_filters** | **List[Optional[object]]** | initial dataset filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, not_regex, &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, &#x3D;, &lt;&gt;, in, not_in, like,not_like, has, has_not you can use the % operator with like and not_like to match any string of zero or more characters example: [\&quot;domain\&quot;,\&quot;&lt;&gt;\&quot;, \&quot;logitech.com\&quot;] [[\&quot;domain\&quot;,\&quot;&lt;&gt;\&quot;,\&quot;logitech.com\&quot;],\&quot;and\&quot;,[\&quot;content_info.connotation_types.negative\&quot;,\&quot;&gt;\&quot;,1000]] [[\&quot;domain\&quot;,\&quot;&lt;&gt;\&quot;,\&quot;logitech.com\&quot;]], \&quot;and\&quot;, [[\&quot;content_info.connotation_types.negative\&quot;,\&quot;&gt;\&quot;,1000], \&quot;or\&quot;, [\&quot;content_info.text_category\&quot;,\&quot;has\&quot;,10994]]] for more information about filters, please refer to Content Analysis API – Filters | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.content_analysis_sentiment_analysis_live_request_info import ContentAnalysisSentimentAnalysisLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentAnalysisSentimentAnalysisLiveRequestInfo from a JSON string
content_analysis_sentiment_analysis_live_request_info_instance = ContentAnalysisSentimentAnalysisLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print ContentAnalysisSentimentAnalysisLiveRequestInfo.to_json()

# convert the object into a dict
content_analysis_sentiment_analysis_live_request_info_dict = content_analysis_sentiment_analysis_live_request_info_instance.to_dict()
# create an instance of ContentAnalysisSentimentAnalysisLiveRequestInfo from a dict
content_analysis_sentiment_analysis_live_request_info_form_dict = content_analysis_sentiment_analysis_live_request_info.from_dict(content_analysis_sentiment_analysis_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


