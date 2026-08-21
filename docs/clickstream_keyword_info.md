# ClickstreamKeywordInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**search_volume** | **StrictInt** | <em>average monthly search volume rate</em><br>represents the (approximate) number of searches for the given keyword idea on google.com |[optional]|
**last_updated_time** | **StrictStr** | <em>date and time when keyword data was updated</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**gender_distribution** | **Dict[str, Optional[StrictInt]]** | <em>distribution of estimated clickstream-based metrics by gender</em><br>learn more about how the metric is calculated in this <a href='https://dataforseo.com/help-center/what-are-clickstream-based-metrics-and-how-do-we-calculate-them' rel='noopener noreferrer' target='_blank'>help center article</a> |[optional]|
**age_distribution** | **Dict[str, Optional[StrictInt]]** | <em>distribution of clickstream-based metrics by age</em><br>learn more about how the metric is calculated in this <a href='https://dataforseo.com/help-center/what-are-clickstream-based-metrics-and-how-do-we-calculate-them' rel='noopener noreferrer' target='_blank'>help center article</a> |[optional]|
**monthly_searches** | **List[Optional[MonthlySearchesInfo]]** | <em>monthly searches</em><br>represents the (approximate) number of searches on this keyword idea (as available for the past twelve months), targeted to the specified geographic locations |[optional]|