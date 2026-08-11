# ImagesSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | <em>group rank in SERP</em><br>position within a group of elements with identical <code>type</code> values;<br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code>;<br>always equals <code>0</code> for <code>desktop</code> |[optional]|
**rank_absolute** | **StrictInt** | <em>absolute rank in SERP</em><br>absolute position among all the elements in SERP<br>always equals <code>0</code> for <code>desktop</code> |[optional]|
**title** | **StrictStr** | <em>title of the row</em> |[optional]|
**url** | **StrictStr** | <i>URL of the third-party review source</i> |[optional]|
**items** | **List[Optional[AiModeImagesElementInfo]]** | <em>contains arrays of elements available in the list</em> |[optional]|
**related_image_searches** | **List[Optional[RelatedImageSearchesElement]]** | <em>contains keywords and images related to the specified search term</em><br><strong>Note:</strong> this array is deprecated and always returns <code>null</code> |[optional]|