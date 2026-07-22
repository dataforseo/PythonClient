# KnowledgeGraphSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**title** | **StrictStr** | title of the result in SERP |[optional]|
**subtitle** | **StrictStr** | subtitle of the item |[optional]|
**description** | **StrictStr** | description of the results element in SERP |[optional]|
**card_id** | **StrictStr** | card id |[optional]|
**url** | **StrictStr** | relevant URL in SERP |[optional]|
**image_url** | **StrictStr** | URL of the image<br>the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available) |[optional]|
**logo_url** | **StrictStr** | URL of the logo from knowledge graph |[optional]|
**cid** | **StrictStr** | google-defined client id<br>unique id of a local establishment;<br>can be used with Google Reviews API to get a full list of reviews |[optional]|
**items** | **List[Optional[BaseSerpApiKnowledgeGraphElementItem]]** | additional items present in the element<br>if there are none, equals null |[optional]|