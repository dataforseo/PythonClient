# BaseOnPageResourceItem

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**resource_type** | **string** | type of element |[optional]|
**status_code** | **number** | status code of the page |[optional]|
**location** | **string** | location header<br>indicates the URL to redirect a page to |[optional]|
**url** | **string** | page URL |[optional]|
**resource_errors** | **OnPageResourceIssueInfo** | resource errors and warnings |[optional]|
**size** | **number** | resource size<br>indicates the size of a given page measured in bytes |[optional]|
**encoded_size** | **number** | page size after encoding<br>indicates the size of the encoded page measured in bytes |[optional]|
**total_transfer_size** | **number** | compressed page size<br>indicates the compressed size of a given page |[optional]|
**fetch_time** | **string** | date and time when a resource was fetched<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**cache_control** | **CacheControl** | instructions for caching |[optional]|
**checks** | **{ [key: string]: boolean; }** | website checks<br>on-page check-ups related to the page |[optional]|
**content_encoding** | **string** | type of encoding |[optional]|
**media_type** | **string** | types of media used to display a page |[optional]|
**server** | **string** | server version |[optional]|
**last_modified** | **LastModified** | contains data on changes related to the resource<br>if there is no data, the value will be null |[optional]|