# BacklinksBulkSpamScoreLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**targets** | **List[str]** | domains, subdomains or webpages to get rank for required field you can set up to 1000 domains, subdomains or webpages the domain or subdomain should be specified without https:// and www. the page should be specified with absolute URL (including http:// or https://) example: \&quot;targets\&quot;: [   \&quot;forbes.com\&quot;,   \&quot;cnn.com\&quot;,   \&quot;bbc.com\&quot;,   \&quot;yelp.com\&quot;,   \&quot;https://www.apple.com/iphone/\&quot;,   \&quot;https://ahrefs.com/blog/\&quot;,   \&quot;ibm.com\&quot;,   \&quot;https://variety.com/\&quot;,   \&quot;https://stackoverflow.com/\&quot;,   \&quot;www.trustpilot.com\&quot; ] | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_bulk_spam_score_live_request_info import BacklinksBulkSpamScoreLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksBulkSpamScoreLiveRequestInfo from a JSON string
backlinks_bulk_spam_score_live_request_info_instance = BacklinksBulkSpamScoreLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print BacklinksBulkSpamScoreLiveRequestInfo.to_json()

# convert the object into a dict
backlinks_bulk_spam_score_live_request_info_dict = backlinks_bulk_spam_score_live_request_info_instance.to_dict()
# create an instance of BacklinksBulkSpamScoreLiveRequestInfo from a dict
backlinks_bulk_spam_score_live_request_info_form_dict = backlinks_bulk_spam_score_live_request_info.from_dict(backlinks_bulk_spam_score_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


