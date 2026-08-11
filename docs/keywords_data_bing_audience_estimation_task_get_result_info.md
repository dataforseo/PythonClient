# KeywordsDataBingAudienceEstimationTaskGetResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**est_impressions** | **AudienceEstimationInfo** | <em>monthly estimated impressions range</em> |[optional]|
**est_audience_size** | **AudienceEstimationInfo** | <em>monthly estimated reach user count range</em> |[optional]|
**est_clicks** | **AudienceEstimationInfo** | <em>monthly estimated click count range</em> |[optional]|
**est_spend** | **AudienceEstimationInfo** | <em>monthly estimated spending range</em> |[optional]|
**est_cost_per_event** | **AudienceEstimationInfo** | <em>indicates the estimated cost per event with range result</em> |[optional]|
**est_ctr** | **AudienceEstimationInfo** | <em>estimated click-through rate range</em> |[optional]|
**suggested_bid** | **StrictFloat** | <em>suggested bid value under the current targeting</em> |[optional]|
**suggested_budget** | **StrictFloat** | <em>suggested daily budget value under the current targeting and bid</em> |[optional]|
**events_lost_to_bid** | **StrictInt** | <em>indicates event lost count due to insufficient input bid</em> |[optional]|
**events_lost_to_budget** | **StrictInt** | <em>indicates the event lost count due to insufficient input budget</em> |[optional]|
**est_reach_audience_size** | **StrictInt** | <em>monthly estimated user count</em> |[optional]|
**est_reach_impressions** | **StrictInt** | <em>monthly estimated impressions</em> |[optional]|
**currency** | **StrictStr** | <em>currency name</em><p>example: <code>USDollar</code> |[optional]|