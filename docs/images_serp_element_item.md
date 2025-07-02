# ImagesSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**position** | **StrictStr** | the alignment of the element in SERP<br>can take the following values:<br>left, right |[optional]|
**xpath** | **StrictStr** | the XPath of the element |[optional]|
**title** | **StrictStr** | title of the row |[optional]|
**url** | **StrictStr** | source URL |[optional]|
**items** | **List[Optional[ImagesElement]]** | contains arrays of specific images |[optional]|
**related_image_searches** | **List[Optional[RelatedImageSearchesElement]]** | contains keywords and images related to the specified search term<br>if there are none, equals null |[optional]|
**rectangle** | **Rectangle** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP<br>equals null if calculate_rectangles in the POST request is not set to true |[optional]|