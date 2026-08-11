# BaseOnPageResourceItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**resource_type** | **StrictStr** | <em>type of the returned resource = <strong>'html'</strong></em> |[optional]|
**status_code** | **StrictInt** | <i>general status code</i><br>you can find the full list of the response codes <a href='/v3/appendix/errors'>here</a><br><strong>Note:</strong> we strongly recommend designing a necessary system for handling related exceptional or error conditions |[optional]|
**location** | **StrictStr** | <em>location header</em><br>indicates the URL to redirect a page to |[optional]|
**url** | **StrictStr** | <em>page URL</em> |[optional]|
**resource_errors** | **OnPageResourceIssueInfo** | <em>resource errors and warnings</em> |[optional]|
**size** | **StrictInt** | <em>resource size</em><br>indicates the size of a given page measured in bytes |[optional]|
**encoded_size** | **StrictInt** | <em>page size after encoding</em><br>indicates the size of the encoded page measured in bytes |[optional]|
**total_transfer_size** | **StrictInt** | <em>compressed page size</em><br>indicates the compressed size of a given page |[optional]|
**fetch_time** | **StrictStr** | <em>date and time when a resource was fetched</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**cache_control** | **CacheControl** | <em>instructions for caching</em> |[optional]|
**checks** | **Dict[str, Optional[StrictBool]]** | <em>website checks</em><br>on-page check-ups related to the page |[optional]|
**content_encoding** | **StrictStr** | <em>type of encoding</em> |[optional]|
**media_type** | **StrictStr** | <em>types of media used to display a page</em> |[optional]|
**server** | **StrictStr** | <em>server version</em> |[optional]|
**last_modified** | **LastModified** | <em>contains data on changes related to the resource</em><br>if there is no data, the value will be <code>null</code> |[optional]|