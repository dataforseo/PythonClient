# BacklinksBulkReferringDomainsLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**target** | **StrictStr** | <em>domain, subdomain or webpage from a POST array</em> |[optional]|
**referring_domains** | **StrictInt** | <em>number of referring domains pointing to the <code>target</code></em><br>note that we calculate main domains (root domains, like <code>example.com</code>) and their subdomains (e.g. <code>blog.example.com</code>) separately for this metric |[optional]|
**referring_domains_nofollow** | **StrictInt** | <em>number of domains pointing at least one nofollow link to the <code>target</code></em> |[optional]|
**referring_main_domains** | **StrictInt** | <em>number of referring main domains pointing to the <code>target</code></em><br>the number of primary (root) domains referring to your target |[optional]|
**referring_main_domains_nofollow** | **StrictInt** | <em>number of main domains pointing at least one nofollow link to the <code>target</code></em> |[optional]|