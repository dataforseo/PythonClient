# BaseAppDataSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictFloat** | position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictFloat** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**position** | **StrictStr** | the alignment of the element in SERP<br>can take the following values:<br>left, right |[optional]|
**title** | **StrictStr** | title of the app |[optional]|
**rating** | **BusinessDataRatingInfo** | average rating of the app |[optional]|