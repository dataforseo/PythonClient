[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# SerpGoogleOrganicLiveHtmlResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword received in a POST array keyword is returned with decoded %## (plus symbol ‘+’ will be decoded to a space character) | [optional]
**type** | **str** | type of element | [optional]
**se_domain** | **str** | search engine domain in a POST array | [optional]
**location_code** | **int** | location code in a POST array | [optional]
**language_code** | **str** | language code in a POST array | [optional]
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional]
**items_count** | **int** | the number of results returned in the items array | [optional]
**items** | [**List[HtmlItem]**](HtmlItem.md) | elements of search results found in SERP | [optional]

## Example

```python
from dataforseo_client.models.serp_google_organic_live_html_result_info import SerpGoogleOrganicLiveHtmlResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpGoogleOrganicLiveHtmlResultInfo from a JSON string
serp_google_organic_live_html_result_info_instance = SerpGoogleOrganicLiveHtmlResultInfo.from_json(json)
# print the JSON string representation of the object
print SerpGoogleOrganicLiveHtmlResultInfo.to_json()

# convert the object into a dict
serp_google_organic_live_html_result_info_dict = serp_google_organic_live_html_result_info_instance.to_dict()
# create an instance of SerpGoogleOrganicLiveHtmlResultInfo from a dict
serp_google_organic_live_html_result_info_form_dict = serp_google_organic_live_html_result_info.from_dict(serp_google_organic_live_html_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")