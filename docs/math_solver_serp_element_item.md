# MathSolverSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values;<br>positions of elements with different type values are omitted from rank_group;<br>always equals 0 for desktop |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP<br>always equals 0 for desktop |[optional]|
**title** | **StrictStr** | reference page title |[optional]|
**result** | **StrictStr** | solution to the equation<br>solution to the mathematical equation specified in the keyword field when setting a task |[optional]|
**items** | **List[Optional[MathSolverElement]]** | contains arrays of specific images |[optional]|
**links** | **List[Optional[LinkElement]]** | link of the element |[optional]|