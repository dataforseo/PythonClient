# SerpApiPeopleAlsoAskAiOverviewExpandedElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**items** | **List[Optional[BaseSerpApiAiOverviewElementItem]]** | <em>items present in the element</em> |[optional]|
**references** | **List[Optional[AiModeAiOverviewReferenceInfo]]** | <em>additional references relevant to the item</em><br>includes references to webpages that may have been used to generate the <code>ai_overview</code> |[optional]|
**asynchronous_ai_overview** | **StrictBool** | <em>indicates whether the element is loaded asynchronously</em><br>if <code>true</code>, the <code>people_also_ask_ai_overview_expanded_element</code> element is loaded asynchronously;<br>if <code>false</code>, the <code>people_also_ask_ai_overview_expanded_element</code> element is loaded from cache |[optional]|