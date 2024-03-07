[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# OnPagePagesResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crawl_progress** | **str** | status of the crawling session possible values: in_progress, finished | [optional]
**crawl_status** | [**CrawlStatusInfo**](CrawlStatusInfo.md) |  | [optional]
**total_items_count** | **int** | total number of relevant items in the database | [optional]
**items_count** | **int** | number of items in the results array | [optional]
**items** | [**List[BaseOnPageResourceItemInfo]**](BaseOnPageResourceItemInfo.md) | items array | [optional]

## Example

```python
from dataforseo_client.models.on_page_pages_result_info import OnPagePagesResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPagePagesResultInfo from a JSON string
on_page_pages_result_info_instance = OnPagePagesResultInfo.from_json(json)
# print the JSON string representation of the object
print OnPagePagesResultInfo.to_json()

# convert the object into a dict
on_page_pages_result_info_dict = on_page_pages_result_info_instance.to_dict()
# create an instance of OnPagePagesResultInfo from a dict
on_page_pages_result_info_form_dict = on_page_pages_result_info.from_dict(on_page_pages_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")