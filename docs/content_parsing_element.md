# ContentParsingElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**fetch_time** | **StrictStr** | <em>date and time when the content was fethced</em><br>            example:<br>            <code>'2022-11-01 10:02:52 +00:00'</code> |[optional]|
**status_code** | **StrictInt** | <i>general status code</i><br>            you can find the full list of the response codes <a href='/v3/appendix/errors'>here</a><br>            <strong>Note:</strong> we strongly recommend designing a necessary system for handling related exceptional or error conditions |[optional]|
**page_content** | **PageContentInfo** | <em>parsed content of the page</em><br> |[optional]|
**page_as_markdown** | **StrictStr** | <em>page content in the markdown format</em><br>            page content in the <a href='https://daringfireball.net/projects/markdown/' target='_blank'>text-to-HTML markdown format</a><br>            specify <code>markdown_view</code> as <code>true</code> in the request to return the value |[optional]|