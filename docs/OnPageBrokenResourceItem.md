# OnPageBrokenResourceItem

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**fetch_timing** | **FetchTiming** | time range within which a result was fetched |[optional]|
**is_resource** | **boolean** | indicates whether a page is a single resource |[optional]|
**meta** | **PageMetaInfo** | resource properties<br>the value depends on the resource_type<br>note that if you do not indicate a url when setting a task, resource’s meta is returned based on the data from the page where our crawler first saw the resource;<br>to obtain resource’s meta from a particular url, specify that URL when setting a task |[optional]|
**accept_type** | **string** | indicates the expected type of resource<br>for example, if 'resource_type': 'broken', accept_type will indicate the type of the broken resource<br>possible values:<br>any, none, image, sitemap, robots, script, stylesheet, redirect, html, text, other, font |[optional]|