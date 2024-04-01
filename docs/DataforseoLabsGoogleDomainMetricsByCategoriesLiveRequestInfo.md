# DataforseoLabsGoogleDomainMetricsByCategoriesLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_codes** | **List[str]** | product and service categories required field The maximum number of categories you can specify: 5 you can download the full list of possible categories | [optional] 
**first_date** | **str** | first date of comparison period required field first date for which domain metrics will be provided; date format: \&quot;yyyy-mm-dd\&quot;; example: \&quot;2021-06-01\&quot;; the list available dates is available through the available history endpoint; Note: first_date cannot be greater than today’s date; Also note: the dates specified in first_date and second_date cannot point to the same month of the same year; you can specify the dates in any order: first_date can be greater than second_date and vice versa; minimum date: \&quot;2020-10-01\&quot; | [optional] 
**second_date** | **str** | second date of comparison period required field second date for which domain metrics will be provided; date format: \&quot;yyyy-mm-dd\&quot;; example: \&quot;2021-10-01\&quot;; the list available dates is available through the available history endpoint; Note: second_date cannot be greater than today’s date; Also note: the dates specified in first_date and second_date cannot point to the same month of the same year; you can specify the dates in any order: second_date can be greater than first_date and vice versa; minimum date: \&quot;2020-10-01\&quot; | [optional] 
**location_name** | **str** | full name of the location required field if you don’t specify location_code Note: it is required to specify either location_name or location_code; you can receive the list of available locations with their location_name by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; example: United Kingdom | [optional] 
**location_code** | **int** | unique location identifier required field if you don’t specify location_name Note: it is required to specify either location_name or location_code; you can receive the list of available locations with their location_code by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; example: 2840 | [optional] 
**language_name** | **str** | full name of the language required field if you don’t specify language_code Note: it is required to specify either language_name or language_code; you can receive the list of available languages with their language_name by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; example: English | [optional] 
**language_code** | **str** | unique language identifier required field if you don’t specify language_name Note: it is required to specify either language_name or language_code; you can receive the list of available languages with their language_code by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; example: en | [optional] 
**item_types** | **List[str]** | display results by item type optional field indicates the type of search results included in the response; Note: if the item_types array contains item types that are different from the organic object, the results will be ordered by the first item type in the array; you will not be able to sort and filter results by the types of search results not included in the response; possible values: [\&quot;organic\&quot;, \&quot;paid\&quot;, \&quot;featured_snippet\&quot;, \&quot;local_pack\&quot;]; default value: [\&quot;organic\&quot;, \&quot;paid\&quot;] | [optional] 
**top_categories_count** | **int** | number of additional domain categories optional field by using this parameter, you can receive domains relevant to additional categories that are not specified in category_codes above; to learn more about the parameter, please refer to this help center article; by default, top_categories_count is equal to the number of categories specified in the category_codes array; Note: top_categories_count cannot be less than the number of categories in the category_codes array; maximum value: 5 | [optional] 
**include_subdomains** | **bool** | return subdomains in the API response optional field if false, the API response will contain main_domain only; if true, the API will return main_domain plus its subdomains (if available); default value: true | [optional] 
**etv_min** | **int** | minimum current organic ETV of the domain optional field if specified, the API will return only domains with organic_etv greater than the specified value | [optional] 
**etv_max** | **int** | maximum current organic ETV of the domain optional field if specified, the API will return only domains with organic_etv lesser than the specified value | [optional] 
**correlate** | **bool** | correlate data with previously obtained datasets optional field default value: true; if you use this parameter, our system will correlate data you obtain now with previously obtained datasets; this parameter is intended to mitigate any inconsistencies that may result from changes to our database; Note: we do not recommend setting correlate to false | [optional] 
**limit** | **int** | the maximum number of domains in the results array optional field default value: 100; maximum value: 1000 | [optional] 
**offset** | **int** | offset in the results array of returned domains optional field default value: 0; if you specify the 10 value, the first ten domains in the results array will be omitted and the data will be provided for the successive domains | [optional] 
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum); you should set a logical operator and, or between the conditions the following operators are supported: regex, &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, &#x3D;, &lt;&gt;, in, not_in, like, not_like; you can use the % operator with like and not_like to match any string of zero or more characters; example: [\&quot;metrics_history.202110.organic.pos_1\&quot;, \&quot;&gt;\&quot;, 15]; for more information about filters, please refer to Dataforseo Labs – Filters or this help center guide | [optional] 
**order_by** | **List[str]** | results sorting rules optional field you can use the same values as in the filters array to sort the results; default rule: [\&quot;organic_etv,desc\&quot;]; possible sorting types: asc – results will be sorted in ascending order desc – results will be sorted in descending order; you should use a comma to set up a sorting type; example: [\&quot;organic_count,desc\&quot;]; note that you can set no more than three sorting rules in a single request; you should use a comma to separate several sorting rules; example: [\&quot;organic_etv,desc\&quot;,\&quot;organic_count,asc\&quot;] | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255; you can use this parameter to identify the task and match it with the result; you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_domain_metrics_by_categories_live_request_info import DataforseoLabsGoogleDomainMetricsByCategoriesLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleDomainMetricsByCategoriesLiveRequestInfo from a JSON string
dataforseo_labs_google_domain_metrics_by_categories_live_request_info_instance = DataforseoLabsGoogleDomainMetricsByCategoriesLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsGoogleDomainMetricsByCategoriesLiveRequestInfo.to_json())

# convert the object into a dict
dataforseo_labs_google_domain_metrics_by_categories_live_request_info_dict = dataforseo_labs_google_domain_metrics_by_categories_live_request_info_instance.to_dict()
# create an instance of DataforseoLabsGoogleDomainMetricsByCategoriesLiveRequestInfo from a dict
dataforseo_labs_google_domain_metrics_by_categories_live_request_info_form_dict = dataforseo_labs_google_domain_metrics_by_categories_live_request_info.from_dict(dataforseo_labs_google_domain_metrics_by_categories_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


