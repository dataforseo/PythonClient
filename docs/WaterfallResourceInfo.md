# WaterfallResourceInfo

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**resource_type** | **string** |  |[optional]|
**url** | **string** | resource URL |[optional]|
**initiator** | **string** | resource initiator |[optional]|
**duration_time** | **number** | total time it takes until a browser receives a complete response from a server (in milliseconds) |[optional]|
**fetch_start** | **number** | time to start downloading the resource<br>the amount of time the browser needs to start downloading a resource |[optional]|
**fetch_end** | **number** | time to complete downloading the resource<br>the amount of time the browser needs to complete downloading a resource |[optional]|
**location** | **OnPageResourceLocationInfo** | location of the resource in the document<br>parameters defining the location of the specific resource within the document’s HTML |[optional]|
**is_render_blocking** | **boolean** | indicates whether the resource blocks rendering |[optional]|