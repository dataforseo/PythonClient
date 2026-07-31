# TargetInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**server** | **StrictStr** | <em>server</em> |[optional]|
**cms** | **StrictStr** | <em>content management system</em> |[optional]|
**platform_type** | **List[Optional[StrictStr]]** | <em>platform type</em> |[optional]|
**ip_address** | **StrictStr** | <em>IP address of the <code>target</code></em> |[optional]|
**country** | **StrictStr** | <em>country code that the <code>target</code> domain is determined to belong to</em> |[optional]|
**is_ip** | **StrictBool** | <em>indicates if the <code>target</code> is IP</em><br>if <code>true</code>, the domain, subdomain or webpage functions as an IP address and does not have a domain name |[optional]|
**target_spam_score** | **StrictInt** | <em>spam score of the <code>target</code></em><br>if the <code>target</code> is a domain/subdomain, this fields indicates the average spam score of all pages of that domain/subdomain;<br>learn more about how the metric is calculated on <a href='https://dataforseo.com/help-center/what-is-spam-score-and-how-is-it-calculated' rel='noopener noreferrer' target='_blank'>this help center page</a> |[optional]|