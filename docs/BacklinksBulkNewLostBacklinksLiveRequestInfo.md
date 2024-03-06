[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BacklinksBulkNewLostBacklinksLiveRequestInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**targets** | **List[str]** | domains, subdomains or webpages to get new &amp; lost backlinks for required field you can set up to 1000 domains, subdomains or webpages the domain or subdomain should be specified without https:// and www. the page should be specified with absolute URL (including http:// or https://) example: \&quot;targets\&quot;: [   \&quot;forbes.com\&quot;,   \&quot;cnn.com\&quot;,   \&quot;bbc.com\&quot;,   \&quot;yelp.com\&quot;,   \&quot;https://www.apple.com/iphone/\&quot;,   \&quot;https://ahrefs.com/blog/\&quot;,   \&quot;ibm.com\&quot;,   \&quot;https://variety.com/\&quot;,   \&quot;https://stackoverflow.com/\&quot;,   \&quot;www.trustpilot.com\&quot; ] | [optional]
**date_from** | **str** | starting date of the time range optional field this field indicates the date which will be used as a threshold for new and lost backlinks; the backlinks that appeared in our index after the specified date will be considered as new; the backlinks that weren’t found after the specified date, but were present before, will be considered as lost; default value: today’s date -(minus) one month; e.g. if today is 2021-10-13, default date_from will be 2021-09-13. minimum value equals today’s date -(minus) one year; e.g. if today is 2021-10-13, minimum date_from will be 2020-10-13. date format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2021-01-01\&quot; | [optional]
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional]

## Example

```python
from dataforseo_client.models.backlinks_bulk_new_lost_backlinks_live_request_info import BacklinksBulkNewLostBacklinksLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksBulkNewLostBacklinksLiveRequestInfo from a JSON string
backlinks_bulk_new_lost_backlinks_live_request_info_instance = BacklinksBulkNewLostBacklinksLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print BacklinksBulkNewLostBacklinksLiveRequestInfo.to_json()

# convert the object into a dict
backlinks_bulk_new_lost_backlinks_live_request_info_dict = backlinks_bulk_new_lost_backlinks_live_request_info_instance.to_dict()
# create an instance of BacklinksBulkNewLostBacklinksLiveRequestInfo from a dict
backlinks_bulk_new_lost_backlinks_live_request_info_form_dict = backlinks_bulk_new_lost_backlinks_live_request_info.from_dict(backlinks_bulk_new_lost_backlinks_live_request_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")