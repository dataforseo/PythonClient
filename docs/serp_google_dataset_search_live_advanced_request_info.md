# SerpGoogleDatasetSearchLiveAdvancedRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | keywordrequired fieldyou can specify up to 700 characters in the keyword fieldall %## will be decoded (plus character ‘+’ will be decoded to a space character)if you need to use the “%” character for your keyword, please specify it as “%25”;if you need to use the “+” character for your keyword, please specify it as “%2B”;learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article |[optional]|
**language_code** | **StrictStr** | search engine language codeoptional field if you don't specify language_nameif you use this field, you don't need to specify language_namepossible value:en |[optional]|
**depth** | **StrictInt** | parsing depthoptional fieldnumber of results in SERPdefault value: 20max value: 700Your account will be billed per each SERP containing up to 20 results;Setting depth above 20 may result in additional charges if the search engine returns more than 20 results;If the specified depth is higher than the number of results in the response, the difference will be refunded to your account balance automatically. |[optional]|
**device** | **StrictStr** | device typeoptional fieldreturn results for a specific device typepossible value: desktop |[optional]|
**language_name** | **StrictStr** | full name of search engine languageoptional fieldif you use this field, you don't need to specify language_codepossible value:English |[optional]|
**os** | **StrictStr** | device operating systemoptional fieldchoose from the following values: windows, macosdefault value: windows |[optional]|
**tag** | **StrictStr** | user-defined task identifieroptional fieldthe character limit is 255you can use this parameter to identify the task and match it with the resultyou will find the specified tag value in the data object of the response |[optional]|
**last_updated** | **StrictStr** | last time the dataset was updatedoptional fieldpossible values: 1m, 1y, 3y |[optional]|
**file_formats** | **List[Optional[StrictStr]]** | file formats of the datasetoptional fieldpossible values: other, archive, text, image, document, tabular |[optional]|
**usage_rights** | **StrictStr** | usage rights of the datasetoptional fieldpossible values: commercial, noncommercial |[optional]|
**is_free** | **StrictBool** | indicates whether displayed datasets are freeoptional fieldpossible values: true, false |[optional]|
**topics** | **List[Optional[StrictStr]]** | dataset topicsoptional fieldpossible values: humanities, social_sciences, life_sciences, agriculture, natural_sciences, geo, computer, architecture_and_urban_planning, engineering |[optional]|