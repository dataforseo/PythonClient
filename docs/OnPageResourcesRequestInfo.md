# OnPageResourcesRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the task required field you can get this ID in the response of the Task POST endpoint example: “07131248-1535-0216-1000-17384017ad04” | [optional] 
**url** | **str** | page URL optional field specify this field if you want to get the resources for a specific page note that to obtain resource’s meta from a particular URL, you should specify the URL in this field; if you do not indicate a url when setting a task, resource’s meta in the results will be returned based on the data from the page where our crawler first saw the resource | [optional] 
**limit** | **int** | the maximum number of returned resources optional field default value: 100 maximum value: 1000 | [optional] 
**offset** | **int** | offset in the results array of returned resources optional field default value: 0 if you specify the 10 value, the first ten resources in the results array will be omitted and the data will be provided for the successive resources | [optional] 
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, &#x3D;, &lt;&gt;, in, not_in, like, not_like you can use the % operator with like and not_like to match any string of zero or more characters example: [\&quot;resource_type\&quot;,\&quot;&#x3D;\&quot;,\&quot;stylesheet\&quot;] [[\&quot;resource_type\&quot;,\&quot;&#x3D;\&quot;,\&quot;image\&quot;], \&quot;and\&quot;,[\&quot;checks.is_https\&quot;,\&quot;&#x3D;\&quot;,false]] [[\&quot;fetch_timing.duration_time\&quot;,\&quot;&gt;\&quot;,1],\&quot;and\&quot;,[[\&quot;total_transfer_size\&quot;,\&quot;&gt;\&quot;,100],\&quot;or\&quot;,[\&quot;checks.high_loading_time\&quot;,\&quot;&#x3D;\&quot;,true]]] The full list of possible filters is available by this link. | [optional] 
**relevant_pages_filters** | **List[str]** | filter the resources by relevant pages optional field you can use this field to obtain resources from pages matching to the defined parameters you can apply the same filters here as available for the pages endpoint you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, &#x3D;, &lt;&gt;, in, not_in, like, not_like you can use the % operator with like and not_like to match any string of zero or more characters example: [\&quot;checks.no_image_title\&quot;,\&quot;&#x3D;\&quot;,true] | [optional] 
**order_by** | **List[str]** | results sorting rules optional field you can use the same values as in the filters array to sort the results possible sorting types: asc – results will be sorted in the ascending order desc – results will be sorted in the descending order you should use a comma to set up a sorting type example: [\&quot;size,desc\&quot;] note that you can set no more than three sorting rules in a single request you should use a comma to separate several sorting rules example: [\&quot;size,desc\&quot;,\&quot;fetch_timing.fetch_end,desc\&quot;] | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.on_page_resources_request_info import OnPageResourcesRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageResourcesRequestInfo from a JSON string
on_page_resources_request_info_instance = OnPageResourcesRequestInfo.from_json(json)
# print the JSON string representation of the object
print(OnPageResourcesRequestInfo.to_json())

# convert the object into a dict
on_page_resources_request_info_dict = on_page_resources_request_info_instance.to_dict()
# create an instance of OnPageResourcesRequestInfo from a dict
on_page_resources_request_info_form_dict = on_page_resources_request_info.from_dict(on_page_resources_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


