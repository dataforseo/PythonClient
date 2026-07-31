# DataforseoLabsleAppCompetitorsLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | <em>search engine type</em> |[optional]|
**app_id** | **StrictStr** | <em>id of the app in a POST array</em> |[optional]|
**avg_position** | **StrictFloat** | <em>average position of the app in Google Play SERP</em><br><strong>Note:</strong> average position is calculated for intersected keywords only;<br>the value for a given application may differ when combined with different target applications |[optional]|
**sum_position** | **StrictInt** | <em>sum of all app positions in Google Play SERP</em><br><strong>Note:</strong> sum position is calculated for intersected keywords only;<br>the value for a given application may differ when combined with different target applications |[optional]|
**intersections** | **StrictInt** | <em>number of intersecting keywords</em> |[optional]|
**competitor_metrics** | **Dict[str, Optional[AppMetricsInfo]]** | <em>metrics for intersecting keywords</em><br>ranking data relevant to the keywords that the provided competitor application shares with the app in a POST request;<br><strong>note:</strong> in this array ranking data is provided for the returned competitor's <code>app_id</code> |[optional]|
**full_metrics** | **Dict[str, Optional[AppMetricsInfo]]** | <em>metrics for all keywords of the application</em><br>full overview of ranking data relevant to all keywords that the provided <code>app_id</code> is ranking for |[optional]|