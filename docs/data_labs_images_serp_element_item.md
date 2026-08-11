# DataLabsImagesSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | <em>title of the result in SERP</em> |[optional]|
**url** | **StrictStr** | <em> relevant URL in SERP</em> |[optional]|
**items** | **List[Optional[AiModeImagesElementInfo]]** | <em>historical SERPs and related data found in the database</em> |[optional]|
**related_image_searches** | **RelatedImageSearchesElement** | <em>contains keywords and images related to the specified search term</em><br>            if there are none, equals <code>null</code> |[optional]|