# TopStoriesElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**source** | **StrictStr** | <em>reference source name or title</em> |[optional]|
**domain** | **StrictStr** | <em>domain where a link points</em> |[optional]|
**title** | **StrictStr** | <em>title of a given link element</em> |[optional]|
**date** | **StrictStr** | <em>the date when the page source of the element was published</em> |[optional]|
**amp_version** | **StrictBool** | <em>Accelerated Mobile Pages</em><br>indicates whether an item has the Accelerated Mobile Page (AMP) version |[optional]|
**timestamp** | **StrictStr** | <em>date and time when the result was published</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**url** | **StrictStr** | <em>source URL</em> |[optional]|
**image_url** | **StrictStr** | <em>URL of the image</em><br>the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available) |[optional]|
**badges** | **List[Optional[StrictStr]]** | <em>badges relevant to the element</em> |[optional]|