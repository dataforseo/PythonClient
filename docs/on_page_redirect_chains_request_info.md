# OnPageRedirectChainsRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**id** | **StrictStr** | ID of the task<br>required field<br>you can get this ID in the response of the Task POST endpoint<br>example:<br>“07131248-1535-0216-1000-17384017ad04” |[optional]|
**url** | **StrictStr** | page URL<br>optional field<br>absolute URL of the target page<br>if you use this field, the API response will return only redirect chains which contain the specified URL |[optional]|
**limit** | **StrictInt** | the maximum number of returned redirect chains<br>optional field<br>default value: 100<br>maximum value: 1000 |[optional]|
**offset** | **StrictInt** | offset in the results array of returned redirect chains<br>optional field<br>default value: 0<br>if you specify the 10 value, the first ten redirect chains in the results array will be omitted and the data will be provided for the successive redirect chains |[optional]|
**filters** | **List[Optional[Any]]** | array of results filtering parameters<br>optional field<br>you can use only one filtering parameter with this endpoint<br>the following filtering parameter is supported:<br>is_redirect_loop<br>the following operators are supported:<br>regex, not_regex, =, <><br>examples:<br>['is_redirect_loop','=','true']<br>['is_redirect_loop','<>','false'] |[optional]|
**tag** | **StrictStr** | user-defined task identifier<br>optional field<br>the character limit is 255<br>you can use this parameter to identify the task and match it with the result<br>you will find the specified tag value in the data object of the response |[optional]|