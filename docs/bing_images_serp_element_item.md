# BingImagesSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | title of the result in SERP |[optional]|
**url** | **StrictStr** | relevant URL |[optional]|
**items** | **List[Optional[AiModeImagesElementInfo]]** | additional items present in the element<br>if there are none, equals null |[optional]|
**related_image_searches** | **List[Optional[RelatedImageSearchesElement]]** | contains keywords and images related to the specified search term<br>if there are none, equals null |[optional]|