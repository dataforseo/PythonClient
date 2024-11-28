# OnPageLighthouseTaskPostRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | target URL required field target page should be specified with its absolute URL (including http:// or https://) example: https://dataforseo.com/ | [optional] 
**for_mobile** | **bool** | applies mobile emulation optional field if set to true, Lighthouse will use mobile device and screen emulation to test the page against mobile environment if set to false, the results will be provided for desktop default value: false | [optional] 
**categories** | **List[str]** | categories of Lighthouse audits optional field each category is a collection of audits and audit groups that applies weighting and scoring to the section (see official definition) if you ignore this field, we will return data for all categories unless you specify audits use this field to get data for specific categories you indicate here possible values: seo, pwa, performance, best_practices, accessibility | [optional] 
**audits** | **List[str]** | Lighthouse audits optional field audits are individual tests Lighthouse runs for each specific feature/optimization/metric to produce a numeric score (see official definition)   if you ignore this field, we will return data for all audits use this field to get data for specific audits you indicate here note that some audits do not belong to a specific category and are stand-alone page quality measurements in general, there can be several use cases: 1. if you ignore categories, you can use this field to get data for the specified audits only for example, if you ignore \&quot;categories\&quot; and specify \&quot;audits\&quot;: [\&quot;metrics/cumulative-layout-shift\&quot;,\&quot;metrics/largest-contentful-paint\&quot;,\&quot;metrics/total-blocking-time\&quot;], you will get data only for these audits 2. if you specify a category, you can use this field to additionally receive audits that do not belong to the category(-ies) you specified for example, if you specify \&quot;categories\&quot;: [\&quot;seo\&quot;] and \&quot;audits\&quot;: [\&quot;metrics/cumulative-layout-shift\&quot;,\&quot;metrics/largest-contentful-paint\&quot;,\&quot;metrics/total-blocking-time\&quot;], you will get only these audits under “performance” and all audits under “seo” you can get the full list of possible audits here | [optional] 
**version** | **str** | lighthouse version optional field you can obtain the results specific to a certain Lighthouse version by specifying its number the list of available versions is available through the Lighthouse Versions endpoint | [optional] 
**language_name** | **str** | lighthouse language name optional field you can receive the list of available languages of the search engine with their language_name by making a separate request to https://api.dataforseo.com/v3/on_page/lighthouse/languages default value: English | [optional] 
**language_code** | **str** | lighthouse language code optional field you can receive the list of available languages of the search engine with their language_code by making a separate request to https://api.dataforseo.com/v3/on_page/lighthouse/languages default value: en | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 
**pingback_url** | **str** | notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/pingscript?id&#x3D;$id http://your-server.com/pingscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special characters in pingback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center | [optional] 
**postback_url** | **str** | return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request example: http://your-server.com/postbackscript?id&#x3D;$id http://your-server.com/postbackscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special characters in postback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center | [optional] 

## Example

```python
from dataforseo_client.models.on_page_lighthouse_task_post_request_info import OnPageLighthouseTaskPostRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageLighthouseTaskPostRequestInfo from a JSON string
on_page_lighthouse_task_post_request_info_instance = OnPageLighthouseTaskPostRequestInfo.from_json(json)
# print the JSON string representation of the object
print(OnPageLighthouseTaskPostRequestInfo.to_json())

# convert the object into a dict
on_page_lighthouse_task_post_request_info_dict = on_page_lighthouse_task_post_request_info_instance.to_dict()
# create an instance of OnPageLighthouseTaskPostRequestInfo from a dict
on_page_lighthouse_task_post_request_info_from_dict = OnPageLighthouseTaskPostRequestInfo.from_dict(on_page_lighthouse_task_post_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


