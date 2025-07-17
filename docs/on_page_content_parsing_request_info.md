# OnPageContentParsingRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**url** | **StrictStr** | URL of the content to parse<br>required field<br>URL of the page to parse<br>example:<br>https://dataforseo.com/blog/a-versatile-alternative-to-google-trends-exploring-the-power-of-dataforseo-trends-api |[optional]|
**id** | **StrictStr** | ID of the task<br>required field<br>you can get this ID in the response of the Task POST endpoint<br>note: the enable_content_parsing parameter in the POST request must be set to true<br>example:<br>'07131248-1535-0216-1000-17384017ad04' |[optional]|
**markdown_view** | **StrictBool** | return page content as markdown<br>optional field<br>if set to true, the markdown-formatted content of the page will be returned in the page_as_markdown field of the response;<br>default value: false |[optional]|