# KeywordsDataBingKeywordsForKeywordsLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | keyword in a POST array |[optional]|
**location_code** | **StrictInt** | location code in a POST array<br>if there is no data, then the value is null |[optional]|
**language_code** | **StrictStr** | language code in a POST array<br>if there is no data, then the value is null |[optional]|
**search_partners** | **StrictBool** | indicates whether data from partner networks is included in the response |[optional]|
**device** | **StrictStr** | device type<br>indicates for what device type the data is provided;<br>possible values: all, mobile, desktop, tablet |[optional]|
**competition** | **StrictFloat** | competition<br>represents the relative amount of competition associated with the given keyword in paid SERP only. This value is based on Bing Ads data.<br>Possible values: 0.1, 0.5,0.90.1 – low competition,<br>0.5 – medium competition,<br>0.9 – high competition;<br>if there is no data the value is null |[optional]|
**cpc** | **StrictFloat** | cost-per-click<br>represents the average cost per click (USD) historically paid for the keyword.<br>if there is no data, then the value is null |[optional]|
**search_volume** | **StrictInt** | monthly average search volume rate<br>represents the (approximate) number of searches for the keyword on the Bing search engine, depending on the user’s targetingsearch volume is rounded to the closest decimal values<br>if there is no data, then the value is null |[optional]|
**categories** | **List[Optional[StrictStr]]** | product and service categories<br>legacy field, the value will always be null |[optional]|
**monthly_searches** | **List[Optional[MonthlySearches]]** | monthly searches<br>represents the (approximate) number of searches on this keyword (as available for the past twelve months), targeted to the specified geographic locations.<br>if there is no data, then the value is null |[optional]|