[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BacklinksSummaryLiveRequestInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | domain, subdomain or webpage to get data for required field a domain or a subdomain should be specified without https:// and www. a page should be specified with absolute URL (including http:// or https://) | [optional]
**include_subdomains** | **bool** | indicates if the subdomains of the target will be included in the search optional field if set to false, the subdomains will be ignored default value: true | [optional]
**include_indirect_links** | **bool** | indicates if indirect links to the target will be included in the results optional field if set to true, the results will include data on indirect links pointing to a page that either redirects to the target, or points to a canonical page if set to false, indirect links will be ignored default value: true | [optional]
**internal_list_limit** | **int** | maximum number of elements within internal arrays optional field you can use this field to limit the number of elements within the following arrays: referring_links_tld referring_links_types referring_links_attributes referring_links_platform_types referring_links_semantic_locations default value: 10 maximum value: 1000 | [optional]
**backlinks_status_type** | **str** | set what backlinks to return and count optional field you can use this field to choose what backlinks will be returned and used for aggregated metrics for your target; possible values: all – all backlinks will be returned and counted; live – backlinks found during the last check will be returned and counted; lost – lost backlinks will be returned and counted; default value: live | [optional]
**backlinks_filters** | **List[Optional[object]]** | filter the backlinks of your target optional field you can use this field to filter the initial backlinks that will be included in the dataset for aggregated metrics for your target you can filter the backlinks by all fields available in the response of this endpoint using this parameter, you can include only dofollow backlinks in the response and create a flexible backlinks dataset to calculate the metrics for example: \&quot;backlinks_filters\&quot;: [\&quot;dofollow\&quot;, \&quot;&#x3D;\&quot;, true] | [optional]
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional]

## Example

```python
from dataforseo_client.models.backlinks_summary_live_request_info import BacklinksSummaryLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksSummaryLiveRequestInfo from a JSON string
backlinks_summary_live_request_info_instance = BacklinksSummaryLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print BacklinksSummaryLiveRequestInfo.to_json()

# convert the object into a dict
backlinks_summary_live_request_info_dict = backlinks_summary_live_request_info_instance.to_dict()
# create an instance of BacklinksSummaryLiveRequestInfo from a dict
backlinks_summary_live_request_info_form_dict = backlinks_summary_live_request_info.from_dict(backlinks_summary_live_request_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")