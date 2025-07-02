# DataforseoTrendsDemographyInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**position** | **StrictInt** | the alignment of the element<br>can take the following values: 1, 2, 3, 4, etc. |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**keywords** | **List[Optional[StrictStr]]** | relevant keywords<br>the data included in the demography and demography_comparison is based on the keywords listed in this array |[optional]|
**demography** | **Demography** | demographic breakdown of keyword popularity data per each specified term<br>conains keyword popularity data by age and gender |[optional]|
**demography_comparison** | **DemographyComparisonInfo** | comparison of demographic data on keyword popularity for the specified parameters<br>conains keyword popularity data by age and gender<br>if you specified a single keyword, the value will be null |[optional]|