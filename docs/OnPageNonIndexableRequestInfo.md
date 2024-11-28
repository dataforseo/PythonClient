# OnPageNonIndexableRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the task required field you can get this ID in the response of the Task POST endpoint example: “07131248-1535-0216-1000-17384017ad04” | [optional] 
**limit** | **int** | the maximum number of returned pages optional field default value: 100 maximum value: 1000 | [optional] 
**offset** | **int** | offset in the results array of returned pages optional field default value: 0 if you specify the 10 value, the first ten pages in the results array will be omitted and the data will be provided for the successive pages | [optional] 
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, not_regex, &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, &#x3D;, &lt;&gt;, in, not_in, like, not_like you can use the % operator with like and not_like to match any string of zero or more characters example: [\&quot;reason\&quot;,\&quot;&#x3D;\&quot;,\&quot;robots_txt\&quot;][[\&quot;reason\&quot;,\&quot;&lt;&gt;\&quot;,\&quot;robots_txt\&quot;], \&quot;and\&quot;, [\&quot;url\&quot;,\&quot;not_like\&quot;,\&quot;%/wp-admin/%\&quot;]] [[\&quot;url\&quot;,\&quot;not_like\&quot;,\&quot;%/wp-admin/%\&quot;], \&quot;and\&quot;, [[\&quot;reason\&quot;,\&quot;&lt;&gt;\&quot;,\&quot;meta_tag\&quot;],\&quot;or\&quot;,[\&quot;reason\&quot;,\&quot;&lt;&gt;\&quot;,\&quot;http_header\&quot;]]] The full list of possible filters is available by this link. | [optional] 

## Example

```python
from dataforseo_client.models.on_page_non_indexable_request_info import OnPageNonIndexableRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageNonIndexableRequestInfo from a JSON string
on_page_non_indexable_request_info_instance = OnPageNonIndexableRequestInfo.from_json(json)
# print the JSON string representation of the object
print(OnPageNonIndexableRequestInfo.to_json())

# convert the object into a dict
on_page_non_indexable_request_info_dict = on_page_non_indexable_request_info_instance.to_dict()
# create an instance of OnPageNonIndexableRequestInfo from a dict
on_page_non_indexable_request_info_from_dict = OnPageNonIndexableRequestInfo.from_dict(on_page_non_indexable_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


