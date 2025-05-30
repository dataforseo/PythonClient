# DataforseoLabsGoogleDomainWhoisOverviewLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | search engine type |[optional]|
**domain** | **StrictStr** | domain name |[optional]|
**created_datetime** | **StrictStr** | date and time of registration<br>date and time (in the ISO 8601 format) when the domain was first registered<br>example:<br>'1997-03-29 03:00:00 +00:00' |[optional]|
**changed_datetime** | **StrictStr** | date and time when the domain entry was changed<br>date and time (in the ISO 8601 format) when the domain entry was last modified<br>example:<br>'2021-01-14 08:36:28 +00:00' |[optional]|
**expiration_datetime** | **StrictStr** | date and time when the domain will expire<br>date and time (in the ISO 8601 format) when the domain is due to expire<br>example:<br>'2022-11-26 17:21:23 +00:00' |[optional]|
**updated_datetime** | **StrictStr** | date and time when the domain was updated<br>date and time (in the ISO 8601 format) when the domain was last updated<br>example:<br>'2021-01-29 13:59:38 +00:00' |[optional]|
**first_seen** | **StrictStr** | date and time when our crawler found the domain for the first time<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>'2019-11-15 12:57:46 +00:00' |[optional]|
**epp_status_codes** | **List[Optional[StrictStr]]** | extensive provisioning protocol status codes<br>the status of a domain name registration as defined by ICANN |[optional]|
**tld** | **StrictStr** | top-level domain<br>top-level domain in the DNS root zone |[optional]|
**registered** | **StrictBool** | domain registration status<br>if false, the domain name registration has expired<br>Note: expired domains will remain in the database for only a short period of time |[optional]|
**registrar** | **StrictStr** | domain registrar<br>if null, the domain registrar is unknown<br>example:<br>NameCheap, Inc. |[optional]|
**metrics** | **Dict[str, Optional[DataforseoLabsMetricsInfo]]** | ranking data relevant to the specified domain |[optional]|
**backlinks_info** | **BacklinksInfo** | backlink data for the returned domain |[optional]|