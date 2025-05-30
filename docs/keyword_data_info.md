# KeywordDataInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | search engine type |[optional]|
**keyword** | **StrictStr** | returned keyword idea |[optional]|
**location_code** | **StrictFloat** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**keyword_info** | **KeywordInfo** | keyword data for the returned keyword idea |[optional]|
**keyword_info_normalized_with_bing** | **KeywordInfoNormalizedWithInfo** | contains keyword search volume normalized with Bing search volume |[optional]|
**keyword_info_normalized_with_clickstream** | **KeywordInfoNormalizedWithInfo** | contains keyword search volume normalized with clickstream data |[optional]|
**clickstream_keyword_info** | **ClickstreamKeywordInfo** | clickstream data for the returned keyword<br>to retrieve results for this field, the parameter include_clickstream_data must be set to true |[optional]|
**keyword_properties** | **KeywordProperties** | additional information about the keyword |[optional]|
**serp_info** | **SerpInfo** | SERP data<br>the value will be null if you didn’t set the field include_serp_info to true in the POST array or if there is no SERP data for this keyword in our database |[optional]|
**avg_backlinks_info** | **AvgBacklinksInfo** | backlink data for the returned keyword<br>this object provides the average number of backlinks, referring pages and domains, as well as the average rank values among the top-10 webpages ranking organically for the keyword |[optional]|
**search_intent_info** | **SearchIntentInfo** | search intent info for the returned keyword<br>learn about search intent in this help center article |[optional]|