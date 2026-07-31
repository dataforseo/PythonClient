# MerchantIdListRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**datetime_from** | **StrictStr** | <em>start time for filtering results</em><br><strong>required field</strong><br>if <code>include_metadata</code> is set to <code>true</code>, maximum value: a month from current datetime;<br>if <code>include_metadata</code> is set to <code>false</code>, maximum value: six months from current datetime;<br>must be specified in the UTC format: 'yyyy-mm-dd hh-mm-ss +00:00'<br>example:<br><code>2023-01-15 12:57:46 +00:00</code> |[optional]|
**datetime_to** | **StrictStr** | <em>finish time for filtering results</em><br><strong>required field</strong><br>maximum value: current datetime;<br>must be specified in the UTC format: 'yyyy-mm-dd hh-mm-ss +00:00'<br>example:<br><code>2023-01-31 13:57:46 +00:00</code> |[optional]|
**limit** | **StrictInt** | <em>the maximum number of returned task IDs</em><br>optional field<br>default value: <code>1000</code><br>maximum value: <code>1000</code> |[optional]|
**offset** | **StrictInt** | <em>offset in the results array of returned task IDs</em><br>optional field<br>default value: <code>0</code><br>if you specify the <code>10</code> value, the first ten tasks in the results array will be omitted |[optional]|
**sort** | **StrictStr** | <em>sorting by task execution time</em><br>optional field<br>possible values: <code>'asc'</code>, <code>'desc'</code><br>default value: <code>'asc'</code> |[optional]|
**include_metadata** | **StrictBool** | <em>include task metadata in the respond</em><br>optional field<br>default value: <code>false</code> |[optional]|