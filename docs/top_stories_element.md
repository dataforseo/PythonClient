# TopStoriesElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**source** | **StrictStr** | reference source name or title |[optional]|
**domain** | **StrictStr** | domain where a link points |[optional]|
**title** | **StrictStr** | title of a given link element |[optional]|
**date** | **StrictStr** | the date when the page source of the element was published |[optional]|
**amp_version** | **StrictBool** | Accelerated Mobile Pages<br>indicates whether an item has the Accelerated Mobile Page (AMP) version |[optional]|
**timestamp** | **StrictStr** | date and time when the result was published<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**url** | **StrictStr** | source URL |[optional]|
**image_url** | **StrictStr** | URL of the image<br>the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available) |[optional]|
**badges** | **List[Optional[StrictStr]]** | badges relevant to the element |[optional]|