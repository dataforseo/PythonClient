# OnPageUncrawlableResourcesItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**url** | **StrictStr** | URL of the uncrawlable resource |[optional]|
**reason** | **StrictStr** | reason the resource is uncrawlablecan take the following values: content_type_inconsistency |[optional]|
**status_code** | **StrictInt** | HTTP response code returned by the uncrawlable resourcepossible values: 200 |[optional]|
**fetch_time** | **StrictStr** | date and time when the resource was fetchedin the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”example:2026-03-09 18:20:32 +00:00 |[optional]|
**meta** | **UncrawlableResourcesMeta** | metadata of the uncrawlable resource |[optional]|