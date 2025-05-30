# SerpGoogleFinanceMarketsLiveAdvancedRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**location_name** | **StrictStr** | full name of search engine location<br>required field if you don’t specify location_code<br>if you use this field, you don’t need to specify location_code<br>you can receive the list of available locations of the search engine with their location_name by making a separate request to  https://api.dataforseo.com/v3/serp/google/locations<br>example:<br>London,England,United Kingdom |[optional]|
**location_code** | **StrictInt** | search engine location code<br>required field if you don’t specify location_name<br>if you use this field, you don’t need to specify location_name<br>you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/serp/google/locations<br>example:<br>2840 |[optional]|
**language_name** | **StrictStr** | full name of search engine language<br>required field if you don’t specify language_code <br>if you use this field, you don’t need to specify language_code<br>you can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/serp/google/languages<br>example:<br>English |[optional]|
**language_code** | **StrictStr** | search engine language code<br>required field if you don’t specify language_name<br>if you use this field, you don’t need to specify language_name<br>you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/languages<br>example:<br>en |[optional]|
**device** | **StrictStr** | device type<br>optional field<br>possible value: desktop |[optional]|
**os** | **StrictStr** | device operating system<br>optional field<br>possible values: windows |[optional]|
**market_type** | **StrictStr** | type of google finance market<br>optional field<br>possible values: most-active, indexes, indexes/americas, indexes/europe-middle-east-africa, indexes/asia-pacific, gainers, losers, climate-leaders, cryptocurrencies, currencies<br>default value: most-active |[optional]|
**tag** | **StrictStr** | user-defined task identifier<br>optional field<br>the character limit is 255<br>you can use this parameter to identify the task and match it with the result<br>you will find the specified tag value in the data object of the response |[optional]|