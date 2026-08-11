# OnPageRawHtmlRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**id** | **StrictStr** | <em>ID of the task</em><br><strong>required field</strong><br>you can get this ID in the response of the <a href='/v3/on_page/task_post/'>Task POST</a> endpoint<br>example:<br>'07131248-1535-0216-1000-17384017ad04' |[optional]|
**url** | **StrictStr** | <em>page url</em><br><strong>required field</strong><br>the absolute URL of a page to request HTML<br><strong>Note:</strong> this field is optional if the task was set using the <a href='/v3/on_page/instant_pages/'>Instant Pages endpoint</a> |[optional]|