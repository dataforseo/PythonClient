# KeywordInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | search engine type |[optional]|
**last_updated_time** | **StrictStr** | date and time when keyword data was updated<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**competition** | **StrictFloat** | competition<br>represents the relative amount of competition associated with the given keyword. This value is based on Google Ads data and can be between 0 and 1 (inclusive) |[optional]|
**competition_level** | **StrictStr** | competition level<br>represents the relative level of competition associated with the given keyword in paid SERP only;<br>possible values: LOW, MEDIUM, HIGH<br>if competition level is unknown, the value is null;<br>learn more about the metric in this help center article |[optional]|
**cpc** | **StrictFloat** | cost-per-click<br>represents the average cost per click (USD) historically paid for the keyword |[optional]|
**search_volume** | **StrictFloat** | average monthly search volume rate<br>represents the (approximate) number of searches for the given keyword idea on google.com |[optional]|
**low_top_of_page_bid** | **StrictFloat** | minimum bid for the ad to be displayed at the top of the first page<br>indicates the value greater than about 20% of the lowest bids for which ads were displayed (based on Google Ads statistics for advertisers)<br>the value may differ depending on the location specified in a POST request |[optional]|
**high_top_of_page_bid** | **StrictFloat** | maximum bid for the ad to be displayed at the top of the first page<br>indicates the value greater than about 80% of the lowest bids for which ads were displayed (based on Google Ads statistics for advertisers)<br>the value may differ depending on the location specified in a POST request |[optional]|
**categories** | **List[Optional[StrictFloat]]** | product and service categories<br>you can download the full list of possible categories |[optional]|
**monthly_searches** | **List[Optional[MonthlySearches]]** | monthly searches<br>represents the (approximate) number of searches on this keyword idea (as available for the past twelve months), targeted to the specified geographic locations |[optional]|
**search_volume_trend** | **SearchVolumeTrend** | search volume trend changes<br>represents search volume change in percent compared to the previous period |[optional]|