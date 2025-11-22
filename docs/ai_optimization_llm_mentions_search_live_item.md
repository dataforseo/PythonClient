# AiOptimizationLlmMentionsSearchLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**platform** | **StrictStr** | platform received in a POST array |[optional]|
**location_code** | **StrictInt** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**question** | **StrictStr** | relevant question |[optional]|
**answer** | **StrictStr** | relevant answer in markdown format<br>content of the result formatted in the markdown markup language |[optional]|
**sources** | **List[Optional[Sources]]** | array of sources<br>the sources the model cited or relied on in its final answer |[optional]|
**search_results** | **List[Optional[SearchResults]]** | array of search results<br>all web search outputs the model retrieved when looking up information, including duplicates and unused entries |[optional]|
**ai_search_volume** | **StrictInt** | current AI search volume rate of a keyword<br>learn more about this metric here |[optional]|
**monthly_searches** | **List[Optional[MonthlySearchesInfo]]** |  |[optional]|