# KeywordsDataGoogleAdsSearchVolumeTaskGetResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | <em>keyword<br></em><strong>keyword is returned with decoded %## (plus character '+' will be decoded to a space character)</strong> |[optional]|
**spell** | **StrictStr** | <em>correct spelling of the keyword</em><br><strong>Note:</strong>if the keyword in the POST array appears to be misspelled, data will be returned for the correctly spelled keyword;<br>we use the functionality of Google Ads API to check and validate the spelling of keywords, <a href='https://support.google.com/google-ads/answer/7476658' target='_blank' rel='noopener noreferrer'>learn more by this link</a> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em><br>if there is no data, then the value is_<code>null</code>n |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em><br>if there is no data, then the value is_<code>null</code>n |[optional]|
**search_partners** | **StrictBool** | <em>indicates whether data from partner networks included in the response</em> |[optional]|
**competition** | **StrictStr** | <em>competition</em><br>represents the relative amount of competition associated with the given keyword in paid SERP only;<br>this value is based on Google Ads data and can take the following values: <code>HIGH</code>, <code>MEDIUM</code>, <code>LOW</code>;<br>if there is no data the value is <code>null</code>;<br>learn more about the metric in <a href='https://dataforseo.com/help-center/what-is-competition' target='_blank' rel='noopener noreferrer'>this help center article</a> |[optional]|
**competition_index** | **StrictInt** | <em>competition</em><br>represents the relative amount of competition associated with the given keyword in paid SERP only;<br>this value is based on Google Ads data and can be between 0 and 100 (inclusive);<br>if there is no data the value is <code>null</code>;<br>learn more about the metric in <a href='https://dataforseo.com/help-center/what-is-competition' target='_blank' rel='noopener noreferrer'>this help center article</a> |[optional]|
**search_volume** | **StrictInt** | <em>monthly average search volume rate</em> |[optional]|
**low_top_of_page_bid** | **StrictFloat** | <em>minimum bid for the ad to be displayed at the top of the first page</em><br>indicates the value greater than about 20% of the lowest bids for which ads were displayed (based on Google Ads statistics for advertisers);<br>the value may differ depending on the location specified in a POST request |[optional]|
**high_top_of_page_bid** | **StrictFloat** | <em>maximum bid for the ad to be displayed at the top of the first page</em><br>indicates the value greater than about 80% of the lowest bids for which ads were displayed (based on Google Ads statistics for advertisers);<br>the value may differ depending on the location specified in a POST request |[optional]|
**cpc** | **StrictFloat** | <em>cost per click</em><br>indicates the amount paid (USD) for each click on the ad displayed for a given keyword |[optional]|
**monthly_searches** | **List[Optional[MonthlySearchesInfo]]** | <em>monthly searches</em><br>represents the (approximate) number of searches on this keyword idea (as available for the past twelve months by default), targeted to the specified geographic locations;<br>if there is no data then the value is_<code>null</code>n |[optional]|