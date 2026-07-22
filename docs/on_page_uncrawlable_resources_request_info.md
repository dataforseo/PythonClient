# OnPageUncrawlableResourcesRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**id** | **StrictStr** | ID of the task<br>required field<br>you can get this ID in the response of the Task POST endpoint<br>example:<br>'07131248-1535-0216-1000-17384017ad04' |[optional]|
**limit** | **StrictInt** | the maximum number of returned uncrawlable resources<br>optional field<br>default value: 100<br>maximum value: 1000 |[optional]|
**offset** | **StrictInt** | offset in the results array of returned uncrawlable resources<br>optional field<br>default value: 0<br> maximum value: 2000000<br>if you specify the 10 value, the first ten invalid resources in the results array will be omitted and the data will be provided for the successive invalid resources |[optional]|
**order_by** | **List[Optional[StrictStr]]** | results sorting rules<br>optional field<br>you can use the same values as in the filters array to sort the results<br>possible sorting types:<br>asc - results will be sorted in the ascending order<br>desc - results will be sorted in the descending order<br>you should use a comma to set up a sorting type<br>example:<br>['meta.content_type,desc']<br>note that you can set no more than three sorting rules in a single request<br>you should use a comma to separate several sorting rules<br>example:<br>['meta.content_type,asc','fetch_time,desc'] |[optional]|
**filters** | **List[Optional[Any]]** | array of results filtering parameters<br>optional field<br>you can add several filters at once (8 filters maximum)<br>you should set a logical operator and, or between the conditions<br>the following operators are supported:<br>regex, not_regex, <, <=, >, >=, =, <>, in, not_in, like, not_like<br>you can use the % operator with like and not_like to match any string of zero or more characters<br>example:<br> [['meta.content_type','=','image/jpeg'],<br>'and',<br>['url','not_like','%/help-center/%']]The full list of possible filters is available by this link. |[optional]|