# BaseResponseInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**version** | **StrictStr** | the current version of the API |[optional]|
**status_code** | **StrictInt** | general status code<br>you can find the full list of the response codes here |[optional]|
**status_message** | **StrictStr** | general informational message<br>you can find the full list of general informational messages here |[optional]|
**time** | **StrictStr** | total execution time, seconds |[optional]|
**cost** | **StrictFloat** | total tasks cost, USD |[optional]|
**tasks_count** | **StrictInt** | the number of tasks in the tasks array |[optional]|
**tasks_error** | **StrictInt** | the number of tasks in the tasks array returned with an error |[optional]|