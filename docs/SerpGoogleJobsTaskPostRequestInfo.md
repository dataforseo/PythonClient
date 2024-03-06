[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# SerpGoogleJobsTaskPostRequestInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword required field you can specify up to 700 symbols in the keyword field all %## will be decoded (plus symbol ‘+’ will be decoded to a space character) if you need to use the “%” symbol for your keyword, please specify it as “%25”; if you need to use the “+” symbol for your keyword, please specify it as “%2B”; Note: the keyword you specify must indicate the job title; example: .net developer | [optional]
**priority** | **int** | task priority optional field can take the following values: 1 – normal execution priority (set by default); 2 – high execution priority You will be additionally charged for the tasks with high execution priority; The cost can be calculated on the Pricing page | [optional]
**location_name** | **str** | full name of search engine location required field if you don’t specify location_code if you use this field, you don’t need to specify location_code; you can receive the list of available locations of the search engine with their location_name by making a separate request to https://api.dataforseo.com/v3/serp/google/jobs/locations example: London,England,United Kingdom | [optional]
**location_code** | **int** | search engine location code required field if you don’t specify location_name; you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/serp/google/jobs/locations example: 2840 | [optional]
**location_radius** | **float** | location search radius optional field location search radius in kilometers; Note: for countries that use the imperial system of units, you will need to convert miles to kilometers by multiplying the value in miles by 1.609; if value is not specified, search is executed anywhere within the specified location; maximal value: 300 minimal value: &gt; 0 | [optional]
**language_name** | **str** | full name of search engine language required field if you don’t specify language_code if you use this field, you don’t need to specify language_code; you can receive the list of available languages of the search engine with their language_name by making a separate request to https://api.dataforseo.com/v3/serp/google/languages example: English | [optional]
**language_code** | **str** | search engine language code required field if you don’t specify language_name if you use this field, you don’t need to specify language_name; you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/languages example: en | [optional]
**depth** | **int** | parsing depth optional field number of results in SERP; default value: 10 max value: 200 Note: your account will be billed per each SERP containing up to 10 results; thus, setting the depth above 10 may result in additional charges if the search engine returns more than 10 results; if the specified depth is higher than the number of results in the response, the difference will be refunded automatically to your account balance | [optional]
**employment_type** | **List[str]** | employment contract type optional field type of employment contract for which the search results will be returned; possible values: fulltime, partime, contractor, intern | [optional]
**date_posted** | **str** | job posting date optional field you can use this field to filter job vacancies by posting date; possible values: today — return job vacancies posted today; 3days — return job vacancies posted no longer than 3 days ago; week — return job vacancies posted no longer than a week ago; month — return job vacancies posted no longer than a month ago | [optional]
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional]
**postback_url** | **str** | return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request example: http://your-server.com/postbackscript?id&#x3D;$id http://your-server.com/postbackscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special symbols in postback_url will be urlencoded; i.a., the # symbol will be encoded into %23 | [optional]
**postback_data** | **str** | postback_url datatype required field if you specify postback_url corresponds to the datatype that will be sent to your server possible values: regular, advanced, html | [optional]
**pingback_url** | **str** | notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/pingscript?id&#x3D;$id http://your-server.com/pingscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special symbols in pingback_url will be urlencoded; i.a., the # symbol will be encoded into %23 | [optional]

## Example

```python
from dataforseo_client.models.serp_google_jobs_task_post_request_info import SerpGoogleJobsTaskPostRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpGoogleJobsTaskPostRequestInfo from a JSON string
serp_google_jobs_task_post_request_info_instance = SerpGoogleJobsTaskPostRequestInfo.from_json(json)
# print the JSON string representation of the object
print SerpGoogleJobsTaskPostRequestInfo.to_json()

# convert the object into a dict
serp_google_jobs_task_post_request_info_dict = serp_google_jobs_task_post_request_info_instance.to_dict()
# create an instance of SerpGoogleJobsTaskPostRequestInfo from a dict
serp_google_jobs_task_post_request_info_form_dict = serp_google_jobs_task_post_request_info.from_dict(serp_google_jobs_task_post_request_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")