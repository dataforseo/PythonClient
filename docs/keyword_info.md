# KeywordInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | <em>search engine type</em> |[optional]|
**last_updated_time** | **StrictStr** | <em>date and time when keyword data was updated</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**competition** | **StrictFloat** | <em>competition</em><br>represents the relative amount of competition associated with the given keyword. This value is based on Google Ads data and can be between 0 and 1 (inclusive) |[optional]|
**competition_level** | **StrictStr** | <em>competition level</em><br>represents the relative level of competition associated with the given keyword in paid SERP only;<br>possible values: <code>LOW</code>, <code>MEDIUM</code>, <code>HIGH</code><br>if competition level is unknown, the value is <code>null</code>;<br>learn more about the metric in <a href='https://dataforseo.com/help-center/what-is-competition' target='_blank' rel='noopener noreferrer'>this help center article</a> |[optional]|
**cpc** | **StrictFloat** | <em>cost-per-click</em><br>represents the average cost per click (USD) historically paid for the keyword |[optional]|
**search_volume** | **StrictInt** | <em>average monthly search volume rate</em><br>represents the (approximate) number of searches for the given keyword idea on google.com |[optional]|
**low_top_of_page_bid** | **StrictFloat** | <em>minimum bid for the ad to be displayed at the top of the first page</em><br>indicates the value greater than about 20% of the lowest bids for which ads were displayed (based on Google Ads statistics for advertisers)<br>the value may differ depending on the location specified in a POST request |[optional]|
**high_top_of_page_bid** | **StrictFloat** | <em>maximum bid for the ad to be displayed at the top of the first page</em><br>indicates the value greater than about 80% of the lowest bids for which ads were displayed (based on Google Ads statistics for advertisers)<br>the value may differ depending on the location specified in a POST request |[optional]|
**categories** | **List[Optional[StrictInt]]** | <em>product and service categories</em><br>you can download the <a href='https://cdn.dataforseo.com/v3/categories/categories_dataforseo_labs_2023_10_25.csv'>full list of possible categories</a> |[optional]|
**monthly_searches** | **List[Optional[MonthlySearchesInfo]]** | <em>monthly searches</em><br>represents the (approximate) number of searches on this keyword idea (as available for the past twelve months), targeted to the specified geographic locations |[optional]|
**search_volume_trend** | **SearchVolumeTrend** | <em>search volume trend changes</em><br>represents search volume change in percent compared to the previous period |[optional]|