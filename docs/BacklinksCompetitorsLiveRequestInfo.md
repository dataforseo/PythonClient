[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BacklinksCompetitorsLiveRequestInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | domain, subdomain or webpage to get competitor domains for required field a domain or a subdomain should be specified without https:// and www. a page should be specified with absolute URL (including http:// or https://) | [optional]
**limit** | **int** | the maximum number of returned domains optional field default value: 100 maximum value: 1000 | [optional]
**offset** | **int** | offset in the results array of returned domains optional field default value: 0 if you specify the 10 value, the first ten domains in the results array will be omitted and the data will be provided for the successive pages | [optional]
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, &#x3D;, &lt;&gt;, in, not_in, like, not_like, ilike, not_ilike you can use the % operator with like and not_like to match any string of zero or more characters example: [\&quot;rank\&quot;,\&quot;&gt;\&quot;,\&quot;100\&quot;] [[\&quot;target\&quot;,\&quot;like\&quot;,\&quot;%forbes%\&quot;], \&quot;and\&quot;, [[\&quot;rank\&quot;,\&quot;&gt;\&quot;,\&quot;100\&quot;],\&quot;or\&quot;,[\&quot;intersections\&quot;,\&quot;&gt;\&quot;,\&quot;5\&quot;]]] The full list of possible filters is available here. | [optional]
**order_by** | **List[str]** | results sorting rules optional field you can use the same values as in the filters array to sort the results possible sorting types: asc – results will be sorted in the ascending order desc – results will be sorted in the descending order you should use a comma to set up a sorting type example: [\&quot;rank,desc\&quot;] note that you can set no more than three sorting rules in a single request you should use a comma to separate several sorting rules example: [\&quot;intersections,desc\&quot;,\&quot;rank,asc\&quot;] | [optional]
**main_domain** | **bool** | indicates if only main domain of the target will be included in the search optional field if set to true, only the main domain will be included in search; default value: true | [optional]
**exclude_large_domains** | **bool** | indicates whether large domain will appear in results optional field if set to true, the results from the large domain (google.com, amazon.com, etc.) will be omitted; default value: true | [optional]
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional]

## Example

```python
from dataforseo_client.models.backlinks_competitors_live_request_info import BacklinksCompetitorsLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksCompetitorsLiveRequestInfo from a JSON string
backlinks_competitors_live_request_info_instance = BacklinksCompetitorsLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print BacklinksCompetitorsLiveRequestInfo.to_json()

# convert the object into a dict
backlinks_competitors_live_request_info_dict = backlinks_competitors_live_request_info_instance.to_dict()
# create an instance of BacklinksCompetitorsLiveRequestInfo from a dict
backlinks_competitors_live_request_info_form_dict = backlinks_competitors_live_request_info.from_dict(backlinks_competitors_live_request_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")