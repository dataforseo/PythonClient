# KeywordsDataDataforseoTrendsExploreLiveRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keywords** | **List[Optional[StrictStr]]** | keywords<br>required field<br>the maximum number of keywords you can specify: 5<br>learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article |[optional]|
**location_name** | **StrictStr** | full name of search engine location<br>optional field<br>if you don’t use this field, you will recieve global results<br>if you use this field, you don’t need to specify location_code<br>you can receive the list of available locations of the search engine with their location_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/dataforseo_trends/locations<br>note that the data will be provided for the country the specified location_name belongs to;<br>example:<br>United Kingdom |[optional]|
**location_code** | **StrictInt** | search engine location code<br>optional field<br>if you don’t use this field, you will recieve global results<br>if you use this field, you don’t need to specify location_name<br>you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/dataforseo_trends/locations<br>note that the data will be provided for the country the specified location_code belongs to;<br>example:<br>2840 |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**date_from** | **StrictStr** | starting date of the time range<br>optional field<br>if you don’t specify this field, the current day and month of the preceding year will be used by default<br>minimal value for the web type: 2004-01-01<br>minimal value for other types: 2008-01-01<br>date format: 'yyyy-mm-dd'<br>example:<br>'2019-01-15' |[optional]|
**date_to** | **StrictStr** | ending date of the time range<br>optional field<br>if you don’t specify this field, the today’s date will be used by default<br>date format: 'yyyy-mm-dd'<br>example:<br>'2019-01-15' |[optional]|
**time_range** | **StrictStr** | preset time ranges<br>optional field<br>if you specify date_from or date_to parameters, this field will be ignored when setting a task<br>possible values for all type parameters:<br>past_4_hours, past_day, past_7_days, past_30_days, past_90_days, past_12_months, past_5_years |[optional]|
**tag** | **StrictStr** | user-defined task identifier<br>optional field<br>the character limit is 255<br>you can use this parameter to identify the task and match it with the result<br>you will find the specified tag value in the data object of the response |[optional]|