# OnPageKeywordDensityRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**id** | **StrictStr** | ID of the task<br>required field<br>you can get this ID in the response of the Task POST endpoint<br>example:<br>“07131248-1535-0216-1000-17384017ad04” |[optional]|
**keyword_length** | **StrictInt** | number of words for a keyword<br>required field<br>possible values:<br>1, 2, 3, 4, 5 |[optional]|
**url** | **StrictStr** | page URL<br>optional field<br>if you do not specify a page here, the results will be provided for the whole website<br>if you use this field, the API response will contain only keywords from the specified page<br>a page should be specified with absolute URL (including http:// or https://) |[optional]|
**limit** | **StrictInt** | the maximum number of returned keywords<br>optional field<br>default value: 100<br>maximum value: 1000 |[optional]|
**filters** | **List[Optional[Any]]** | array of results filtering parameters<br>optional field<br>you can add several filters at once (8 filters maximum)<br>you should set a logical operator and, or between the conditions<br>the following operators are supported:<br>regex, not_regex, =, <>, in, not_in, like, not_like<br>you can use the % operator with like and not_like to match any string of zero or more characters<br>example:<br>['keyword','=','%seo%']<br>[['keyword','=','%seo%'],<br>'and',<br>['frequency','<','6']]<br>[['keyword','not_like','%seo%'],<br>'and',<br>[['frequency','>','6'],'or',['density','>','0.02']]]<br>The full list of possible filters is available by this link. |[optional]|
**order_by** | **List[Optional[StrictStr]]** | results sorting rules<br>optional field<br>you can use the same values as in the filters array to sort the results<br>possible sorting types:<br>asc – results will be sorted in the ascending order<br>desc – results will be sorted in the descending order<br>you should use a comma to set up a sorting type<br>example:<br>['frequency,desc']<br>note that you can set no more than three sorting rules in a single request<br>you should use a comma to separate several sorting rules<br>example:<br>['keyword,asc','frequency,desc'] |[optional]|
**tag** | **StrictStr** | user-defined task identifier<br>optional field<br>the character limit is 255<br>you can use this parameter to identify the task and match it with the result<br>you will find the specified tag value in the data object of the response |[optional]|