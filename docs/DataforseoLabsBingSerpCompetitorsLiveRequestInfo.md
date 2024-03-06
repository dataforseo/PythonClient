[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# DataforseoLabsBingSerpCompetitorsLiveRequestInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keywords** | **List[str]** | keywords array required field the results will be based on the keywords you specify in this array UTF-8 encoding; the keywords will be converted to lowercase format; a keyword should be at least 3 characters long; you can specify the maximum of 200 keywords | [optional]
**location_name** | **str** | full name of the location required field if you don’t specify location_code Note: it is required to specify either location_name or location_code you can receive the list of available locations with location_name parameters by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; Note: this endpoint currently supports the US location only; example: United States | [optional]
**location_code** | **int** | unique location identifier required field if you don’t specify location_name Note: it is required to specify either location_name or location_code you can receive the list of available locations with their location_code parameters by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; Note: this endpoint currently supports the US location only; example: 2840 | [optional]
**language_name** | **str** | full name of the language required field if you don’t specify language_code Note: it is required to specify either language_name or language_code you can receive the list of available languages with their language_name parameters by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: English | [optional]
**language_code** | **str** | unique language identifier required field if you don’t specify language_name Note: it is required to specify either language_name or language_code you can receive the list of available languages with their language_code parameters by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: en | [optional]
**include_subdomains** | **bool** | indicates if the subdomains will be included in the search optional field if set to false, the subdomains will be ignored default value: true | [optional]
**item_types** | **List[str]** | search results type indicates type of search results included in the response optional field possible values: [\&quot;organic\&quot;, \&quot;paid\&quot;, \&quot;featured_snippet\&quot;, \&quot;local_pack\&quot;] default value: [\&quot;organic\&quot;, \&quot;paid\&quot;, \&quot;featured_snippet\&quot;, \&quot;local_pack\&quot;] | [optional]
**limit** | **int** | the maximum number of returned domains optional field default value: 100 maximum value: 1000 | [optional]
**offset** | **int** | offset in the results array of returned domains optional field default value: 0 if you specify the 10 value, the first ten domains in the results array will be omitted and the data will be provided for the successive domains | [optional]
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, &#x3D;, &lt;&gt;, in, not_in, like, not_like you can use the % operator with like and not_like to match any string of zero or more characters example: [\&quot;median_position\&quot;,\&quot;in\&quot;,[1,10]] [[\&quot;median_position\&quot;,\&quot;in\&quot;,[1,10]],\&quot;and\&quot;,[\&quot;domain\&quot;,\&quot;not_like\&quot;,\&quot;%wikipedia.org%\&quot;]] [[\&quot;domain\&quot;,\&quot;not_like\&quot;,\&quot;%wikipedia.org%\&quot;], \&quot;and\&quot;, [[\&quot;relevant_serp_items\&quot;,\&quot;&gt;\&quot;,0],\&quot;or\&quot;,[\&quot;median_position\&quot;,\&quot;in\&quot;,[1,10]]]] for more information about filters, please refer to Dataforseo Labs – Filters or this help center guide | [optional]
**order_by** | **List[str]** | results sorting rules optional field you can use the same values as in the filters array to sort the results possible sorting types: asc – results will be sorted in the ascending order desc – results will be sorted in the descending order the comma is used as a separator example: [\&quot;avg_position,asc\&quot;] default rule: [\&quot;rating,desc\&quot;] note that you can set no more than three sorting rules in a single request you should use a comma to separate several sorting rules example: [\&quot;avg_position,asc\&quot;,\&quot;etv,desc\&quot;] | [optional]
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional]

## Example

```python
from dataforseo_client.models.dataforseo_labs_bing_serp_competitors_live_request_info import DataforseoLabsBingSerpCompetitorsLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsBingSerpCompetitorsLiveRequestInfo from a JSON string
dataforseo_labs_bing_serp_competitors_live_request_info_instance = DataforseoLabsBingSerpCompetitorsLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsBingSerpCompetitorsLiveRequestInfo.to_json()

# convert the object into a dict
dataforseo_labs_bing_serp_competitors_live_request_info_dict = dataforseo_labs_bing_serp_competitors_live_request_info_instance.to_dict()
# create an instance of DataforseoLabsBingSerpCompetitorsLiveRequestInfo from a dict
dataforseo_labs_bing_serp_competitors_live_request_info_form_dict = dataforseo_labs_bing_serp_competitors_live_request_info.from_dict(dataforseo_labs_bing_serp_competitors_live_request_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")