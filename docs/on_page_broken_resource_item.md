# OnPageBrokenResourceItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**fetch_timing** | **FetchTiming** | <em>time range within which a result was fetched</em> |[optional]|
**is_resource** | **StrictBool** | <em>indicates whether a page is a single resource</em> |[optional]|
**meta** | **PageMetaInfo** | <em>resource properties</em><br>the value depends on the <code>resource_type</code><br>note that if you do not indicate a <code>url</code> when setting a task, resource's <code>meta</code> is returned based on the data from the page where our crawler first saw the resource;<br>to obtain resource's <code>meta</code> from a particular <code>url</code>, specify that URL when setting a task |[optional]|
**accept_type** | **StrictStr** | <em>indicates the expected type of resource</em><br>for example, if <code>'resource_type': 'broken'</code>, <code>accept_type</code> will indicate the type of the broken resource<br>possible values: <br><code>any</code>, <code>none</code>, <code>image</code>, <code>sitemap</code>, <code>robots</code>, <code>script</code>, <code>stylesheet</code>, <code>redirect</code>, <code>html</code>, <code>text</code>, <code>other</code>, <code>font</code> |[optional]|