# DataforseoLabsCategoriesResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**category_code** | **StrictInt** | <em>category code</em> |[optional]|
**category_name** | **StrictStr** | <em>full name of the category</em> |[optional]|
**category_code_parent** | **StrictInt** | <em>the code of the superordinate category</em><br>example:<br>`'category_code': 10178`,<br>`'category_name': 'Apparel Accessories'`,<br>`'category_code_parent': 10021`<br>where `category_code_parent`<br>corresponds to: <br>`'category_code': 10021`,<br>`'category_name': 'Apparel'`<br>`'category_code_parent': null` |[optional]|