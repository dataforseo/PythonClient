# DataforseoLabsCategoriesResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**category_code** | **StrictInt** | category code |[optional]|
**category_name** | **StrictStr** | full name of the category |[optional]|
**category_code_parent** | **StrictInt** | the code of the superordinate category<br>example:<br>'category_code': 10178,<br>'category_name': 'Apparel Accessories',<br>'category_code_parent': 10021<br>where category_code_parent<br>corresponds to:<br>'category_code': 10021,<br>'category_name': 'Apparel'<br>'category_code_parent': null |[optional]|