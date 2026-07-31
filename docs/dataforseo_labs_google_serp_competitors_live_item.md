# DataforseoLabsGoogleSerpCompetitorsLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | <em>search engine type</em> |[optional]|
**domain** | **StrictStr** | <em>domain name of the detected SERP competitor</em> |[optional]|
**avg_position** | **StrictFloat** | <em>the average position of the domain for the specified keywords</em><br>the arithmetic mean of values in the <code>keywords_positions</code> array |[optional]|
**median_position** | **StrictFloat** | <em>the median position of the domain for the specified keywords</em><br>the median of the values in the <code>keywords_positions</code> array |[optional]|
**rating** | **StrictFloat** | <em>the margin between the greatest possible and actual keyword positions</em><br>represents the relative visibility rate of the domain in SERP for the specified keywords<br>calculated as <em>sum(100-<code>keywords_positions</code>)</em> |[optional]|
**etv** | **StrictFloat** | <em>estimated traffic volume</em><br>represents the estimated monthly traffic that specified keywords are driving to the website<br>calculated as the sum of the products of the specified keywords' search volume values and CTR (click-through-rate) rates at certain positions in SERP<br>learn more about how the metric is calculated in <a href='https://dataforseo.com/help-center/how-is-etv-calculated' rel='noopener noreferrer' target='_blank'>this help center article</a> |[optional]|
**keywords_count** | **StrictInt** | <em>the number of specified keywords the domain has positions for in SERPs</em> |[optional]|
**visibility** | **StrictFloat** | <em>SERP visibility rate</em><br>represents the website visibility rate based on the SERP positions of the specified keywords<br>Keywords with positions in the range from <strong>1 to 10</strong> are assigned the visibility index from 1 to 0.1, respectively<br>Keywords with positions in the range from <strong>11 to 20</strong> have the fixed visibility index of 0.05<br>keywords with positions from <strong>20 to 100</strong> have the visibility index equal to 0 |[optional]|
**relevant_serp_items** | **StrictInt** | <em>the number of SERP elements relevant to the domain</em><br>represents the number of search results in SERP relevant to the domain for the specified keywords |[optional]|
**keywords_positions** | **Dict[str, Optional[List[Optional[StrictInt]]]]** | <em>keyword positions</em><br>SERP positions the related domain holds in SERP for the specified keywords |[optional]|