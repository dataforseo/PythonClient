# PageTiming


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_to_interactive** | **int** | Time To Interactive (TTI) metric the time it takes until the user can interact with a page (in milliseconds) | [optional] 
**dom_complete** | **int** | time to load resources the time it takes until the page and all of its subresources are downloaded (in milliseconds) | [optional] 
**largest_contentful_paint** | **float** | Core Web Vitals metric measuring how fast the largest above-the-fold content element is displayed The amount of time (in milliseconds) to render the largest content element visible in the viewport, from when the user requests the URL. Learn more. | [optional] 
**first_input_delay** | **float** | Core Web Vitals metric indicating the responsiveness of a page The time (in milliseconds) from when a user first interacts with your page to the time when the browser responds to that interaction. Learn more. | [optional] 
**connection_time** | **int** | time to connect to a server the time it takes until the connection with a server is established (in milliseconds) | [optional] 
**time_to_secure_connection** | **int** | time to establish a secure connection the time it takes until the secure connection with a server is established (in milliseconds) | [optional] 
**request_sent_time** | **int** | time to send a request to a server the time it takes until the request to a server is sent (in milliseconds) | [optional] 
**waiting_time** | **int** | time to first byte (TTFB) in milliseconds | [optional] 
**download_time** | **int** | time it takes for a browser to receive a response (in milliseconds) | [optional] 
**duration_time** | **int** | total time it takes until a browser receives a complete response from a server (in milliseconds) | [optional] 
**fetch_start** | **int** | time to start downloading the HTML resource the amount of time the browser needs to start downloading a page | [optional] 
**fetch_end** | **int** | time to complete downloading the HTML resource the amount of time the browser needs to complete downloading a page | [optional] 

## Example

```python
from dataforseo_client.models.page_timing import PageTiming

# TODO update the JSON string below
json = "{}"
# create an instance of PageTiming from a JSON string
page_timing_instance = PageTiming.from_json(json)
# print the JSON string representation of the object
print(PageTiming.to_json())

# convert the object into a dict
page_timing_dict = page_timing_instance.to_dict()
# create an instance of PageTiming from a dict
page_timing_form_dict = page_timing.from_dict(page_timing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


