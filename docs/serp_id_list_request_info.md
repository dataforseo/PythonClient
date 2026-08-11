# SerpIdListRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**datetime_from** | **StrictStr** | <em>start time for filtering results</em><br><strong>required field</strong><br>if <code>include_metadata</code> is set to <code>true</code>, minimum start value: a month from current datetime;<br>if <code>include_metadata</code> is set to <code>false</code>, minimum start value: six months from current datetime;<br>maximum start value: current <code>datetime</code>;<br>must be specified in the UTC format: 'yyyy-mm-dd hh-mm-ss +00:00';<br>example:<br><code>2023-01-15 12:57:46 +00:00</code> |[optional]|
**datetime_to** | **StrictStr** | <em>finish time for filtering results</em><br><strong>required field</strong><br>if <code>include_metadata</code> is set to <code>true</code>, minimum finish value: a month from current datetime;<br>if <code>include_metadata</code> is set to <code>false</code>, minimum finish value: six months from current datetime;<br>maximum finish value: current <code>datetime</code>;<br><strong>Note:</strong> <code>datetime_to</code> must be greater than <code>datetime_from</code>;<br>must be specified in the UTC format: 'yyyy-mm-dd hh-mm-ss +00:00';<br>example:<br><code>2023-01-31 13:57:46 +00:00</code> |[optional]|
**limit** | **StrictInt** | <em>the maximum number of returned task IDs</em><br>optional field<br>default value: <code>1000</code><br>maximum value: <code>1000</code><br>minimum value: <code>1</code> |[optional]|
**offset** | **StrictInt** | <em>offset in the results array of returned task IDs</em><br>optional field<br>if you specify the <code>10</code> value, the first ten tasks in the results array will be omitted;<br>minimum and default value: <code>0</code>;<br>maximum value: <code>100M</code> (100 million) |[optional]|
**sort** | **StrictStr** | <em>sorting by task execution time</em><br>optional field<br>possible values: <code>'asc'</code>, <code>'desc'</code><br>default value: <code>'asc'</code> |[optional]|
**include_metadata** | **StrictBool** | <em>include task metadata in the response</em><br>optional field<br>if set to <code>true</code>, the <code>metadata</code> object containing parameters specified in the POST request will be provided in the response;<br>default value: <code>false</code> |[optional]|