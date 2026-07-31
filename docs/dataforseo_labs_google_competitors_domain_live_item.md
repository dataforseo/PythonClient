# DataforseoLabsGoogleCompetitorsDomainLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | <em>search engine type</em> |[optional]|
**domain** | **StrictStr** | <em>domain name</em> |[optional]|
**avg_position** | **StrictFloat** | <em>average position of the domain in SERP</em><br><strong>Note:</strong> average position is calculated for intersected keywords only;<br>the value for a given domain may differ when combined with different target websites |[optional]|
**sum_position** | **StrictInt** | <em>sum of all domain positions in SERP</em><br><strong>Note:</strong> average position is calculated for intersected keywords only;<br>the value for a given domain may differ when combined with different target websites |[optional]|
**intersections** | **StrictInt** | <em>number of intersecting keywords</em> |[optional]|
**full_domain_metrics** | **Dict[str, Optional[DataforseoLabsMetricsInfo]]** | <em>metrics for all keywords of the domain</em><br>full overview of ranking and traffic data relevant to all keywords that the provided <code>domain</code> is ranking for |[optional]|
**metrics** | **Dict[str, Optional[DataforseoLabsMetricsInfo]]** | <em>metrics for intersecting keywords</em><br>ranking and traffic data relevant to the keywords that the provided <code>domain</code> shares with the <code>target</code> domain<br><strong>note:</strong> in this array ranking and traffic data is provided for the <code>target</code> considering the keywords <code>target</code> shares in search with the competitor's <code>domain</code> |[optional]|
**competitor_metrics** | **Dict[str, Optional[DataforseoLabsMetricsInfo]]** | <em>metrics for intersecting keywords</em><br>ranking and traffic data relevant to the keywords that the provided <code>domain</code> shares with the <code>target</code> domain<br><strong>note:</strong> in this array ranking and traffic data is provided for the returned competitor's <code>domain</code> |[optional]|