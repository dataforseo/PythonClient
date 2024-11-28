# MerchantGoogleProductsTaskPostRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword required field you can specify up to 700 characters in the keyword filed all %## will be decoded (plus character ‘+’ will be decoded to a space character) if you need to use the “%” character for your keyword, please specify it as “%25”; learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article | [optional] 
**url** | **str** | direct URL of the search query optional field you can specify a direct URL and we will sort it out to the necessary fields. Note that this method is the most difficult for our API to process and also requires you to specify the exact language and location in the URL. In most cases, we wouldn’t recommend using this method. Note: you may use the &amp;udm&#x3D;28 parameter in the direct URL to use the new Google Shopping markup with 40 SERP results returned by default (the cost for one SERP is deducted accordingly);the maximum depth is 200; this parameter must be specified without tbm&#x3D;shop ; example: https://www.google.com/search?q&#x3D;fish&amp;hl&#x3D;en&amp;gl&#x3D;US&amp;gws_rd&#x3D;cr&amp;uule&#x3D;w+CAIQIFISCQs2MuSEtepUEUK33kOSuTsc&amp;udm&#x3D;28 | [optional] 
**priority** | **int** | task priority optional field can take the following values: 1 – normal execution priority (set by default) 2 – high execution priority You will be additionally charged for the tasks with high execution priority. The cost can be calculated on the Pricing page. | [optional] 
**location_name** | **str** | full name of the location required field if you don’t specify location_code or location_coordinate if you use this field, you don’t need to specify location_code or location_coordinate you can receive the list of available Google Shopping locations with their location_name by making a separate request to the https://api.dataforseo.com/v3/merchant/google/locations example: London,England,United Kingdom | [optional] 
**location_code** | **int** | location code required field if you don’t specify location_name or location_coordinate if you use this field, you don’t need to specify location_name or location_coordinate you can receive the list of available Google Shopping locations with their location_code by making a separate request to the https://api.dataforseo.com/v3/merchant/google/locations example: 2840 | [optional] 
**location_coordinate** | **str** | GPS coordinates of a location required field if you don’t specify location_name or location_code if you use this field, you don’t need to specify location_name or location_code location_coordinate parameter should be specified in the “latitude,longitude,radius” format the maximum number of decimal digits for “latitude” and “longitude”: 7 the minimum value for “radius”: 199.9 example: 53.476225,-2.243572,200 | [optional] 
**language_name** | **str** | full name of the language required field if you don’t specify language_code if you use this field, you don’t need to specify language_code you can receive the list of available Google Shopping languages with their language_name by making a separate request to the https://api.dataforseo.com/v3/merchant/google/languages example: English | [optional] 
**language_code** | **str** | language code required field if you don’t specify language_name if you use this field, you don’t need to specify language_name you can receive the list of available Google Shopping languages with their language_code by making a separate request to the https://api.dataforseo.com/v3/merchant/google/languages example: en | [optional] 
**se_domain** | **str** | search engine domain optional field we choose the relevant search engine domain automatically according to the location and language you specify however, you can set a custom search engine domain in this field example: google.co.uk, google.com.au, google.de, etc. | [optional] 
**depth** | **int** | parsing depth optional field number of results to be retrieved from the Google Shopping results page default value: 100 max value: 700 Note: your account will be billed per each results page containing up to 100 results; thus, setting a depth above 100 may result in additional charges if the search engine returns more than 100 results; if the specified depth is higher than the number of results in the response, the difference will be refunded automatically to your account balance | [optional] 
**max_crawl_pages** | **int** | page crawl limit optional field number of search results pages to crawl max value: 7 Note: the max_crawl_pages and depth parameters complement each other; learn more at our help center | [optional] 
**search_param** | **str** | additional parameters of the search query optional field you can use the following search URL parameters for customizing the search; example: &amp;tbs&#x3D;ppr_min:45 – search for products that cost more than 45 USD; &amp;tbs&#x3D;ppr_max:50 – search for products that cost less than 50 USD; &amp;tbs&#x3D;p_ord:p – sort by ascending price; &amp;tbs&#x3D;p_ord:pd – sort by descending price; &amp;tbs&#x3D;p_ord:rv – sort by review score; &amp;tbs&#x3D;ppr_max:50,p_ord:rv – sort by review score with the maximum price of 50 USD.; &amp;udm&#x3D;28 – use new Google Shopping markup with 40 SERP results returned by default (the cost for one SERP is deducted accordingly);the maximum depth is 200; this parameter must be specified without tbm&#x3D;shop in the url; Note that search_param values will be ignored if any of the following parameters are used: price_min, price_max, sort_by | [optional] 
**price_min** | **int** | minimum product price optional field minimum price of the returned products listed on Google Shopping for the specified query example: 5 Note: if you specify price_min, the search_param parameter will be ignored | [optional] 
**price_max** | **int** | maximum product price optional field maximum price of the returned products listed on Google Shopping for the specified query example: 100 Note: if you specify price_max, the search_param parameter will be ignored | [optional] 
**sort_by** | **str** | results sorting rules optional field the following sorting rules are supported: review_score, price_low_to_high, price_high_to_low example: sort_by:\&quot;review_score\&quot; Note: if you specify sort_by, the search_param parameter will be ignored | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 
**postback_url** | **str** | return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/postbackscript?id&#x3D;$id http://your-server.com/postbackscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special characters in postback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center | [optional] 
**postback_data** | **str** | postback_url datatype required field if you specify postback_url corresponds to the datatype that will be sent to your server possible values: advanced, html | [optional] 
**pingback_url** | **str** | notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/pingscript?id&#x3D;$id http://your-server.com/pingscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special characters in pingback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center | [optional] 

## Example

```python
from dataforseo_client.models.merchant_google_products_task_post_request_info import MerchantGoogleProductsTaskPostRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantGoogleProductsTaskPostRequestInfo from a JSON string
merchant_google_products_task_post_request_info_instance = MerchantGoogleProductsTaskPostRequestInfo.from_json(json)
# print the JSON string representation of the object
print(MerchantGoogleProductsTaskPostRequestInfo.to_json())

# convert the object into a dict
merchant_google_products_task_post_request_info_dict = merchant_google_products_task_post_request_info_instance.to_dict()
# create an instance of MerchantGoogleProductsTaskPostRequestInfo from a dict
merchant_google_products_task_post_request_info_from_dict = MerchantGoogleProductsTaskPostRequestInfo.from_dict(merchant_google_products_task_post_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


