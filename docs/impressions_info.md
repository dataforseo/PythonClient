# ImpressionsInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | search engine type |[optional]|
**last_updated_time** | **StrictStr** | date and time when the clickstream dataset was updated<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” |[optional]|
**bid** | **StrictInt** | the maximum CPC<br>it stands for the price you are willing to pay for an ad. The higher value, the higher positions and price you will getwe return the results for the 999 bid value to provide the highest number of impressions and level down the account-specific factors |[optional]|
**match_type** | **StrictStr** | type of keyword match<br>can take the following values: exact, broad, phrase |[optional]|
**ad_position_min** | **StrictFloat** | the minimum ad position<br>represents the minimum position of the advertisement |[optional]|
**ad_position_max** | **StrictFloat** | the maximum ad position<br>represents the maximum position of the advertisement |[optional]|
**ad_position_average** | **StrictFloat** | the average ad position<br>represents the average position of the advertisement |[optional]|
**cpc_min** | **StrictFloat** | the minimum value of cost-per-click<br>the minimum cost-per-click (USD) for the keyword given that a bid is set to 999;<br>note: this field does not represent an actual CPC value;<br>you can find an actual CPC value for a keyword in the cpc field of the keyword_info object |[optional]|
**cpc_max** | **StrictFloat** | the maximum value of cost-per-click<br>the maximum cost-per-click (USD) for the keyword given that a bid is set to 999;<br>note: this field does not represent an actual CPC value;<br>you can find an actual CPC value for a keyword in the cpc field of the keyword_info object |[optional]|
**cpc_average** | **StrictFloat** | the average value of cost-per-click<br>the average cost-per-click (USD) for the keyword given that a bid is set to 999;<br>note: this field does not represent an actual CPC value;<br>you can find an actual CPC value for a keyword in the cpc field of the keyword_info object |[optional]|
**daily_impressions_min** | **StrictFloat** | the minimum value of daily impressions<br>represents the minimum number of daily impressions of the advertisement given that that a bid is set to 999; provides a more accurate alternative to Google search volume data |[optional]|
**daily_impressions_max** | **StrictFloat** | the maximum value of daily impressions<br>represents the maximum number of daily impressions of the advertisement given that that a bid is set to 999; provides a more accurate alternative to Google search volume data |[optional]|
**daily_impressions_average** | **StrictFloat** | the average value of daily impressions<br>represents the average number of daily impressions of the advertisement given that that a bid is set to 999; provides a more accurate alternative to Google search volume data |[optional]|
**daily_clicks_min** | **StrictFloat** | the minimum value of daily clicks<br>represents the minimum number of daily clicks on the advertisement |[optional]|
**daily_clicks_max** | **StrictFloat** | the maximum value of daily clicks<br>represents the maximum number of daily clicks on the advertisement |[optional]|
**daily_clicks_average** | **StrictFloat** | the average value of daily clicks<br>represents the average number of daily clicks on the advertisement |[optional]|
**daily_cost_min** | **StrictFloat** | the minimum daily charge value<br>represents the minimum daily cost of the advertisement (USD) |[optional]|
**daily_cost_max** | **StrictFloat** | the maximum daily charge value<br>represents the maximum daily cost of the advertisement (USD) |[optional]|
**daily_cost_average** | **StrictFloat** | the average daily charge value<br>represents the average daily cost of the advertisement (USD) |[optional]|