# DomainAnalyticsTechnologiesTechnologyStatsLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**date** | **StrictStr** | <em>date for which the data is provided</em> |[optional]|
**domains_count** | **StrictInt** | <em>number of domains that use the specified technology</em> |[optional]|
**countries** | **Dict[str, Optional[StrictInt]]** | <em>distribution of websites by country</em><br>contains country codes and number of websites per country |[optional]|
**languages** | **Dict[str, Optional[StrictInt]]** | <em>distribution of websites by language</em><br>contains language codes and number of websites per language |[optional]|
**domains_rank** | **Dict[str, Optional[StrictInt]]** | <em>distribution of websites by backlink rank</em><br>contains domain rank ranges and number of websites per range<br>learn more about rank and how it is calculated in <a href='https://dataforseo.com/help-center/what_is_rank_in_backlinks_api' rel='noopener noreferrer' target='_blank'>this help center article</a> |[optional]|