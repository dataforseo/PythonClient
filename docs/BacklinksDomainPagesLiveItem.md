[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BacklinksDomainPagesLiveItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**main_domain** | **str** | main website domain main website domain does not include subdomains | [optional]
**domain** | **str** | domain domain where the page was found | [optional]
**tld** | **str** | top-level domain top-level domain in the DNS root zone | [optional]
**page** | **str** | page URL relevant page URL | [optional]
**ip** | **str** | Internet Protocol address | [optional]
**first_visited** | **str** | date and time of the first page visit date and time when our crawler visited this page for the first time in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2017-01-24 13:20:59 +00:00 | [optional]
**prev_visited** | **str** | previous to the most recent date when our crawler visited the page in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2017-01-24 13:20:59 +00:00 | [optional]
**fetch_time** | **str** | most recent date and time when our crawler visited the page in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2017-01-24 13:20:59 +00:00 | [optional]
**status_code** | **int** | HTTP status code of the page | [optional]
**location** | **str** | location header indicates the URL to redirect a page to if exists | [optional]
**size** | **int** | indicates the page size, in bytes | [optional]
**encoded_size** | **int** | page size after encoding indicates the size of the encoded page, in bytes | [optional]
**content_encoding** | **str** | type of encoding | [optional]
**media_type** | **str** | types of media used to display a page | [optional]
**server** | **str** | server version | [optional]
**meta** | [**BacklinksPageMeta**](BacklinksPageMeta.md) |  | [optional]
**page_summary** | [**PageSummary**](PageSummary.md) |  | [optional]

## Example

```python
from dataforseo_client.models.backlinks_domain_pages_live_item import BacklinksDomainPagesLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksDomainPagesLiveItem from a JSON string
backlinks_domain_pages_live_item_instance = BacklinksDomainPagesLiveItem.from_json(json)
# print the JSON string representation of the object
print BacklinksDomainPagesLiveItem.to_json()

# convert the object into a dict
backlinks_domain_pages_live_item_dict = backlinks_domain_pages_live_item_instance.to_dict()
# create an instance of BacklinksDomainPagesLiveItem from a dict
backlinks_domain_pages_live_item_form_dict = backlinks_domain_pages_live_item.from_dict(backlinks_domain_pages_live_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")