# OnPagePagesRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the task required field you can get this ID in the response of the Task POST endpoint example: “07131248-1535-0216-1000-17384017ad04” | [optional] 
**limit** | **int** | the maximum number of returned pages optional field default value: 100 maximum value: 1000 | [optional] 
**offset** | **int** | offset in the results array of returned pages optional field default value: 0 if you specify the 10 value, the first ten pages in the results array will be omitted and the data will be provided for the successive pages | [optional] 
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, not_regex, &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, &#x3D;, &lt;&gt;, in, not_in, like, not_like you can use the % operator with like and not_like to match any string of zero or more characters example: [\&quot;meta.external_links_count\&quot;,\&quot;&lt;&#x3D;\&quot;,50][\&quot;url\&quot;,\&quot;like\&quot;,\&quot;https://dataforseo.com/apis/dataforseo-labs-api\&quot;][[\&quot;checks.high_waiting_time\&quot;,\&quot;&#x3D;\&quot;,false], \&quot;and\&quot;,[\&quot;resource_type\&quot;,\&quot;&#x3D;\&quot;,\&quot;html\&quot;]][[\&quot;page_timing.duration_time\&quot;,\&quot;&lt;\&quot;,100],\&quot;and\&quot;,[[\&quot;checks.large_page_size\&quot;,\&quot;&#x3D;\&quot;,false],\&quot;or\&quot;,[\&quot;checks.high_waiting_time\&quot;,\&quot;&#x3D;\&quot;,false]]]The full list of possible filters is available by this link. | [optional] 
**order_by** | **List[str]** | results sorting rules optional field you can use the same values as in the filters array to sort the results possible sorting types: asc – results will be sorted in the ascending order desc – results will be sorted in the descending order you should use a comma to set up a sorting type example: [\&quot;meta.external_links_count,desc\&quot;] note that you can set no more than three sorting rules in a single request you should use a comma to separate several sorting rules example: [\&quot;page_timing.dom_complete,asc\&quot;,\&quot;size,desc\&quot;] | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.on_page_pages_request_info import OnPagePagesRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPagePagesRequestInfo from a JSON string
on_page_pages_request_info_instance = OnPagePagesRequestInfo.from_json(json)
# print the JSON string representation of the object
print OnPagePagesRequestInfo.to_json()

# convert the object into a dict
on_page_pages_request_info_dict = on_page_pages_request_info_instance.to_dict()
# create an instance of OnPagePagesRequestInfo from a dict
on_page_pages_request_info_form_dict = on_page_pages_request_info.from_dict(on_page_pages_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


