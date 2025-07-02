# ImageLinkElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**link_attribute** | **List[Optional[StrictStr]]** | link attribute added to external link<br>indicates link attributes added to the link_to on the page_from<br>example:<br>['ugc','noopener'] |[optional]|
**text** | **StrictStr** | anchor text |[optional]|
**image_alt** | **StrictStr** | alternative text for the image |[optional]|
**image_src** | **StrictStr** | url of the image |[optional]|
**page_to_status_code** | **StrictInt** | status code of the referenced page<br>status code of the page to which the link is pointing |[optional]|