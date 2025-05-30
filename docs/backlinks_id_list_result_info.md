# BacklinksIdListResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**id** | **StrictStr** | id of the task |[optional]|
**url** | **StrictStr** | URL of the task<br>URL you used for making an API call |[optional]|
**datetime_posted** | **StrictStr** | date and time when the task was made<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2023-01-15 12:57:46 +00:00 |[optional]|
**datetime_done** | **StrictStr** | date and time when the task was completed<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2023-01-15 12:57:46 +00:00 |[optional]|
**status** | **StrictStr** | informational message of the task<br>you can find the full list of general informational messages here |[optional]|
**cost** | **StrictFloat** | cost of the task, USD |[optional]|
**metadata** | **Dict[str, Optional[Any]]** | contains parameters you specified in the POST request |[optional]|