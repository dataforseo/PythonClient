# SerpApiGoogleImagesRelatedSearchesElementItem

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**page** | **number** |  |[optional]|
**position** | **string** | the alignment of the element in SERP<br>can take the following values:<br>left, right |[optional]|
**items** | **string[]** | items of the element |[optional]|
**rectangle** | **AiModeRectangleInfo** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP<br>note: calculate_rectangles parameter is not yet available when setting tasks for this search engine type, that’s why rectangle always equals null |[optional]|