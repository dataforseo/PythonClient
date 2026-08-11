# BingImagesSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | <em>title of the item</em> |[optional]|
**url** | **StrictStr** | <em>URL</em> |[optional]|
**items** | **List[Optional[AiModeImagesElementInfo]]** | <em>contains results featured in the 'hotels_pack' element of SERP</em> |[optional]|
**related_image_searches** | **List[Optional[RelatedImageSearchesElement]]** | <em>contains keywords and images related to the specified search term</em><br>            if there are none, equals <code>null</code> |[optional]|