# WaterfallResourceInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**resource_type** | **StrictStr** |  |[optional]|
**url** | **StrictStr** | resource URL |[optional]|
**initiator** | **StrictStr** | resource initiator |[optional]|
**duration_time** | **StrictFloat** | total time it takes until a browser receives a complete response from a server (in milliseconds) |[optional]|
**fetch_start** | **StrictFloat** | time to start downloading the resource<br>the amount of time the browser needs to start downloading a resource |[optional]|
**fetch_end** | **StrictFloat** | time to complete downloading the resource<br>the amount of time the browser needs to complete downloading a resource |[optional]|
**location** | **OnPageResourceLocationInfo** | location of the resource in the document<br>parameters defining the location of the specific resource within the document’s HTML |[optional]|
**is_render_blocking** | **StrictBool** | indicates whether the resource blocks rendering |[optional]|