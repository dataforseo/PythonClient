# KeywordsDataGoogleTrendsExploreLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keywords** | **List[Optional[StrictStr]]** | <em>keywords in a POST array</em> |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em><br>if there is no data, then the value is_<code>null</code>n |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em><br>if there is no data, then the value is_<code>null</code>n |[optional]|
**check_url** | **StrictStr** | <em>direct URL to the Google Trends results</em><br>you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | <em>date and time when the result was received</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**items_count** | **StrictInt** | <em>the number of results returned in the <strong><code>items</code></strong> array</em> |[optional]|
**items** | **List[Optional[BaseKeywordDataGoogleTrendsItem]]** | <em>items on the Google Trends page</em> |[optional]|