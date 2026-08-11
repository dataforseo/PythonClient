# KeywordsDataGoogleAdsAdTrafficByKeywordsTaskGetResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | <em>keyword in a POST array</em><br>metrics are provided for all the keywords specified in the POST array |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em><br>if there is no data, then the value is_<code>null</code>n |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em><br>if there is no data, then the value is_<code>null</code>n |[optional]|
**date_interval** | **StrictStr** | <em>forecasting date interval in a POST array</em> |[optional]|
**search_partners** | **StrictBool** | <em>include Google search partners</em><br>the value is always <code>false</code> |[optional]|
**bid** | **StrictFloat** | <em>the maximum custom bid</em><br>the bid you have specified when setting the task<br>represents the price you are willing to pay for an ad<br>the higher value you have specified, the higher metrics and cost you receive in response<br>learn more in <a href='https://dataforseo.com/help-center/configuring-bid'>this help center article</a> |[optional]|
**match** | **StrictStr** | <em>keywords match-type</em><br>can take the following values: <code>exact</code>, <code>broad</code>, <code>phrase</code> |[optional]|
**impressions** | **StrictInt** | <em>projected number of ad impressions</em><br>number of impressions an ad is projected to get within the specified time period<br><strong>Note:</strong> parameter deprecated, the value is always_<code>null</code>n |[optional]|
**ctr** | **StrictFloat** | <em>projected clickthrough rate (CTR) of the advertisement</em><br>number of clicks an ad is projected to receive divided by the number of ad impressions;<br><strong>Note:</strong> parameter deprecated, the value is always <code>null</code> |[optional]|
**average_cpc** | **StrictFloat** | <em>the average cost-per-click value</em><br>represents the cost-per-click (USD) estimated for a keyword based on the specified time period and historical data;<br>if there is no data, then the value is_<code>null</code>n |[optional]|
**cost** | **StrictFloat** | <em>charge for an ad</em><br>amount that will be charged for running an ad within the specified time period<br>if there is no data, then the value is_<code>null</code>n |[optional]|
**clicks** | **StrictFloat** | <em>number of clicks on an ad</em><br>number of clicks an ad is projected to get within the specified time period<br>if there is no data, then the value is_<code>null</code>n |[optional]|