# EventDates


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**start_datetime** | **StrictStr** | date and time when the event starts<br>if time zone is specified in the event, value will be returned in the UTC format:<br>“yyyy-mm-ddThh-mm-ss+00:00”<br>example:<br>2019-11-15T12:57:46+00:00<br>if time zone is not specified in the event, unspecified local time will be returned in the following format:<br>“yyyy-mm-ddThh-mm-ss”<br>example:<br>2019-11-15T12:57:46 |[optional]|
**end_datetime** | **StrictStr** | date and time when the event ends<br>if time zone is specified in the event, value will be returned in the UTC format:<br>“yyyy-mm-ddThh-mm-ss+00:00”<br>example:<br>2019-11-15T12:57:46+00:00<br>if time zone is not specified in the event, unspecified local time will be returned in the following format:<br>“yyyy-mm-ddThh-mm-ss”<br>example:<br>2019-11-15T12:57:46 |[optional]|
**displayed_dates** | **StrictStr** | date or date range as it is displayed in SERP |[optional]|