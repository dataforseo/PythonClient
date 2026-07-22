# StocksBoxSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values;<br>positions of elements with different type values are omitted from rank_group;<br>always equals 0 for desktop |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP<br>always equals 0 for desktop |[optional]|
**title** | **StrictStr** | title of the row |[optional]|
**source** | **StrictStr** | source of the element<br>indicates the source of information included in the recipes_element |[optional]|
**snippet** | **StrictStr** | text alongside the link title |[optional]|
**price** | **PriceInfo** | price indicated in the element |[optional]|
**url** | **StrictStr** | URL of the third-party review source |[optional]|
**domain** | **StrictStr** | domain of the website hosting the video |[optional]|
**table** | **Table** | table present in the element<br>the header and content of the table present in the element |[optional]|
**graph** | **Graph** | contains data provided in the graph of the element |[optional]|