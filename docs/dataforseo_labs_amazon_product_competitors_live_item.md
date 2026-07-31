# DataforseoLabsAmazonProductCompetitorsLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | <em>search engine type</em> |[optional]|
**asin** | **StrictStr** | <em>ASIN in a POST array</em> |[optional]|
**avg_position** | **StrictFloat** | <em>average position of the product in Amazon SERP</em><br><strong>Note:</strong> average position is calculated for intersected keywords only;<br>the value for a given product may differ when combined with different target products |[optional]|
**sum_position** | **StrictInt** | <em>sum of all product positions in Amazon SERP</em><br><strong>Note:</strong> average position is calculated for intersected keywords only;<br>the value for a given product may differ when combined with different target products |[optional]|
**intersections** | **StrictInt** | <em>number of intersecting keywords</em> |[optional]|
**competitor_metrics** | **AmazonMetricsBundleInfo** | <em>metrics for intersecting keywords</em><br>ranking data relevant to the keywords that the provided <code>asin</code> shares with the target <code>asin</code>;<br><strong>Note:</strong> in this object ranking data is provided for the returned competitor's <code>asin</code> |[optional]|
**full_metrics** | **AmazonMetricsBundleInfo** | <em>metrics for all keywords of the product</em><br>full overview of ranking data relevant to all keywords that the provided <code>asin</code> is ranking for |[optional]|