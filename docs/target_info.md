# TargetInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**server** | **StrictStr** | server |[optional]|
**cms** | **StrictStr** | content management system |[optional]|
**platform_type** | **List[Optional[StrictStr]]** | platform type |[optional]|
**ip_address** | **StrictStr** | IP address of the target |[optional]|
**country** | **StrictStr** | country code that the target domain is determined to belong to |[optional]|
**is_ip** | **StrictBool** | indicates if the target is IP<br>if true, the domain, subdomain or webpage functions as an IP address and does not have a domain name |[optional]|
**target_spam_score** | **StrictInt** | spam score of the target<br>if the target is a domain/subdomain, this fields indicates the average spam score of all pages of that domain/subdomain;<br>learn more about how the metric is calculated on this help center page |[optional]|