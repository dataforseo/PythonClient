# OnPageRedirectChainsRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the task required field you can get this ID in the response of the Task POST endpoint example: “07131248-1535-0216-1000-17384017ad04” | [optional] 
**url** | **str** | page URL optional field absolute URL of the target page if you use this field, the API response will return only redirect chains which contain the specified URL | [optional] 
**limit** | **int** | the maximum number of returned redirect chains optional field default value: 100 maximum value: 1000 | [optional] 
**offset** | **int** | offset in the results array of returned redirect chains optional field default value: 0 if you specify the 10 value, the first ten redirect chains in the results array will be omitted and the data will be provided for the successive redirect chains | [optional] 
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can use only one filtering parameter with this endpoint the following filtering parameter is supported: is_redirect_loop the following operators are supported: regex, &#x3D;, &lt;&gt; examples: [\&quot;is_redirect_loop\&quot;,\&quot;&#x3D;\&quot;,\&quot;true\&quot;] [\&quot;is_redirect_loop\&quot;,\&quot;&lt;&gt;\&quot;,\&quot;false\&quot;] | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.on_page_redirect_chains_request_info import OnPageRedirectChainsRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageRedirectChainsRequestInfo from a JSON string
on_page_redirect_chains_request_info_instance = OnPageRedirectChainsRequestInfo.from_json(json)
# print the JSON string representation of the object
print OnPageRedirectChainsRequestInfo.to_json()

# convert the object into a dict
on_page_redirect_chains_request_info_dict = on_page_redirect_chains_request_info_instance.to_dict()
# create an instance of OnPageRedirectChainsRequestInfo from a dict
on_page_redirect_chains_request_info_form_dict = on_page_redirect_chains_request_info.from_dict(on_page_redirect_chains_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


