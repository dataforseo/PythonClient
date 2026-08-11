# KeywordsDataGoogleAdsKeywordsForKeywordsTaskGetResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | <em>keyword in a POST array</em> |[optional]|
**spell** | **StrictStr** |  |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em><br>if there is no data, the value is_<code>null</code>n |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em><br>if there is no data, the value is_<code>null</code>n |[optional]|
**search_partners** | **StrictBool** | <em>include Google search partners</em><br>the value you specified when setting the task<br>if <code class='prettyprint'>true</code>, the results are returned for owned, operated, and syndicated networks across Google and partner sites that host Google search;<br>if <code>false</code>, the results are returned for Google search sites only |[optional]|
**competition** | **StrictStr** | <em>competition</em><br>represents the relative level of competition associated with the given keyword in paid SERP only<br>possible values: <code>LOW</code>, <code>MEDIUM</code>, <code>HIGH</code><br>if competition level is unknown, the value is <code>null</code>;<br>learn more about the metric in <a href='https://dataforseo.com/help-center/what-is-competition' rel='noopener noreferrer' target='_blank'>this help center article</a> |[optional]|
**competition_index** | **StrictInt** | <em>competition index</em><br>the competition index for the query indicating how competitive ad placement is for the keyword<br>can take values from 0 to 100 <br>the level of competition from 0 to 100 is determined by the number of ad slots filled divided by the total number of ad slots available <br>if not enough data is available, the value is <code>null</code>;<br>learn more about the metric in <a href='https://dataforseo.com/help-center/what-is-competition' rel='noopener noreferrer' target='_blank'>this help center article</a> |[optional]|
**search_volume** | **StrictInt** | <em>monthly average search volume rate</em><br>represents the (approximate) number of searches for the given keyword idea either on google.com or google.com and partners, depending on the user’s targeting<br>if there is no data, the value is <code>null</code> |[optional]|
**low_top_of_page_bid** | **StrictFloat** | <em>minimum bid for the ad to be displayed at the top of the first page</em><br>indicates the value greater than about 20% of the lowest bids for which ads were displayed (based on Google Ads statistics for advertisers)<br>the value may differ depending on the location specified in a POST request |[optional]|
**high_top_of_page_bid** | **StrictFloat** | <em>maximum bid for the ad to be displayed at the top of the first page</em><br>indicates the value greater than about 80% of the lowest bids for which ads were displayed (based on Google Ads statistics for advertisers)<br>the value may differ depending on the location specified in a POST request |[optional]|
**cpc** | **StrictFloat** | <em>cost per click</em><br>indicates the amount paid (USD) for each click on the ad displayed for a given keyword |[optional]|
**monthly_searches** | **List[Optional[MonthlySearchesInfo]]** | <em>monthly searches</em><br>represents the (approximate) number of searches on this keyword idea (as available for the past twelve months), targeted to the specified geographic locations<br>if there is no data, the value is <code>null</code> |[optional]|