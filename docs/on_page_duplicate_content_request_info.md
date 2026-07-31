# OnPageDuplicateContentRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**id** | **StrictStr** | <em>ID of the task</em><br><strong>required field</strong><br>you can get this ID in the response of the <a href='https://docs.dataforseo.com/v3/on_page/task_post/'>Task POST</a> endpoint<br>example:<br>'07131248-1535-0216-1000-17384017ad04' |[optional]|
**url** | **StrictStr** | <em>page URL</em><br><strong>required field</strong><br>specify the initial page you want to receive duplicate content for |[optional]|
**similarity** | **StrictInt** | <em>content similarity score</em><br>by default, the content is considered duplicate if the value is greater than or equals <code>6</code><br>you can specify any similarity score in the 0-to-10 range |[optional]|
**limit** | **StrictInt** | <em>the maximum number of returned pages</em><br>optional field<br>default value: <code>100</code><br>maximum value: <code>1000</code> |[optional]|
**offset** | **StrictInt** | <em>offset in the results array of returned pages</em><br>optional field<br>default value: <code>0</code><br>maximum value: <code>2000000</code><br>if you specify the <code>10</code> value, the first ten pages in the results array will be omitted and the data will be provided for the successive pages |[optional]|
**tag** | **StrictStr** | <em>user-defined task identifier</em><br>optional field<br><em>the character limit is 255</em><br>you can use this parameter to identify the task and match it with the result<br>you will find the specified <code>tag</code> value in the <code>data</code> object of the response |[optional]|