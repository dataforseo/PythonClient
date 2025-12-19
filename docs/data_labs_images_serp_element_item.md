# DataLabsImagesSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | title of the result in SERP |[optional]|
**url** | **StrictStr** | sitelink URL |[optional]|
**items** | **List[Optional[AiModeImagesElementInfo]]** | historical SERPs and related data found in the database |[optional]|
**related_image_searches** | **RelatedImageSearchesElement** | contains keywords and images related to the specified search term<br>if there are none, equals null |[optional]|