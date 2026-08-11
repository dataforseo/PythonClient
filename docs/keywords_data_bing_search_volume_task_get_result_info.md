# KeywordsDataBingSearchVolumeTaskGetResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | <em>keyword in a POST array</em> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em> |[optional]|
**search_partners** | **StrictBool** | <em>indicates whether data from partner networks included in the response</em> |[optional]|
**device** | **StrictStr** | <em>device type in a POST array</em><br>if there is no data, then the value is_<code>null</code>n |[optional]|
**competition** | **StrictFloat** | <em>competition</em><br>represents the relative amount of competition associated with the given keyword in paid SERP only. This value is based on Bing Ads data.<br>Possible values: <code>0.1</code>, <code>0.5</code>,<code>0.9</code> <p><code>0.1</code> - low competition,<br><code>0.5</code> - medium competition, <br><code>0.9</code> - high competition;<br>if there is no data the value is <code>null</code> |[optional]|
**cpc** | **StrictFloat** | <em>cost-per-click</em><br>represents the average cost per click (USD) historically paid for the keyword.<br>if there is no data then the value is_<code>null</code>n |[optional]|
**search_volume** | **StrictInt** | <em>monthly average search volume rate</em><br>search volume is rounded to the nearest tens |[optional]|
**categories** | **List[Optional[StrictStr]]** | <em>product and service categories</em><br>our API doesn't return categories for this endpoint: the parameter will always equal <code>null</code> |[optional]|
**monthly_searches** | **List[Optional[MonthlySearchesInfo]]** | <em>monthly searches</em><br>represents the (approximate) number of searches on this keyword idea (as available for the past twelve months), targeted to the specified geographic locations<br>if there is no data then the value is_<code>null</code>n |[optional]|