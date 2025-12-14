# AiOptimizationLlmMentionssLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**key** | **StrictStr** | URL of a found page<br>the URL of a page found in LLM mentions for the specified target |[optional]|
**location** | **List[Optional[GroupElement]]** | location-based grouping<br>array of objects containing page mention metrics segmented by geographical location |[optional]|
**language** | **List[Optional[GroupElement]]** | language-based grouping<br>array of objects containing page mention metrics segmented by content language |[optional]|
**platform** | **List[Optional[GroupElement]]** | platform-based grouping<br>array of group elements containing page mention metrics segmented by AI platform |[optional]|
**sources_domain** | **List[Optional[GroupElement]]** | source domains relevant to the specific page<br>array of objects containing data on domains that are cited as sources in LLM responses |[optional]|
**search_results_domain** | **List[Optional[GroupElement]]** | search results domains relevant to the specific page<br>array of objects containing data on domains that appear in search results related to LLM queries |[optional]|
**brand_entities_title** | **List[Optional[GroupElement]]** | data on brand entities relevant to the target<br>array of objects containing data on brand entity titles that appear in search results related to LLM queries |[optional]|
**brand_entities_category** | **List[Optional[GroupElement]]** | data on brand entities relevant to the target<br>array of objects containing data on brand entity categories that appear in search results related to LLM queries |[optional]|