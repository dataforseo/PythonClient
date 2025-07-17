# DataforseoLabsleAppCompetitorsLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | search engine type |[optional]|
**app_id** | **StrictStr** | id of the competitor app |[optional]|
**avg_position** | **StrictFloat** | average position of the app in Google Play SERP<br>Note: average position is calculated for intersected keywords only;<br>the value for a given application may differ when combined with different target applications |[optional]|
**sum_position** | **StrictInt** | sum of all app positions in Google Play SERP<br>Note: sum position is calculated for intersected keywords only;<br>the value for a given application may differ when combined with different target applications |[optional]|
**intersections** | **StrictInt** | number of intersecting keywords |[optional]|
**competitor_metrics** | **Dict[str, Optional[AppMetricsInfo]]** | metrics for intersecting keywords<br>ranking data relevant to the keywords that the provided competitor application shares with the app in a POST request;<br>note: in this array ranking data is provided for the returned competitor’s app_id |[optional]|
**full_metrics** | **Dict[str, Optional[AppMetricsInfo]]** | metrics for all keywords of the application<br>full overview of ranking data relevant to all keywords that the provided app_id is ranking for |[optional]|