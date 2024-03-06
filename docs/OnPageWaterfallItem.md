[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# OnPageWaterfallItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_url** | **str** | URL of the page | [optional]
**time_to_interactive** | **int** | Time To Interactive (TTI) metric the time it takes until the user can interact with a page (in milliseconds) | [optional]
**dom_complete** | **int** | time to load resources the time it takes until the page and all of its subresources are downloaded (in milliseconds) | [optional]
**connection_time** | **int** | time to connect to a server the time it takes until the connection with a server is established (in milliseconds) | [optional]
**time_to_secure_connection** | **int** | time to establish a secure connection the time it takes until the secure connection with a server is established (in milliseconds) | [optional]
**request_sent_time** | **int** | time to send a request to a server the time it takes until the request to a server is sent (in milliseconds) | [optional]
**waiting_time** | **int** | time to first byte (TTFB) in milliseconds | [optional]
**download_time** | **int** | time it takes for a browser to receive a response (in milliseconds) | [optional]
**duration_time** | **int** | total time it takes until a browser receives a complete response from a server (in milliseconds) | [optional]
**fetch_start** | **int** | time to start downloading the HTML resource the amount of time the browser needs to start downloading a page | [optional]
**fetch_end** | **int** | time to complete downloading the HTML resource the amount of time the browser needs to complete downloading a page | [optional]
**resources** | [**List[BaseOnPageResourceItemInfo]**](BaseOnPageResourceItemInfo.md) | resource-specific timing contains separate arrays with timing for each resource found on the page | [optional]

## Example

```python
from dataforseo_client.models.on_page_waterfall_item import OnPageWaterfallItem

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageWaterfallItem from a JSON string
on_page_waterfall_item_instance = OnPageWaterfallItem.from_json(json)
# print the JSON string representation of the object
print OnPageWaterfallItem.to_json()

# convert the object into a dict
on_page_waterfall_item_dict = on_page_waterfall_item_instance.to_dict()
# create an instance of OnPageWaterfallItem from a dict
on_page_waterfall_item_form_dict = on_page_waterfall_item.from_dict(on_page_waterfall_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")