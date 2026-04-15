# SerpGoogleDatasetInfoLiveAdvancedRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**dataset_id** | **StrictStr** | ID of the datasetrequired fieldyou can find dataset ID in the dataset URL or dataset item of Google Dataset Search resultexample:L2cvMTFqbl85ZHN6MQ== |[optional]|
**language_code** | **StrictStr** | search engine language codeoptional fieldif you use this field, you don't need to specify language_namepossible value:en |[optional]|
**device** | **StrictStr** | device typeoptional fieldreturn results for a specific device typepossible value: desktop |[optional]|
**language_name** | **StrictStr** | full name of search engine languageoptional fieldif you use this field, you don't need to specify language_codepossible value:English |[optional]|
**os** | **StrictStr** | device operating systemoptional fieldpossible values: windows, macosdefault value: windows |[optional]|
**tag** | **StrictStr** | user-defined task identifieroptional fieldthe character limit is 255you can use this parameter to identify the task and match it with the resultyou will find the specified tag value in the data object of the response |[optional]|