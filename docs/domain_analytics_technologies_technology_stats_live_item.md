# DomainAnalyticsTechnologiesTechnologyStatsLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**date** | **StrictStr** | date for which the data is provided |[optional]|
**domains_count** | **StrictInt** | number of domains that use the specified technology |[optional]|
**countries** | **Dict[str, Optional[StrictInt]]** | distribution of websites by country<br>contains country codes and number of websites per country |[optional]|
**languages** | **Dict[str, Optional[StrictInt]]** | distribution of websites by language<br>contains language codes and number of websites per language |[optional]|
**domains_rank** | **Dict[str, Optional[StrictInt]]** | distribution of websites by backlink rank<br>contains domain rank ranges and number of websites per range<br>learn more about rank and how it is calculated in this help center article |[optional]|