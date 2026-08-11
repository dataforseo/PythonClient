# SerpApiKnowledgeGraphImagesItemElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | <em>group rank in SERP</em><br>position within a group of elements with identical <code>type</code> values<br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em>absolute rank in SERP</em><br>absolute position among all the elements in SERP |[optional]|
**link** | **LinkElement** | <em>link of the element</em> |[optional]|
**items** | **List[Optional[KnowledgeGraphImagesElement]]** | <em>additional items present in the element</em><br>if there are none, equals <code>null</code> |[optional]|