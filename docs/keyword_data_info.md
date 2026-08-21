# KeywordDataInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | <em>search engine type</em> |[optional]|
**keyword** | **StrictStr** | <em>returned keyword idea</em> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em> |[optional]|
**keyword_info** | **KeywordInfo** | <em>keyword data for the returned keyword idea</em> |[optional]|
**keyword_info_normalized_with_bing** | **KeywordInfoNormalizedWithInfo** | <em>contains keyword search volume normalized with Bing search volume</em> |[optional]|
**keyword_info_normalized_with_clickstream** | **KeywordInfoNormalizedWithInfo** | <em>contains keyword search volume normalized with clickstream data<br></em> |[optional]|
**clickstream_keyword_info** | **ClickstreamKeywordInfo** | <em>clickstream data for the returned keyword</em><br>to retrieve results for this field, the parameter <code>include_clickstream_data</code> must be set to <code>true</code> |[optional]|
**keyword_properties** | **KeywordProperties** | <em>additional information about the keyword</em> |[optional]|
**serp_info** | **SerpInfo** | <em>SERP data</em><br>the value will be <code>null</code> if you didn't set the field <code>include_serp_info</code> to <code>true</code> in the POST array or if there is no SERP data for this keyword in our database |[optional]|
**avg_backlinks_info** | **AvgBacklinksInfo** | <em>backlink data for the returned keyword</em><br>this object provides the average number of backlinks, referring pages and domains, as well as the average rank values among the top-10 webpages ranking organically for the keyword |[optional]|
**search_intent_info** | **SearchIntentInfo** | <em>search intent info for the returned keyword</em><br>learn about search intent in this <a href='https://dataforseo.com/help-center/search-intent-and-its-types' target='_blank' rel='noopener noreferrer'>help center article</a> |[optional]|