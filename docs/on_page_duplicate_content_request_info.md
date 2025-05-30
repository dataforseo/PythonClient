# OnPageDuplicateContentRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**id** | **StrictStr** | ID of the task<br>required field<br>you can get this ID in the response of the Task POST endpoint<br>example:<br>“07131248-1535-0216-1000-17384017ad04” |[optional]|
**url** | **StrictStr** | page URL<br>required field<br>specify the initial page you want to receive duplicate content for |[optional]|
**similarity** | **StrictInt** | content similarity score<br>by default, the content is considered duplicate if the value is greater than or equals 6<br>you can specify any similarity score in the 0-to-10 range |[optional]|
**limit** | **StrictInt** | the maximum number of returned pages<br>optional field<br>default value: 100<br>maximum value: 1000 |[optional]|
**offset** | **StrictInt** | offset in the results array of returned pages<br>optional field<br>default value: 0<br>if you specify the 10 value, the first ten pages in the results array will be omitted and the data will be provided for the successive pages |[optional]|
**tag** | **StrictStr** | user-defined task identifier<br>optional field<br>the character limit is 255<br>you can use this parameter to identify the task and match it with the result<br>you will find the specified tag value in the data object of the response |[optional]|