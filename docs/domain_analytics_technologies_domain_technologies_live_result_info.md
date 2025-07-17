# DomainAnalyticsTechnologiesDomainTechnologiesLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**domain** | **StrictStr** | specified domain name |[optional]|
**title** | **StrictStr** | domain meta title |[optional]|
**description** | **StrictStr** | domain meta description |[optional]|
**meta_keywords** | **List[Optional[StrictStr]]** | domain meta keywords |[optional]|
**domain_rank** | **StrictInt** | backlink rank of the target domain<br>learn more about the metric and how it is calculated in this help center article |[optional]|
**last_visited** | **StrictStr** | most recent date when our crawler visited the domain<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2022-10-10 12:57:46 +00:00 |[optional]|
**country_iso_code** | **StrictStr** | domain ISO code<br>ISO code of the country that the target domain is determined to belong to |[optional]|
**language_code** | **StrictStr** | domain language<br>code of the language that the target domain is determined to be associated with |[optional]|
**content_language_code** | **StrictStr** | content language<br>code of the language that content on the target domain is written in |[optional]|
**phone_numbers** | **List[Optional[StrictStr]]** | phone numbers of the target<br>contact phone numbers indicated on the target website |[optional]|
**emails** | **List[Optional[StrictStr]]** | emails of the target<br>emails indicated on the target website |[optional]|
**social_graph_urls** | **List[Optional[StrictStr]]** | social media links and handles<br>social media URLs detected in the social graphs of the target website |[optional]|
**technologies** | **TechnologiesInfo** | technologies used by target domain<br>contains objects with the names of technologies used on the website<br>see the full list of available technologies structured by groups and categories |[optional]|