# MathSolverSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | title of the row |[optional]|
**result** | **StrictStr** | solution to the equation<br>solution to the mathematical equation specified in the keyword field when setting a task |[optional]|
**items** | **List[Optional[MathSolverElement]]** | contains arrays of specific images |[optional]|
**links** | **List[Optional[LinkElement]]** | link of the element |[optional]|
**rectangle** | **Rectangle** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP<br>equals null if calculate_rectangles in the POST request is not set to true |[optional]|