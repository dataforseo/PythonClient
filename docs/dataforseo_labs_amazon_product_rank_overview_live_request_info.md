# DataforseoLabsAmazonProductRankOverviewLiveRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**asins** | **List[Optional[StrictStr]]** | product IDs to compare<br>required field<br>product IDs to receive ranking data for;<br>the maximum number of ASINs you can specify in this array is 1000;<br>you can receive the asin parameter by making a separate request to the Amazon Products endpoint<br>Note: all letters in ASIN code must be specified in uppercase format;<br>example:<br>B01LW2SL7R |[optional]|
**location_name** | **StrictStr** | full name of the location<br>required field if don’t specify location_code<br>you can receive the list of available locations with their location_name by making a separate request to<br>https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages;<br>Note: this endpoint currently supports the US, Egypt, Saudi Arabia, and the United Arab Emirates locations only;<br>example:<br>United States |[optional]|
**location_code** | **StrictInt** | location code<br>required field if don’t specify location_name<br>you can receive the list of available locations with their location_code by making a separate request to<br>https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages;<br>Note: this endpoint currently supports the US, Egypt, Saudi Arabia, and the United Arab Emirates locations only;<br>example:<br>2840 |[optional]|
**language_name** | **StrictStr** | full name of the language<br>required field if don’t specify language_code<br>you can receive the list of available languages with their language_name by making a separate request to the<br>https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages<br>example:<br>English |[optional]|
**language_code** | **StrictStr** | language code<br>required field if don’t specify language_name<br>you can receive the list of available languages with their language_code by making a separate request to the<br>https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages<br>example:<br>en |[optional]|
**tag** | **StrictStr** | user-defined task identifier<br>optional field<br>the character limit is 255<br>you can use this parameter to identify the task and match it with the result<br>you will find the specified tag value in the data object of the response |[optional]|