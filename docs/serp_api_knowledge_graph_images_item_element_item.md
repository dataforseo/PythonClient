# SerpApiKnowledgeGraphImagesItemElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**link** | **LinkElement** | link of the element |[optional]|
**items** | **List[Optional[KnowledgeGraphImagesElement]]** | items featured in the faq_box |[optional]|