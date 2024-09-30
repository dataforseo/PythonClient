# MerchantAmazonReviewsTaskPostRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asin** | **str** | product ID required field unique product identifier (ASIN) on Amazon you can receive the asin parameter by making a separate request to the Amazon Products endpoint | [optional] 
**priority** | **int** | task priority optional field can take the following values: 1 – normal execution priority (set by default) 2 – high execution priority You will be additionally charged for the tasks with high execution priority. The cost can be calculated on the Pricing page. | [optional] 
**location_name** | **str** | full name of search engine location required field if you don’t specify location_code or location_coordinate if you use this field, you don’t need to specify location_code or location_coordinate you can receive the list of available locations with their location_name parameters by making a separate request to https://api.dataforseo.com/v3/merchant/amazon/locations example: HA1,England,United Kingdom | [optional] 
**location_code** | **int** | search engine location code required field if you don’t specify location_name or location_coordinate if you use this field, you don’t need to specify location_name or location_coordinate you can receive the list of available locations with their location_code parameters by making a separate request to https://api.dataforseo.com/v3/merchant/amazon/locations example: 9045969 | [optional] 
**location_coordinate** | **str** | GPS coordinates of a location required field if you don’t specify location_name or location_code if you use this field, you don’t need to specify location_name or location_code location_coordinate parameter should be specified in the “latitude,longitude,radius” format the maximum number of decimal digits for “latitude” and “longitude”: 7 the minimum value for “radius”: 199.9 example: 53.476225,-2.243572,200 | [optional] 
**language_name** | **str** | full name of search engine language required field if you don’t specify language_code if you use this field, you don’t need to specify language_code you can receive the list of available languages with their language_name parameters by making a separate request to https://api.dataforseo.com/v3/merchant/amazon/languages example: English (United Kingdom) | [optional] 
**language_code** | **str** | search engine language code required field if you don’t specify language_name if you use this field, you don’t need to specify language_name you can receive the list of available languages with their language_code parameters by making a separate request to https://api.dataforseo.com/v3/merchant/amazon/languages example: en_GB | [optional] 
**se_domain** | **str** | search engine domain optional field we choose the relevant search engine domain automatically according to the location and language you specify however, you can set a custom search engine domain in this field example: amazon.com, amazon.co.uk, amazon.fr, etc. | [optional] 
**depth** | **int** | parsing depth optional field number of reviews in SERP; we strongly recommend setting the parsing depth in the multiples of ten, because our system processes ten reviews in a row; maximum value: 50 default value: 10 | [optional] 
**sort_by** | **str** | results sorting parameters optional field you can use this field to sort the results; possible types of sorting: helpful — sort by helpful reviews; recent — sort by recent reviews; default rule: helpful | [optional] 
**reviewer_type** | **str** | filter reviews by reviewer type optional field you can use this field to filter the results; possible types of filtering: all_reviews — return reviews from all reviewers; avp_only_reviews — return reviews with the “Verified Purchase” mark only; default rule: all_reviews | [optional] 
**filter_by_star** | **str** | filter reviews by stars optional field you can use this field to filter the results; possible types of filtering: all_stars — return reviews with any number of stars; five_star — return five-star reviews only; four_star — return four-star reviews only; three_star — return three-star reviews only; two_star — return two-star reviews only; one_star — return one-star reviews only; positive — return positive reviews only; critical — return critical reviews only; default rule: all_stars | [optional] 
**filter_by_keyword** | **str** | filter reviews by specified keyword optional field you can specify up to 300 symbols in this field; if you use this field, the response will only include reviews that contain the specified keyword | [optional] 
**media_type** | **str** | filter reviews by media type optional field you can use this field to filter the results; possible types of filtering: all_contents — return text, image, and video reviews; media_reviews_only — return image and video reviews only; default rule: all_contents | [optional] 
**format_type** | **str** | filter reviews by product modification optional field you can use this field to filter the results; possible types of filtering: all_format — return reviews for all product modifications; current_format — return reviews for the current product modification only; default rule: all_format; Note: ASINs vary depending on a product modification. Thus, two modifications of the same product will have two different ASINs. Make sure to specify the right ASIN when setting a task with the current_format parameter | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 
**postback_url** | **str** | return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/postbackscript?id&#x3D;$id http://your-server.com/postbackscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special symbols in postback_url will be urlencoded; i.a., the # symbol will be encoded into %23 learn more on our Help Center | [optional] 
**postback_data** | **str** | postback_url datatype required field if you specify postback_url corresponds to the datatype that will be sent to your server possible values: advanced, html | [optional] 
**pingback_url** | **str** | notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/pingscript?id&#x3D;$id http://your-server.com/pingscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special symbols in pingback_url will be urlencoded; i.a., the # symbol will be encoded into %23 learn more on our Help Center | [optional] 

## Example

```python
from dataforseo_client.models.merchant_amazon_reviews_task_post_request_info import MerchantAmazonReviewsTaskPostRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantAmazonReviewsTaskPostRequestInfo from a JSON string
merchant_amazon_reviews_task_post_request_info_instance = MerchantAmazonReviewsTaskPostRequestInfo.from_json(json)
# print the JSON string representation of the object
print MerchantAmazonReviewsTaskPostRequestInfo.to_json()

# convert the object into a dict
merchant_amazon_reviews_task_post_request_info_dict = merchant_amazon_reviews_task_post_request_info_instance.to_dict()
# create an instance of MerchantAmazonReviewsTaskPostRequestInfo from a dict
merchant_amazon_reviews_task_post_request_info_form_dict = merchant_amazon_reviews_task_post_request_info.from_dict(merchant_amazon_reviews_task_post_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


