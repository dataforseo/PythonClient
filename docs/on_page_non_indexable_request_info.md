# OnPageNonIndexableRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**id** | **StrictStr** | ID of the task<br>required field<br>you can get this ID in the response of the Task POST endpoint<br>example:<br>“07131248-1535-0216-1000-17384017ad04” |[optional]|
**limit** | **StrictInt** | the maximum number of returned pages<br>optional field<br>default value: 100<br>maximum value: 1000 |[optional]|
**offset** | **StrictInt** | offset in the results array of returned pages<br>optional field<br>default value: 0<br>if you specify the 10 value, the first ten pages in the results array will be omitted and the data will be provided for the successive pages |[optional]|
**filters** | **List[Optional[Any]]** | array of results filtering parameters<br>optional field<br>you can add several filters at once (8 filters maximum)<br>you should set a logical operator and, or between the conditions<br>the following operators are supported:<br>regex, not_regex, <, <=, >, >=, =, <>, in, not_in, like, not_like<br>you can use the % operator with like and not_like to match any string of zero or more characters<br>example:<br>['reason','=','robots_txt'][['reason','<>','robots_txt'],<br>'and',<br>['url','not_like','%/wp-admin/%']]<br>[['url','not_like','%/wp-admin/%'],<br>'and',<br>[['reason','<>','meta_tag'],'or',['reason','<>','http_header']]]<br>The full list of possible filters is available by this link. |[optional]|