# KeywordsDataBingAudienceEstimationTaskGetResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**est_impressions** | **EstInfo** | monthly estimated impressions range |[optional]|
**est_audience_size** | **EstInfo** | monthly estimated reach user count range |[optional]|
**est_clicks** | **EstInfo** | monthly estimated click count range |[optional]|
**est_spend** | **EstInfo** | monthly estimated spending range |[optional]|
**est_cost_per_event** | **EstCInfo** | indicates the estimated cost per event with range result |[optional]|
**est_ctr** | **EstCInfo** | estimated click-through rate range |[optional]|
**suggested_bid** | **StrictFloat** | suggested bid value under the current targeting |[optional]|
**suggested_budget** | **StrictFloat** | suggested daily budget value under the current targeting and bid |[optional]|
**events_lost_to_bid** | **StrictInt** | indicates event lost count due to insufficient input bid |[optional]|
**events_lost_to_budget** | **StrictInt** | indicates the event lost count due to insufficient input budget |[optional]|
**est_reach_audience_size** | **StrictInt** | monthly estimated user count |[optional]|
**est_reach_impressions** | **StrictInt** | monthly estimated impressions |[optional]|
**currency** | **StrictStr** | currency name<br>example: USDollar |[optional]|