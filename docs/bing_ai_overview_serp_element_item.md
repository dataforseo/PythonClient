# BingAiOverviewSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**markdown** | **StrictStr** | <em>content of the element in markdown format</em> |[optional]|
**items** | **List[Optional[BaseSerpApiBingAiOverviewElementItem]]** | <em>additional items present in the element</em><br>            if there are none, equals <code>null</code> |[optional]|
**references** | **List[Optional[AiModeAiOverviewReferenceInfo]]** | <em>additional references relevant to the item</em><br>            includes references to webpages that may have been used to generate the <code>ai_overview</code> |[optional]|