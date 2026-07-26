# DomainAnalyticsWhoisOverviewLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**domain** | **StrictStr** | <em>domain name</em> |[optional]|
**created_datetime** | **StrictStr** | <em>date and time of registration</em><br>date and time (in the <a href='https://en.wikipedia.org/wiki/ISO_8601' rel='noopener noreferrer' target='_blank'>ISO 8601 format</a>) when the domain was first registered <br>example: <br><code>'1997-03-29 03:00:00 +00:00'</code> |[optional]|
**changed_datetime** | **StrictStr** | <em>date and time when the domain entry was changed</em><br>date and time (in the <a href='https://en.wikipedia.org/wiki/ISO_8601' rel='noopener noreferrer' target='_blank'>ISO 8601 format</a>) when the domain entry was last modified<br>example: <br><code>'2021-01-14 08:36:28 +00:00'</code> |[optional]|
**expiration_datetime** | **StrictStr** | <em>date and time when the domain will expire</em><br>date and time (in the <a href='https://en.wikipedia.org/wiki/ISO_8601' rel='noopener noreferrer' target='_blank'>ISO 8601 format</a>) when the domain is due to expire <br>example: <br><code>'2022-11-26 17:21:23 +00:00'</code> |[optional]|
**updated_datetime** | **StrictStr** | <em>date and time when the domain was updated</em><br>date and time (in the <a href='https://en.wikipedia.org/wiki/ISO_8601' rel='noopener noreferrer' target='_blank'>ISO 8601 format</a>) when the domain was last updated <br>example: <br><code>'2021-01-29 13:59:38 +00:00'</code> |[optional]|
**first_seen** | **StrictStr** | <em>date and time when our crawler found the domain for the first time</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example: <br><code>'2019-11-15 12:57:46 +00:00'</code> |[optional]|
**epp_status_codes** | **List[Optional[StrictStr]]** | <em>extensive provisioning protocol status codes</em><br>the status of a domain name registration <a href='https://www.icann.org/resources/pages/epp-status-codes-2014-06-16-en' rel='noopener noreferrer' target='_blank'>as defined by ICANN</a> |[optional]|
**tld** | **StrictStr** | <em>top-level domain</em><br>top-level domain in the <a href='https://www.iana.org/domains/root/db' rel='noopener noreferrer' target='_blank'>DNS root zone</a> |[optional]|
**registered** | **StrictBool** | <em>domain registration status</em><br>if <code>false</code>, the domain name registration has expired<br><strong>Note: expired domains will remain in the database for only a short period of time</strong> |[optional]|
**registrar** | **StrictStr** | <em>domain registrar</em><br>if <code>null</code>, the domain registrar is unknown<br>example:<br><code>NameCheap, Inc.</code> |[optional]|
**metrics** | **MetricsBundleInfo** | <em>ranking data relevant to the specified domain</em> |[optional]|
**backlinks_info** | **BacklinksInfo** | <em>backlink data for the returned domain</em> |[optional]|