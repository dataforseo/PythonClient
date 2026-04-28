# OnPageUncrawlableResourcesRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**id** | **StrictStr** | ID of the taskrequired fieldyou can get this ID in the response of the Task POST endpointexample:'07131248-1535-0216-1000-17384017ad04' |[optional]|
**limit** | **StrictInt** | the maximum number of returned uncrawlable resourcesoptional fielddefault value: 100maximum value: 1000 |[optional]|
**offset** | **StrictInt** | offset in the results array of returned uncrawlable resourcesoptional fielddefault value: 0if you specify the 10 value, the first ten invalid resources in the results array will be omitted and the data will be provided for the successive invalid resources |[optional]|
**order_by** | **List[Optional[StrictStr]]** | results sorting rulesoptional fieldyou can use the same values as in the filters array to sort the resultspossible sorting types:asc - results will be sorted in the ascending orderdesc - results will be sorted in the descending orderyou should use a comma to set up a sorting typeexample:['meta.content_type,desc']note that you can set no more than three sorting rules in a single requestyou should use a comma to separate several sorting rulesexample:['meta.content_type,asc','fetch_time,desc'] |[optional]|
**filters** | **List[Optional[Any]]** | array of results filtering parametersoptional fieldyou can add several filters at once (8 filters maximum)you should set a logical operator and, or between the conditionsthe following operators are supported:regex, not_regex, <, <=, >, >=, =, <>, in, not_in, like, not_likeyou can use the % operator with like and not_like to match any string of zero or more charactersexample: [['meta.content_type','=','image/jpeg'],'and',['url','not_like','%/help-center/%']]The full list of possible filters is available by this link. |[optional]|