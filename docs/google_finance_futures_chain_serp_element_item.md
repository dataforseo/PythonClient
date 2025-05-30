# GoogleFinanceFuturesChainSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictFloat** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictFloat** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**markets** | **List[Optional[GoogleFinanceFuturesChainMarkets]]** | financial markets data<br>array of items containing market indexes and other financial information related to these indexes |[optional]|