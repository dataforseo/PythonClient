# StocksBoxSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values;<br>positions of elements with different type values are omitted from rank_group;<br>always equals 0 for desktop |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP<br>always equals 0 for desktop |[optional]|
**title** | **StrictStr** | title of a given link element |[optional]|
**source** | **StrictStr** | reference source name or title |[optional]|
**snippet** | **StrictStr** | description of the shopping element |[optional]|
**price** | **PriceInfo** | price of the shopping element |[optional]|
**url** | **StrictStr** | URL |[optional]|
**domain** | **StrictStr** | domain name of the reference |[optional]|
**table** | **Table** | table present in the element<br>the header and content of the table present in the element |[optional]|
**graph** | **Graph** | contains data provided in the graph of the element |[optional]|