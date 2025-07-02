# KeywordsDataBingSearchVolumeLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | keyword in a POST array |[optional]|
**location_code** | **StrictInt** | location code in a POST array<br>if there is no data, then the value is null |[optional]|
**language_code** | **StrictStr** | language code in a POST array<br>if there is no data, then the value is null |[optional]|
**search_partners** | **StrictBool** | indicates whether data from partner networks included in the response |[optional]|
**device** | **StrictStr** | device type in a POST array<br>if there is no data, then the value is null |[optional]|
**competition** | **StrictFloat** | competition<br>represents the relative amount of competition associated with the given keyword in paid SERP only. This value is based on Bing Ads data.<br>Possible values: 0.1, 0.5,0.90.1 – low competition,<br>0.5 – medium competition,<br>0.9 – high competition;<br>if there is no data the value is null |[optional]|
**cpc** | **StrictFloat** | cost-per-click<br>represents the average cost per click (USD) historically paid for the keyword.<br>if there is no data then the value is null |[optional]|
**search_volume** | **StrictInt** | monthly average search volume rate<br>represents either the (approximate) number of searches for the given keyword idea on bing search engine depending on the user’s targeting;<br>search volume is rounded to the nearest tens;<br>if there is no data, the value is null |[optional]|
**categories** | **List[Optional[StrictStr]]** | product and service categories<br>our API doesn’t return categories for this endpoint: the parameter will always equal null |[optional]|
**monthly_searches** | **List[Optional[MonthlySearches]]** | monthly searches<br>represents the (approximate) number of searches on this keyword idea (as available for the past twelve months), targeted to the specified geographic locations<br>if there is no data then the value is null |[optional]|