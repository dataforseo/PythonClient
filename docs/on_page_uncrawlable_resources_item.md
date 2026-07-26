# OnPageUncrawlableResourcesItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**url** | **StrictStr** | <em>URL of the uncrawlable resource</em> |[optional]|
**reason** | **StrictStr** | <em>reason the resource is uncrawlable</em><br>can take the following values: <code>content_type_inconsistency</code> |[optional]|
**status_code** | **StrictInt** | <i>general status code</i><br>you can find the full list of the response codes <a href='/v3/appendix/errors'>here</a><br><strong>Note:</strong> we strongly recommend designing a necessary system for handling related exceptional or error conditions |[optional]|
**fetch_time** | **StrictStr** | <em>date and time when the resource was fetched</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code>2026-03-09 18:20:32 +00:00</code> |[optional]|
**meta** | **UncrawlableResourcesMeta** | <em>metadata of the uncrawlable resource</em> |[optional]|