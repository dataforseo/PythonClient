# OnPageContentParsingRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**url** | **StrictStr** | <em>URL of the content to parse</em><br><strong>required field</strong><br>URL of the page to parse<br>example:<br>`https://dataforseo.com/blog/a-versatile-alternative-to-google-trends-exploring-the-power-of-dataforseo-trends-api` |[optional]|
**id** | **StrictStr** | <em>ID of the task</em><br><strong>required field</strong><br>you can get this ID in the response of the <a href='/v3/on_page/task_post/'>Task POST</a> endpoint<br><strong>note:</strong> the <code>enable_content_parsing</code> parameter in the POST request must be set to <code>true</code><br>example:<br><code>'07131248-1535-0216-1000-17384017ad04'</code> |[optional]|
**markdown_view** | **StrictBool** | <em>return page content as markdown</em><br>optional field<br>if set to <code>true</code>, the markdown-formatted content of the page will be returned in the <code>page_as_markdown</code> field of the response;<br>default value: <code>false</code> |[optional]|