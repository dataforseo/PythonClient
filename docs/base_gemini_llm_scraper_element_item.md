# BaseGeminiLlmScraperElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | group rank in SERPposition within a group of elements with identical type valuespositions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERPabsolute position among all the elements in SERP |[optional]|
**markdown** | **StrictStr** | content of the element in markdown formatcontent of the result formatted in the markdown markup language |[optional]|