# BusinessDataTripadvisorReviewsTaskPostRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url_path** | **str** | URL path of the business entity required field if you do not specify keyword URL path to the Tripadvisor page of the business entity; can be found in the URL of the business entity on Tripadvisor example: Hotel_Review-g60763-d23462501-Reviews-Margaritaville_Times_Square-New_York_City_New_York.html https://www.tripadvisor.com/Hotel_Review-g60763-d23462501-Reviews-Margaritaville_Times_Square-New_York_City_New_York.html | [optional] 
**keyword** | **str** | keyword required field if you do not specify url_path the keyword you specify should indicate a name of an existing business or prominent place on Tripadvisor; you can specify up to 700 symbols in the keyword filed; all %## will be decoded (plus symbol ‘+’ will be decoded to a space character); if you need to use the “%” symbol for your keyword, please specify it as “%25” | [optional] 
**location_name** | **str** | full name of search engine location required field if you don’t specify location_code or url_path you can receive the list of available locations with location_name by making a separate request to the https://api.dataforseo.com/v3/business_data/tripadvisor/locations example: London,England,United Kingdom | [optional] 
**location_code** | **int** | search engine location code required field if you don’t specify location_name or url_path you can receive the list of available locations with location_code by making a separate request to the https://api.dataforseo.com/v3/business_data/tripadvisor/locations example: 1003854 | [optional] 
**priority** | **int** | task priority optional field can take the following values: 1 – normal execution priority (set by default) 2 – high execution priority You will be additionally charged for the tasks with high execution priority. The cost can be calculated on the Pricing page. | [optional] 
**language_name** | **str** | full name of search engine language optional field if you use this field, your account will be charged for one extra request you can receive the list of available languages with language_name by making a separate request to the https://api.dataforseo.com/v3/business_data/tripadvisor/languages example: English You will be additionally charged for setting a language parameter in this endpoint. The cost can be calculated on the Pricing page. | [optional] 
**language_code** | **str** | search engine language code optional field if you use this field, your account will be charged for one extra request you can receive the list of available languages with language_code by making a separate request to the https://api.dataforseo.com/v3/business_data/tripadvisor/languages example: en You will be additionally charged for setting a language parameter in this endpoint. The cost can be calculated on the Pricing page. | [optional] 
**depth** | **int** | parsing depth optional field number of reviews in SERP we strongly recommend setting the parsing depth in the multiples of ten, because our systems processes ten reviews in a row default value: 10 | [optional] 
**ratings** | **List[str]** | Tripadvisor traveler rating for a place of interest optional field rating based on the written reviews by a traveler after they visited a place. possible values: excellent, very_good, average, poor, terrible you can specify several values at once | [optional] 
**visit_type** | **List[str]** | filter by type of travelers who left a review optional field possible values: families, couples, solo, business, friends you can specify several values at once | [optional] 
**months** | **List[str]** | filter by months when a traveler made a visit optional field possible values: january, february, march, april, may, april, june, july, august, september, october, november, december you can specify several values at once | [optional] 
**search_reviews_keyword** | **str** | search reviews containing a specified keyword example: dessert | [optional] 
**sort_by** | **str** | results sorting parameters optional field you can use this field to sort the results; possible types of sorting: most_recent detailed_reviews | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 
**postback_url** | **str** | return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/postbackscript?id&#x3D;$id http://your-server.com/postbackscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special symbols in postback_url will be urlencoded; i.a., the # symbol will be encoded into %23 | [optional] 
**pingback_url** | **str** | notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/pingscript?id&#x3D;$id http://your-server.com/pingscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special symbols in pingback_url will be urlencoded; i.a., the # symbol will be encoded into %23 | [optional] 

## Example

```python
from dataforseo_client.models.business_data_tripadvisor_reviews_task_post_request_info import BusinessDataTripadvisorReviewsTaskPostRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataTripadvisorReviewsTaskPostRequestInfo from a JSON string
business_data_tripadvisor_reviews_task_post_request_info_instance = BusinessDataTripadvisorReviewsTaskPostRequestInfo.from_json(json)
# print the JSON string representation of the object
print(BusinessDataTripadvisorReviewsTaskPostRequestInfo.to_json())

# convert the object into a dict
business_data_tripadvisor_reviews_task_post_request_info_dict = business_data_tripadvisor_reviews_task_post_request_info_instance.to_dict()
# create an instance of BusinessDataTripadvisorReviewsTaskPostRequestInfo from a dict
business_data_tripadvisor_reviews_task_post_request_info_form_dict = business_data_tripadvisor_reviews_task_post_request_info.from_dict(business_data_tripadvisor_reviews_task_post_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


