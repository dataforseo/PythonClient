# WaterfallResourceInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**resource_type** | **StrictStr** |  |[optional]|
**url** | **StrictStr** | <em>resource URL</em> |[optional]|
**initiator** | **StrictStr** | <em>resource initiator</em> |[optional]|
**duration_time** | **StrictInt** | <em>total time it takes until a browser receives a complete response from a server (in milliseconds)</em> |[optional]|
**fetch_start** | **StrictInt** | <em>time to start downloading the HTML resource</em><br>the amount of time the browser needs to start downloading a page |[optional]|
**fetch_end** | **StrictInt** | <em>time to complete downloading the HTML resource</em><br>the amount of time the browser needs to complete downloading a page |[optional]|
**location** | **OnPageResourceLocationInfo** | <em>location of the resource in the document</em><br>parameters defining the location of the specific resource within the document's HTML |[optional]|
**is_render_blocking** | **StrictBool** | <em>indicates whether the resource blocks rendering</em> |[optional]|