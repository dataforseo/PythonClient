# BacklinksDomainPagesLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**main_domain** | **StrictStr** | main website domain<br>main website domain does not include subdomains |[optional]|
**domain** | **StrictStr** | domain<br>domain where the page was found |[optional]|
**tld** | **StrictStr** | top-level domain<br>top-level domain in the DNS root zone |[optional]|
**page** | **StrictStr** | page URL<br>relevant page URL |[optional]|
**ip** | **StrictStr** | Internet Protocol address |[optional]|
**first_visited** | **StrictStr** | date and time of the first page visit<br>date and time when our crawler visited this page for the first time<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2017-01-24 13:20:59 +00:00 |[optional]|
**prev_visited** | **StrictStr** | previous to the most recent date when our crawler visited the page<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2017-01-24 13:20:59 +00:00 |[optional]|
**fetch_time** | **StrictStr** | most recent date and time when our crawler visited the page<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2017-01-24 13:20:59 +00:00 |[optional]|
**status_code** | **StrictInt** | HTTP status code of the page |[optional]|
**location** | **StrictStr** | location header<br>indicates the URL to redirect a page to if exists |[optional]|
**size** | **StrictInt** | indicates the page size, in bytes |[optional]|
**encoded_size** | **StrictInt** | page size after encoding<br>indicates the size of the encoded page, in bytes |[optional]|
**content_encoding** | **StrictStr** | type of encoding |[optional]|
**media_type** | **StrictStr** | types of media used to display a page |[optional]|
**server** | **StrictStr** | server version |[optional]|
**meta** | **BacklinksPageMeta** | page meta data |[optional]|
**page_summary** | **PageSummary** | contains backlink data for this page |[optional]|