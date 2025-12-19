# SerpGoogleDatasetInfoLiveAdvancedRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**dataset_id** | **StrictStr** | ID of the dataset<br>required field<br>you can find dataset ID in the dataset URL or dataset item of Google Dataset Search result<br>example:<br>L2cvMTFqbl85ZHN6MQ== |[optional]|
**language_code** | **StrictStr** | search engine language code<br>optional field<br>if you use this field, you don't need to specify language_name<br>possible value:<br>en |[optional]|
**device** | **StrictStr** | device type<br>optional field<br>possible value: desktop |[optional]|
**language_name** | **StrictStr** | full name of search engine language<br>optional field<br>if you use this field, you don't need to specify language_code<br>possible value:<br>English |[optional]|
**os** | **StrictStr** | device operating system<br>optional field<br>possible values: windows, macos<br>default value: windows |[optional]|
**tag** | **StrictStr** | user-defined task identifier<br>optional field<br>the character limit is 255<br>you can use this parameter to identify the task and match it with the result<br>you will find the specified tag value in the data object of the response |[optional]|