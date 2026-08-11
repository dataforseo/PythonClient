# OnPageScriptResourceItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**meta** | **ResourceMetaInfo** |  |[optional]|
**fetch_timing** | **FetchTiming** | <em>time range within which a result was fetched</em> |[optional]|
**accept_type** | **StrictStr** | <em>indicates the expected type of resource</em><br>for example, if <code>'resource_type': 'broken'</code>, <code>accept_type</code> will indicate the type of the broken resource<br>possible values:<br><code>any</code>, <code>none</code>, <code>image</code>, <code>sitemap</code>, <code>robots</code>, <code>script</code>, <code>stylesheet</code>, <code>redirect</code>, <code>html</code>, <code>text</code>, <code>other</code>, <code>font</code> |[optional]|