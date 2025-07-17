# SerpApiGoogleImagesCarouselElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**position** | **StrictStr** | the alignment of the element in SERP<br>can take the following values:<br>left, right |[optional]|
**title** | **StrictStr** | title of the element |[optional]|
**items** | **List[Optional[SerpApiCarouselElement]]** | items of the element |[optional]|
**rectangle** | **RectangleInfo** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP<br>note: calculate_rectangles parameter is not yet available when setting tasks for this search engine type, that’s why rectangle always equals null |[optional]|