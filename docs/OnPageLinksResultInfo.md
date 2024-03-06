[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# OnPageLinksResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crawl_progress** | **str** | status of the crawling session possible values: in_progress, finished | [optional]
**crawl_status** | [**CrawlStatusInfo**](CrawlStatusInfo.md) |  | [optional]
**total_items_count** | **int** | total number of relevant items in the database | [optional]
**items_count** | **int** | number of items in the results array | [optional]
**items** | [**List[BaseOnPageLinkItemInfo]**](BaseOnPageLinkItemInfo.md) | items array | [optional]

## Example

```python
from dataforseo_client.models.on_page_links_result_info import OnPageLinksResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageLinksResultInfo from a JSON string
on_page_links_result_info_instance = OnPageLinksResultInfo.from_json(json)
# print the JSON string representation of the object
print OnPageLinksResultInfo.to_json()

# convert the object into a dict
on_page_links_result_info_dict = on_page_links_result_info_instance.to_dict()
# create an instance of OnPageLinksResultInfo from a dict
on_page_links_result_info_form_dict = on_page_links_result_info.from_dict(on_page_links_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")