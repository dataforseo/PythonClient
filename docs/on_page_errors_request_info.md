# OnPageErrorsRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**limit** | **StrictInt** | <em>the maximum number of returned tasks that responded with an error</em><br>optional field<br>default value: <code>1000</code><br>maximum value: <code>1000</code> |[optional]|
**offset** | **StrictInt** | <em>offset in the results array of returned tasks</em><br>optional field<br>default value: <code>0</code><br>if you specify the <code>10</code> value, the first ten tasks in the results array will be omitted and the data will be provided for the successive tasks |[optional]|
**filtered_function** | **StrictStr** | <em>return tasks with a certain function</em><br>use this field to obtain a list of tasks that returned an error filtered by a certain function<br>you can filter the results by the values you receive in the <code>function</code> fields of the API response<br>i.e., once you receive unfiltered results, you can call this API again to filter them by <code>function</code> <br>example: <code>on_page/task_post</code>, <code>postback_url</code>, <code>pingback_url</code> |[optional]|
**datetime_from** | **StrictStr** | <em>start time for filtering results</em><br>optional field<br>allows filtering results by the <code>datetime</code> parameter within the range of the last 7 days;<br>must be specified in the UTC format: 'yyyy-mm-dd hh-mm-ss +00:00'<br>example:<br><code>2021-11-15 12:57:46 +00:00</code> |[optional]|
**datetime_to** | **StrictStr** | <em>finish time for filtering results</em><br>optional field<br>allows filtering results by the <code>datetime</code> parameter within the range of the last 7 days;<br>must be specified in the UTC format: 'yyyy-mm-dd hh-mm-ss +00:00'<br>example:<br><code>2021-11-15 13:57:46 +00:00</code> |[optional]|