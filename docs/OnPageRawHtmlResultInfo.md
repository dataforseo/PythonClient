[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# OnPageRawHtmlResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crawl_progress** | **str** | status of the crawling session possible values: in_progress, finished | [optional]
**crawl_status** | [**CrawlStatusInfo**](CrawlStatusInfo.md) |  | [optional]
**items_count** | **int** | number of items in the results array | [optional]
**items** | [**OnPageRawHtmlItem**](OnPageRawHtmlItem.md) |  | [optional]

## Example

```python
from dataforseo_client.models.on_page_raw_html_result_info import OnPageRawHtmlResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageRawHtmlResultInfo from a JSON string
on_page_raw_html_result_info_instance = OnPageRawHtmlResultInfo.from_json(json)
# print the JSON string representation of the object
print OnPageRawHtmlResultInfo.to_json()

# convert the object into a dict
on_page_raw_html_result_info_dict = on_page_raw_html_result_info_instance.to_dict()
# create an instance of OnPageRawHtmlResultInfo from a dict
on_page_raw_html_result_info_form_dict = on_page_raw_html_result_info.from_dict(on_page_raw_html_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")