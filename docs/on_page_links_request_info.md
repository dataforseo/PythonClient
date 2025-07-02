# OnPageLinksRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**id** | **StrictStr** | ID of the task<br>required field<br>you can get this ID in the response of the Task POST endpoint<br>example:<br>“07131248-1535-0216-1000-17384017ad04” |[optional]|
**page_from** | **StrictStr** | relative page URL<br>optional field<br>if you use this field, the API response will contain only links from the specified page<br>note that in this field you can specify relative URLs only |[optional]|
**page_to** | **StrictStr** | relative page URL<br>optional field<br>if you use this field, the API response will contain only internal links pointing to the specified page<br>note that in this field you can specify relative URLs only |[optional]|
**limit** | **StrictInt** | the maximum number of returned links<br>optional field<br>default value: 100<br>maximum value: 1000 |[optional]|
**offset** | **StrictInt** | offset in the results array of returned links<br>optional field<br>default value: 0<br>if you specify the 10 value, the first ten links in the results array will be omitted and the data will be provided for the successive links |[optional]|
**filters** | **List[Optional[Any]]** | array of results filtering parameters<br>optional field<br>you can add several filters at once (8 filters maximum)<br>you should set a logical operator and, or between the conditions<br>the following operators are supported:<br>regex, not_regex, =, <>, in, not_in, like, not_like<br>you can use the % operator with like and not_like to match any string of zero or more characters<br>example:<br>['direction','=','external']<br>[['domain_to','<>','example.com'],<br>'and',<br>['link_from','not_like','%example.com/blog%']]<br>[['direction','=','external'],<br>'and',<br>[['link_from','like','%example.com/blog%'],'or',['link_from','like','%example.com/help%']]]<br>The full list of possible filters is available by this link. |[optional]|
**tag** | **StrictStr** | user-defined task identifier<br>optional field<br>the character limit is 255<br>you can use this parameter to identify the task and match it with the result<br>you will find the specified tag value in the data object of the response |[optional]|