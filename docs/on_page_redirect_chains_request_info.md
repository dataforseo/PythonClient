# OnPageRedirectChainsRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**id** | **StrictStr** | <em>ID of the task</em><br><strong>required field</strong><br>you can get this ID in the response of the <a href='/v3/on_page/task_post/'>Task POST</a> endpoint<br>example:<br>'07131248-1535-0216-1000-17384017ad04' |[optional]|
**url** | **StrictStr** | <em>page URL</em><br>optional field<br>absolute URL of the target page<br>if you use this field, the API response will return only redirect chains which contain the specified URL |[optional]|
**limit** | **StrictInt** | <em>the maximum number of returned redirect chains</em><br>optional field<br>default value: <code>100</code><br>maximum value: <code>1000</code> |[optional]|
**offset** | **StrictInt** | <em>offset in the results array of returned redirect chains</em><br>optional field<br>default value: <code>0</code><br>maximum value: <code>2000000</code><br>if you specify the <code>10</code> value, the first ten redirect chains in the results array will be omitted and the data will be provided for the successive redirect chains |[optional]|
**filters** | **List[Optional[Any]]** | <em>array of results filtering parameters</em><br>optional field<br><strong>you can use only one filtering parameter with this endpoint</strong><p>the following filtering parameter is supported:<br><code>is_redirect_loop</code><br>the following operators are supported:<br><code>regex</code>, <code>not_regex</code>, <code>=</code>, <code>&lt;&gt;</code><p>examples:<br><code>['is_redirect_loop','=','true']</code><p><code>['is_redirect_loop','&lt;&gt;','false']</code> |[optional]|
**tag** | **StrictStr** | <em>user-defined task identifier</em><br>optional field<br><em>the character limit is 255</em><br>you can use this parameter to identify the task and match it with the result<br>you will find the specified <code>tag</code> value in the <code>data</code> object of the response |[optional]|