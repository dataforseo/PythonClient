# KnowledgeGraphSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**position** | **StrictStr** | the alignment of the element in SERP<br>can take the following values:<br>left, right |[optional]|
**xpath** | **StrictStr** | the XPath of the element |[optional]|
**title** | **StrictStr** | title of the result in SERP |[optional]|
**subtitle** | **StrictStr** | subtitle of the item |[optional]|
**description** | **StrictStr** | description of the results element in SERP |[optional]|
**card_id** | **StrictStr** | card id |[optional]|
**url** | **StrictStr** | relevant URL in SERP |[optional]|
**image_url** | **StrictStr** | URL of the image<br>the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available) |[optional]|
**logo_url** | **StrictStr** | URL of the logo from knowledge graph |[optional]|
**cid** | **StrictStr** | google-defined client id<br>unique id of a local establishment;<br>can be used with Google Reviews API to get a full list of reviews |[optional]|
**items** | **List[Optional[BaseSerpElementItem]]** | contains results featured in the ‘hotels_pack’ element of SERP |[optional]|
**rectangle** | **Rectangle** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP<br>equals null if calculate_rectangles in the POST request is not set to true |[optional]|