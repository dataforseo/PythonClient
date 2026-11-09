# BaseOnPageResourceItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**resource_type** | **StrictStr** | type of element |[optional]|
**status_code** | **StrictInt** | general status codeyou can find the full list of the response codes hereNote: we strongly recommend designing a necessary system for handling related exceptional or error conditions |[optional]|
**location** | **StrictStr** | location headerindicates the URL to redirect a page to |[optional]|
**url** | **StrictStr** | page URL |[optional]|
**resource_errors** | **OnPageResourceIssueInfo** | resource errors and warnings |[optional]|
**size** | **StrictInt** | resource sizeindicates the size of a given page measured in bytes |[optional]|
**encoded_size** | **StrictInt** | page size after encodingindicates the size of the encoded page measured in bytes |[optional]|
**total_transfer_size** | **StrictInt** | compressed page sizeindicates the compressed size of a given page |[optional]|
**fetch_time** | **StrictStr** | date and time when a resource was fetchedin the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”example:2019-11-15 12:57:46 +00:00 |[optional]|
**cache_control** | **CacheControl** | instructions for caching |[optional]|
**checks** | **Dict[str, Optional[StrictBool]]** | website checkson-page check-ups related to the page |[optional]|
**content_encoding** | **StrictStr** | type of encoding |[optional]|
**media_type** | **StrictStr** | types of media used to display a page |[optional]|
**server** | **StrictStr** | server version |[optional]|
**last_modified** | **LastModified** | contains data on changes related to the resourceif there is no data, the value will be null |[optional]|