# OnPageWaterfallRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**id** | **StrictStr** | <em>ID of the task</em><br><strong>required field</strong><br>you can get this ID in the response of the <a href='/v3/on_page/task_post/'>Task POST</a> endpoint<br>example:<br>'07131248-1535-0216-1000-17384017ad04' |[optional]|
**url** | **StrictStr** | <em>page URL</em><br><strong>required field</strong><br>specify the pages you want to receive timing for |[optional]|
**tag** | **StrictStr** | <em>user-defined task identifier</em><br>optional field<br><em>the character limit is 255</em><br>you can use this parameter to identify the task and match it with the result<br>you will find the specified <code>tag</code> value in the <code>data</code> object of the response |[optional]|