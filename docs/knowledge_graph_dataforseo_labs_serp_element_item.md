# KnowledgeGraphDataforseoLabsSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | search engine type |[optional]|
**title** | **StrictStr** | title of the result in SERP |[optional]|
**sub_title** | **StrictStr** | subtitle of the item |[optional]|
**description** | **StrictStr** | description of the results element in SERP |[optional]|
**card_id** | **StrictStr** | card id |[optional]|
**url** | **StrictStr** | relevant URL in SERP |[optional]|
**image_url** | **StrictStr** | URL of the image from knowledge graph |[optional]|
**logo_url** | **StrictStr** | URL of the logo from knowledge graph |[optional]|
**cid** | **StrictStr** | google-defined client id |[optional]|
**items** | **List[Optional[BaseDataforseoLabsSerpElementItem]]** | additional items present in the element<br>if there are none, equals null |[optional]|