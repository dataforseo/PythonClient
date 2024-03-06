[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# OnPagePageScreenshotResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crawl_progress** | **str** | status of the crawling session possible values: in_progress, finished | [optional]
**error_message** | **str** | error message if the url you indicated returns a 404 status code or is not a valid URL, you will obtain \&quot;error_message\&quot;:\&quot;Screenshot is empty\&quot; if no error is encountered, the value will be null | [optional]
**items_count** | **int** | number of items in the results array | [optional]
**items** | [**List[ScreenshotItem]**](ScreenshotItem.md) | items array | [optional]

## Example

```python
from dataforseo_client.models.on_page_page_screenshot_result_info import OnPagePageScreenshotResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPagePageScreenshotResultInfo from a JSON string
on_page_page_screenshot_result_info_instance = OnPagePageScreenshotResultInfo.from_json(json)
# print the JSON string representation of the object
print OnPagePageScreenshotResultInfo.to_json()

# convert the object into a dict
on_page_page_screenshot_result_info_dict = on_page_page_screenshot_result_info_instance.to_dict()
# create an instance of OnPagePageScreenshotResultInfo from a dict
on_page_page_screenshot_result_info_form_dict = on_page_page_screenshot_result_info.from_dict(on_page_page_screenshot_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")