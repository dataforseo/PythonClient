# ShoppingSpecification


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank on the product specification page<br>absolute position among all the elements found on the product specification page |[optional]|
**position** | **StrictStr** | alignment of the element on the product specification page<br>can take the following values:<br>right |[optional]|
**xpath** | **StrictStr** | XPath of the element |[optional]|
**block_name** | **StrictStr** | name of the block of product attributes<br>indicates the name of the product specification section in which the related element is listed |[optional]|
**specification_name** | **StrictStr** | product attribute<br>attribute name of the product data specification |[optional]|
**specification_value** | **StrictStr** | content of the specification |[optional]|