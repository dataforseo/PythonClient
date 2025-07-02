# BacklinksBulkReferringDomainsLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**target** | **StrictStr** | domain, subdomain or webpage from a POST array |[optional]|
**referring_domains** | **StrictInt** | number of referring domains pointing to the target<br>note that we calculate main domains (root domains, like example.com) and their subdomains (e.g. blog.example.com) separately for this metric |[optional]|
**referring_domains_nofollow** | **StrictInt** | number of domains pointing at least one nofollow link to the target |[optional]|
**referring_main_domains** | **StrictInt** | number of referring main domains pointing to the target<br>the number of primary (root) domains referring to your target |[optional]|
**referring_main_domains_nofollow** | **StrictInt** | number of main domains pointing at least one nofollow link to the target |[optional]|