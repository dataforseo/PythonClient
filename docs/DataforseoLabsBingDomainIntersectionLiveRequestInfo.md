# DataforseoLabsBingDomainIntersectionLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target1** | **str** | domain required field the domain name of the first target website the domain should be specified without https:// and www. | [optional] 
**target2** | **str** | domain required field the domain name of the second target website the domain should be specified without https:// and www. | [optional] 
**location_name** | **str** | full name of the location required field if you don’t specify location_code Note: it is required to specify either location_name or location_code you can receive the list of available locations with their location_name by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; Note: this endpoint currently supports the US location only; example: United States | [optional] 
**location_code** | **int** | location code required field if you don’t specify location_name Note: it is required to specify either location_name or location_code you can receive the list of available locations with their location_code by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; Note: this endpoint currently supports the US location only; example: 2840 | [optional] 
**language_name** | **str** | full name of the language required field if you don’t specify language_code Note: it is required to specify either language_name or language_code you can receive the list of available languages with their language_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: English | [optional] 
**language_code** | **str** | language code required field if you don’t specify language_name Note: it is required to specify either language_name or language_code you can receive the list of available languages with their language_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: en | [optional] 
**intersections** | **bool** | domain intersections in SERP optional field if you set intersections to true, you will get the keywords for which both target domains specified as target1 and target2 have results within the same SERP; the corresponding SERP elements for both domains will be provided in the results array Note: this endpoint will not provide results if the number of intersecting keywords exceeds 10 million if you specify intersections: false, you will get the keywords for which the domain specified as target1 has results in SERP, and the domain specified as target2 doesn’t; thus, the corresponding SERP elements and other data will be provided for the domain specified as target1only default value: true | [optional] 
**item_types** | **List[str]** | search results type indicates type of search results included in the response optional field possible values: [\&quot;organic\&quot;, \&quot;paid\&quot;, \&quot;featured_snippet\&quot;, \&quot;local_pack\&quot;] default value: [\&quot;organic\&quot;, \&quot;paid\&quot;] | [optional] 
**include_serp_info** | **bool** | include data from SERP for each keyword optional field if set to true, we will return a serp_info array containing SERP data (number of search results, relevant URL, and SERP features) for every keyword in the response default value: false | [optional] 
**limit** | **int** | the maximum number of returned keywords optional field default value: 100 maximum value: 1000 | [optional] 
**offset** | **int** | offset in the items array of returned keywords optional field default value: 0 if you specify the 10 value, the first ten keywords in the results array will be omitted and the data will be provided for the successive keywords | [optional] 
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, not_regex, &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, &#x3D;, &lt;&gt;, in, not_in, ilike, not_ilike, like, not_like you can use the % operator with like and not_like, as well as ilike and not_ilike to match any string of zero or more characters example: [\&quot;keyword_data.keyword_info.search_volume\&quot;,\&quot;in\&quot;,[100,1000]] [[\&quot;first_domain_serp_element.etv\&quot;,\&quot;&gt;\&quot;,0],\&quot;and\&quot;,[\&quot;first_domain_serp_element.description\&quot;,\&quot;like\&quot;,\&quot;%goat%\&quot;]] [[\&quot;keyword_data.keyword_info.search_volume\&quot;,\&quot;&gt;\&quot;,100], \&quot;and\&quot;, [[\&quot;first_domain_serp_element.description\&quot;,\&quot;like\&quot;,\&quot;%goat%\&quot;], \&quot;or\&quot;, [\&quot;second_domain_serp_element.type\&quot;,\&quot;&#x3D;\&quot;,\&quot;organic\&quot;]]] for more information about filters, please refer to Dataforseo Labs – Filters or this help center guide | [optional] 
**order_by** | **List[str]** | results sorting rules optional field you can use the same values as in the filters array to sort the results possible sorting types: asc – results will be sorted in the ascending order desc – results will be sorted in the descending order you should use a comma to set up a sorting parameter example: [\&quot;keyword_data.keyword_info.competition,desc\&quot;] default rule: [\&quot;keyword_data.keyword_info.search_volume,desc\&quot;] note that you can set no more than three sorting rules in a single request you should use a comma to separate several sorting rules example: [\&quot;keyword_data.keyword_info.search_volume,desc\&quot;,\&quot;keyword_data.keyword_info.cpc,desc\&quot;] | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_bing_domain_intersection_live_request_info import DataforseoLabsBingDomainIntersectionLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsBingDomainIntersectionLiveRequestInfo from a JSON string
dataforseo_labs_bing_domain_intersection_live_request_info_instance = DataforseoLabsBingDomainIntersectionLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsBingDomainIntersectionLiveRequestInfo.to_json())

# convert the object into a dict
dataforseo_labs_bing_domain_intersection_live_request_info_dict = dataforseo_labs_bing_domain_intersection_live_request_info_instance.to_dict()
# create an instance of DataforseoLabsBingDomainIntersectionLiveRequestInfo from a dict
dataforseo_labs_bing_domain_intersection_live_request_info_from_dict = DataforseoLabsBingDomainIntersectionLiveRequestInfo.from_dict(dataforseo_labs_bing_domain_intersection_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


