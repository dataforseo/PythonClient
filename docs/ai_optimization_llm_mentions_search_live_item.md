# AiOptimizationLlmMentionsSearchLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**platform** | **StrictStr** | platform received in a POST array |[optional]|
**location_code** | **StrictInt** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**question** | **StrictStr** | relevant question |[optional]|
**answer** | **StrictStr** | relevant answer in markdown formatcontent of the result formatted in the markdown markup language |[optional]|
**sources** | **List[Optional[Sources]]** | array of sourcesthe sources the model cited or relied on in its final answer |[optional]|
**search_results** | **List[Optional[SearchResults]]** | array of search resultsall web search outputs the model retrieved when looking up information, including duplicates and unused entries |[optional]|
**ai_search_volume** | **StrictInt** | current AI search volume rate of a keywordlearn more about this metric here |[optional]|
**monthly_searches** | **List[Optional[MonthlySearchesInfo]]** | monthly AI search volume ratesarray of objects with AI search volume rates in a certain month of a year |[optional]|
**first_response_at** | **StrictStr** | date and time when the response data was first recordedin the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”example:2025-10-21 06:25:30 +00:00 |[optional]|
**last_response_at** | **StrictStr** | date and time when the response data was last updatedin the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”example:2025-10-21 06:25:30 +00:00 |[optional]|
**brand_entities** | **List[Optional[BrandEntities]]** | array of brand entitiescontains information on brands mentioned in the response |[optional]|
**fan_out_queries** | **List[Optional[StrictStr]]** | array of fan-out queriescontains related search queries derived from the main query to provide a more comprehensive response |[optional]|