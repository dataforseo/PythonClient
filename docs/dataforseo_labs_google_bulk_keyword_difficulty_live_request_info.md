# DataforseoLabsGoogleBulkKeywordDifficultyLiveRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keywords** | **List[Optional[StrictStr]]** | target keywords<br>required field<br>UTF-8 encoding<br>maximum number of keywords you can specify in this array: 1000<br>the keywords will be converted to lowercase format<br>learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article |[optional]|
**location_name** | **StrictStr** | full name of the location<br>required field if don’t specify location_code<br>you can receive the list of available locations with their location_name by making a separate request to the<br>https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages<br>example:<br>United Kingdom |[optional]|
**location_code** | **StrictInt** | location code<br>required field if don’t specify location_name<br>you can receive the list of available locations with their location_code by making a separate request to the<br>https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages<br>example:<br>2840 |[optional]|
**language_name** | **StrictStr** | full name of the language<br>required field if don’t specify language_code<br>you can receive the list of available languages with their language_name by making a separate request to the<br>https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages<br>example:<br>English |[optional]|
**language_code** | **StrictStr** | language code<br>required field if don’t specify language_name<br>you can receive the list of available languages with their language_code by making a separate request to the<br>https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages<br>example:<br>en |[optional]|
**tag** | **StrictStr** | user-defined task identifier<br>optional field<br>the character limit is 255<br>you can use this parameter to identify the task and match it with the result<br>you will find the specified tag value in the data object of the response |[optional]|