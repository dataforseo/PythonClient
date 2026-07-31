# ClickstreamKeywordInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**search_volume** | **StrictInt** | average monthly search volume raterepresents the (approximate) number of searches for the given keyword idea on google.com |[optional]|
**last_updated_time** | **StrictStr** | date and time when keyword data was updatedin the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”example:2019-11-15 12:57:46 +00:00 |[optional]|
**gender_distribution** | **Dict[str, Optional[StrictInt]]** | distribution of estimated clickstream-based metrics by genderlearn more about how the metric is calculated in this help center article |[optional]|
**age_distribution** | **Dict[str, Optional[StrictInt]]** | distribution of clickstream-based metrics by agelearn more about how the metric is calculated in this help center article |[optional]|
**monthly_searches** | **List[Optional[MonthlySearchesInfo]]** | monthly searchesrepresents the (approximate) number of searches on this keyword idea (as available for the past twelve months), targeted to the specified geographic locations |[optional]|