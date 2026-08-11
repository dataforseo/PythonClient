# DataLabsMathSolverSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | <em>title of the result in SERP</em> |[optional]|
**result** | **StrictStr** | <em>solution to the equation</em><br>            solution to the mathematical equation specified in the <code>keyword</code> field when setting a task |[optional]|
**items** | **List[Optional[MathSolverElement]]** | <em>historical SERPs and related data found in the database</em> |[optional]|
**links** | **List[Optional[LinkElement]]** | <em>sitelinks</em><br>            the links shown below some of Google's search results<br>            if there are none, equals <code>null</code> |[optional]|