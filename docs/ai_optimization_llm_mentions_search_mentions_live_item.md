# AiOptimizationLlmMentionsSearchMentionsLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**platform** | **StrictStr** | platform received in a POST array |[optional]|
**model_name** | **StrictStr** | name of the AI model from which the data was retrieved<br>Note: for the google platform type, the value is always google_ai_overview |[optional]|
**location_code** | **StrictInt** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**question** | **StrictStr** | relevant question |[optional]|
**answer** | **StrictStr** | relevant answer in markdown format<br>content of the result formatted in the markdown markup language |[optional]|
**sources** | **List[Optional[Sources]]** | array of sources<br>the sources the model cited or relied on in its final answer<br>learn more about the sources and how to retrieve LLM citation data at our Help Center |[optional]|
**search_results** | **List[Optional[SearchResults]]** | array of search results<br>all web search outputs the model retrieved when looking up information, including duplicates and unused entries |[optional]|
**ai_search_volume** | **StrictInt** | current AI search volume rate of a keyword<br>learn more about this metric here |[optional]|
**monthly_searches** | **List[Optional[MonthlySearchesInfo]]** | monthly AI search volume rates<br>array of objects with AI search volume rates in a certain month of a year |[optional]|
**first_response_at** | **StrictStr** | date and time when the response data was first recorded<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2025-10-21 06:25:30 +00:00 |[optional]|
**last_response_at** | **StrictStr** | date and time when the response data was last updated<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2025-10-21 06:25:30 +00:00 |[optional]|
**brand_entities** | **List[Optional[BrandEntities]]** | array of brand entities<br>contains information on brands mentioned in the response |[optional]|
**fan_out_queries** | **List[Optional[StrictStr]]** | array of fan-out queries<br>contains related search queries derived from the main query to provide a more comprehensive response |[optional]|
**is_web_search_based** | **StrictBool** | indicates whether the response was generated using web search results<br>if true, the model retrieved live web search results to produce the response<br>if false, the response was generated from the model's internal knowledge |[optional]|