# BaseResponseTaskInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**id** | **StrictStr** | task identifier<br>unique task identifier in our system in the UUID format |[optional]|
**status_code** | **StrictInt** | status code of the task<br>generated by DataForSEO, can be within the following range: 10000-60000<br>you can find the full list of the response codes here |[optional]|
**status_message** | **StrictStr** | informational message of the task<br>you can find the full list of general informational messages here |[optional]|
**time** | **StrictStr** | execution time, seconds |[optional]|
**cost** | **StrictFloat** | total tasks cost, USD |[optional]|
**result_count** | **StrictInt** | number of elements in the result array |[optional]|
**path** | **List[Optional[StrictStr]]** | URL path |[optional]|
**data** | **Dict[str, Optional[Any]]** | contains the same parameters that you specified in the POST request |[optional]|