[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BusinessDataTripadvisorSearchTaskPostRequestInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword required field the keyword you specify should indicate a business category, company name, or a prominent place; you can specify up to 700 symbols in the keyword filed; all %## will be decoded (plus symbol ‘+’ will be decoded to a space character); if you need to use the “%” symbol for your keyword, please specify it as “%25” | [optional]
**location_name** | **str** | full name of search engine location required field if you don’t specify location_code you can receive the list of available locations with location_name by making a separate request to the https://api.dataforseo.com/v3/business_data/tripadvisor/locations example: London,England,United Kingdom | [optional]
**location_code** | **int** | search engine location code required field if you don’t specify location_name you can receive the list of available locations with location_code by making a separate request to the https://api.dataforseo.com/v3/business_data/tripadvisor/locations example: 1003854 | [optional]
**priority** | **int** | task priority optional field can take the following values: 1 – normal execution priority (set by default) 2 – high execution priority You will be additionally charged for the tasks with high execution priority. The cost can be calculated on the Pricing page. | [optional]
**depth** | **int** | parsing depth optional field number of search results to be returned from the API response we strongly recommend setting the parsing depth in the multiples of thirty because our systems processes thirty search results in a row; default value: 30; maximum value: 210 | [optional]
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional]
**postback_url** | **str** | return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/postbackscript?id&#x3D;$id http://your-server.com/postbackscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special symbols in postback_url will be urlencoded; i.a., the # symbol will be encoded into %23 | [optional]
**pingback_url** | **str** | notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/pingscript?id&#x3D;$id http://your-server.com/pingscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special symbols in pingback_url will be urlencoded; i.a., the # symbol will be encoded into %23 | [optional]

## Example

```python
from dataforseo_client.models.business_data_tripadvisor_search_task_post_request_info import BusinessDataTripadvisorSearchTaskPostRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataTripadvisorSearchTaskPostRequestInfo from a JSON string
business_data_tripadvisor_search_task_post_request_info_instance = BusinessDataTripadvisorSearchTaskPostRequestInfo.from_json(json)
# print the JSON string representation of the object
print BusinessDataTripadvisorSearchTaskPostRequestInfo.to_json()

# convert the object into a dict
business_data_tripadvisor_search_task_post_request_info_dict = business_data_tripadvisor_search_task_post_request_info_instance.to_dict()
# create an instance of BusinessDataTripadvisorSearchTaskPostRequestInfo from a dict
business_data_tripadvisor_search_task_post_request_info_form_dict = business_data_tripadvisor_search_task_post_request_info.from_dict(business_data_tripadvisor_search_task_post_request_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")