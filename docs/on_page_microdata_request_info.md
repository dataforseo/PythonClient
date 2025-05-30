# OnPageMicrodataRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**id** | **StrictStr** | ID of the task<br>required field<br>you can get this ID in the response of the Task POST endpoint<br>example:<br>'07131248-1535-0216-1000-17384017ad04' |[optional]|
**url** | **StrictStr** | resource URL<br>required field<br>you can get this URL in the response of the Pages endpoint<br>example:<br>https://dataforseo.com/apis |[optional]|
**tag** | **StrictStr** | user-defined task identifier<br>optional field<br>the character limit is 255<br>you can use this parameter to identify the task and match it with the result<br>you will find the specified tag value in the data object of the response |[optional]|