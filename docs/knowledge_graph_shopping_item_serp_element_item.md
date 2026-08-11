# KnowledgeGraphShoppingItemSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | <em>group rank in SERP</em><br>position within a group of elements with identical <code>type</code> values;<br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code>;<br>always equals <code>0</code> for <code>desktop</code> |[optional]|
**rank_absolute** | **StrictInt** | <em>absolute rank in SERP</em><br>absolute position among all the elements in SERP<br>always equals <code>0</code> for <code>desktop</code> |[optional]|
**title** | **StrictStr** | <em>title of the row</em> |[optional]|
**data_attrid** | **StrictStr** | <em>google defined data attribute ID</em><br>example:<br><code>action:listen_artist</code> |[optional]|
**items** | **List[Optional[KnowledgeGraphShoppingElement]]** | <em>contains arrays of elements available in the list</em> |[optional]|