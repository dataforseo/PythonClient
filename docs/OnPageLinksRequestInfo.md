# OnPageLinksRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the task required field you can get this ID in the response of the Task POST endpoint example: “07131248-1535-0216-1000-17384017ad04” | [optional] 
**page_from** | **str** | relative page URL optional field if you use this field, the API response will contain only links from the specified page note that in this field you can specify relative URLs only | [optional] 
**page_to** | **str** | relative page URL optional field if you use this field, the API response will contain only internal links pointing to the specified page note that in this field you can specify relative URLs only | [optional] 
**limit** | **int** | the maximum number of returned links optional field default value: 100 maximum value: 1000 | [optional] 
**offset** | **int** | offset in the results array of returned links optional field default value: 0 if you specify the 10 value, the first ten links in the results array will be omitted and the data will be provided for the successive links | [optional] 
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, not_regex, &#x3D;, &lt;&gt;, in, not_in, like, not_like you can use the % operator with like and not_like to match any string of zero or more characters example: [\&quot;direction\&quot;,\&quot;&#x3D;\&quot;,\&quot;external\&quot;] [[\&quot;domain_to\&quot;,\&quot;&lt;&gt;\&quot;,\&quot;example.com\&quot;], \&quot;and\&quot;, [\&quot;link_from\&quot;,\&quot;not_like\&quot;,\&quot;%example.com/blog%\&quot;]] [[\&quot;direction\&quot;,\&quot;&#x3D;\&quot;,\&quot;external\&quot;], \&quot;and\&quot;, [[\&quot;link_from\&quot;,\&quot;like\&quot;,\&quot;%example.com/blog%\&quot;],\&quot;or\&quot;,[\&quot;link_from\&quot;,\&quot;like\&quot;,\&quot;%example.com/help%\&quot;]]] The full list of possible filters is available by this link. | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.on_page_links_request_info import OnPageLinksRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageLinksRequestInfo from a JSON string
on_page_links_request_info_instance = OnPageLinksRequestInfo.from_json(json)
# print the JSON string representation of the object
print(OnPageLinksRequestInfo.to_json())

# convert the object into a dict
on_page_links_request_info_dict = on_page_links_request_info_instance.to_dict()
# create an instance of OnPageLinksRequestInfo from a dict
on_page_links_request_info_from_dict = OnPageLinksRequestInfo.from_dict(on_page_links_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


