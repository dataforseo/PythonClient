# SerpIdListRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**datetime_from** | **StrictStr** | start time for filtering results<br>required field<br>if include_metadata is set to true, minimum start value: a month from current datetime;<br>if include_metadata is set to false, minimum start value: six months from current datetime;<br>maximum start value: current datetime;<br>must be specified in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”;<br>example:<br>2023-01-15 12:57:46 +00:00 |[optional]|
**datetime_to** | **StrictStr** | finish time for filtering results<br>required field<br>if include_metadata is set to true, minimum finish value: a month from current datetime;<br>if include_metadata is set to false, minimum finish value: six months from current datetime;<br>maximum finish value: current datetime;<br>Note: datetime_to must be greater than datetime_from;<br>must be specified in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”;<br>example:<br>2023-01-31 13:57:46 +00:00 |[optional]|
**limit** | **StrictInt** | the maximum number of returned task IDs<br>optional field<br>default value: 1000<br>maximum value: 1000<br>minimum value: 1 |[optional]|
**offset** | **StrictInt** | offset in the results array of returned task IDs<br>optional field<br>if you specify the 10 value, the first ten tasks in the results array will be omitted;<br>minimum and default value: 0;<br>maximum value: 100M (100 million) |[optional]|
**sort** | **StrictStr** | sorting by task execution time<br>optional field<br>possible values: 'asc', 'desc'<br>default value: 'asc' |[optional]|
**include_metadata** | **StrictBool** | include task metadata in the response<br>optional field<br>if set to true, the metadata object containing parameters specified in the POST request will be provided in the response;<br>default value: false |[optional]|