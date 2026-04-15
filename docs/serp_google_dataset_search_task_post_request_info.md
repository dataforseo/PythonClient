# SerpGoogleDatasetSearchTaskPostRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | keywordrequired fieldyou can specify up to 700 characters in the keyword fieldall %## will be decoded (plus character ‘+’ will be decoded to a space character)if you need to use the “%” character for your keyword, please specify it as “%25”;if you need to use the “+” character for your keyword, please specify it as “%2B”.learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article |[optional]|
**language_code** | **StrictStr** | search engine language codeoptional fieldpossible value:en |[optional]|
**depth** | **StrictInt** | parsing depthoptional fieldnumber of results in SERPdefault value: 20max value: 700Your account will be billed per each SERP containing up to 20 results;Setting depth above 20 may result in additional charges if the search engine returns more than 20 results;If the specified depth is higher than the number of results in the response, the difference will be refunded to your account balance automatically; |[optional]|
**priority** | **StrictInt** | task priorityoptional fieldcan take the following values:1 – normal execution priority (set by default)2 – high execution priorityYou will be additionally charged for the tasks with high execution priority.The cost can be calculated on the Pricing page. |[optional]|
**device** | **StrictStr** | device typeoptional fieldreturn results for a specific device typepossible value: desktop |[optional]|
**pingback_url** | **StrictStr** | notification URL of a completed taskoptional fieldwhen a task is completed we will notify you by GET request sent to the URL you have specifiedyou can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.example:http://your-server.com/pingscript?id=$idhttp://your-server.com/pingscript?id=$id&tag=$tagNote: special characters in pingback_url will be urlencoded;i.a., the # character will be encoded into %23learn more on our Help Center |[optional]|
**postback_url** | **StrictStr** | URL for sending task resultsoptional fieldonce the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specifiedyou can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the requestexample:http://your-server.com/postbackscript?id=$idhttp://your-server.com/postbackscript?id=$id&tag=$tagNote: special characters in postback_url will be urlencoded;i.a., the # character will be encoded into %23learn more on our Help Center |[optional]|
**postback_data** | **StrictStr** | postback_url datatyperequired field if you specify postback_urlcorresponds to the datatype that will be sent to your serveronly value: advanced |[optional]|
**language_name** | **StrictStr** | full name of search engine languageoptional fieldif you use this field, you don't need to specify language_codepossible value:English |[optional]|
**os** | **StrictStr** | device operating systemoptional fieldpossible values: windows, macosdefault value: windows |[optional]|
**tag** | **StrictStr** | user-defined task identifieroptional fieldthe character limit is 255you can use this parameter to identify the task and match it with the resultyou will find the specified tag value in the data object of the response |[optional]|
**last_updated** | **StrictStr** | last time the dataset was updatedoptional fieldpossible values: 1m, 1y, 3y |[optional]|
**file_formats** | **List[Optional[StrictStr]]** | file formats of the datasetoptional fieldpossible values: other, archive, text, image, document, tabular |[optional]|
**usage_rights** | **StrictStr** | usage rights of the datasetoptional fieldpossible values: commercial, noncommercial |[optional]|
**is_free** | **StrictBool** | indicates whether displayed datasets are freeoptional fieldpossible values: true, false |[optional]|
**topics** | **List[Optional[StrictStr]]** | dataset topicsoptional fieldpossible values: humanities, social_sciences, life_sciences, agriculture, natural_sciences, geo, computer, architecture_and_urban_planning, engineering |[optional]|