# SerpApiKnowledgeGraphRowItemElementItem

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **number** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **number** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**title** | **string** | title of the item |[optional]|
**data_attrid** | **string** | google defined data attribute ID<br>example:<br>kc:/common/topic:social media presence |[optional]|
**text** | **string** | reference text<br>text snippet from the page that was used to generate the ai_overview_element |[optional]|
**links** | **LinkElement[]** | links featured in the faq_box_element |[optional]|