# BacklinksTimeseriesSummaryLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**date** | **StrictStr** | date and time when the data for the target was stored<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**rank** | **StrictInt** | target rank for the given date<br>learn more about the metric and how it is calculated in this help center article |[optional]|
**backlinks** | **StrictInt** | number of backlinks for the given date |[optional]|
**backlinks_nofollow** | **StrictInt** | number of nofollow backlinks for the given date |[optional]|
**referring_pages** | **StrictInt** | number of pages pointing to target for the given date |[optional]|
**referring_pages_nofollow** | **StrictInt** | number of referring pages pointing at least one nofollow link to the target for the given date |[optional]|
**referring_domains** | **StrictInt** | number of referring domains for the given date<br>referring domains include subdomains that are counted as separate domains for this metric |[optional]|
**referring_domains_nofollow** | **StrictInt** | number of domains pointing at least one nofollow link to the target for the given date |[optional]|
**referring_main_domains** | **StrictInt** | number of referring main domains for the given date |[optional]|
**referring_main_domains_nofollow** | **StrictInt** | number of main domains pointing at least one nofollow link to the target for the given date |[optional]|
**referring_ips** | **StrictInt** | number of referring IP addresses for the given date<br>number of IP addresses pointing to this page |[optional]|
**referring_subnets** | **StrictInt** | number of referring subnetworks for the given date |[optional]|