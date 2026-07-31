# BacklinksDomainPagesLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**main_domain** | **StrictStr** | <em>main website domain</em><br>main website domain does not include subdomains |[optional]|
**domain** | **StrictStr** | <em>domain</em><br>domain where the page was found |[optional]|
**tld** | **StrictStr** | <em>top-level domain</em><br>top-level domain in the <a href='https://www.iana.org/domains/root/db' rel='noopener noreferrer' target='_blank'>DNS root zone</a> |[optional]|
**page** | **StrictStr** | <em>page URL</em><br>relevant page URL |[optional]|
**ip** | **StrictStr** | <em>Internet Protocol address</em> |[optional]|
**first_visited** | **StrictStr** | <em>date and time of the first page visit</em><br>date and time when our crawler visited this page for the first time<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code>2017-01-24 13:20:59 +00:00</code> |[optional]|
**prev_visited** | **StrictStr** | <em>previous to the most recent date when our crawler visited the page</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code>2017-01-24 13:20:59 +00:00</code> |[optional]|
**fetch_time** | **StrictStr** | <em>most recent date and time when our crawler visited the page</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code>2017-01-24 13:20:59 +00:00</code> |[optional]|
**status_code** | **StrictInt** | <i>general status code</i><br>you can find the full list of the response codes <a href='/v3/appendix/errors'>here</a><br><strong>Note:</strong> we strongly recommend designing a necessary system for handling related exceptional or error conditions |[optional]|
**location** | **StrictStr** | <em>location header</em><br>indicates the URL to redirect a page to if exists |[optional]|
**size** | **StrictInt** | <em>indicates the page size, in bytes</em> |[optional]|
**encoded_size** | **StrictInt** | <em>page size after encoding</em><br>indicates the size of the encoded page, in bytes |[optional]|
**content_encoding** | **StrictStr** | <em>type of encoding</em> |[optional]|
**media_type** | **StrictStr** | <em>types of media used to display a page</em> |[optional]|
**server** | **StrictStr** | <em>server version</em> |[optional]|
**meta** | **BacklinksPageMeta** | <em>page meta data</em> |[optional]|
**page_summary** | **PageSummary** | <em>contains backlink data for this page</em> |[optional]|