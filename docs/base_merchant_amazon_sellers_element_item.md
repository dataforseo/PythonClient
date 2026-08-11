# BaseMerchantAmazonSellersElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | <em>position within a group of elements with identical <code>type</code> values</em><br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em> absolute rank in SERP</em><br>absolute position among all the elements found in Amazon Sellers SERP |[optional]|
**position** | **StrictStr** | <em>alignment of the element in SERP</em><br>possible values:<br><code>left</code>, <code>right</code> |[optional]|
**xpath** | **StrictStr** | <em><a href='https://en.wikipedia.org/wiki/XPath'>XPath</a> of the element</em> |[optional]|
**seller_name** | **StrictStr** | <em>business name of the seller</em> |[optional]|
**seller_url** | **StrictStr** | <em>url forwarding to the seller's page on Amazon</em> |[optional]|
**ships_from** | **StrictStr** | <em>sender company name</em> |[optional]|
**price** | **PriceInfo** | <em>product pricing details</em><br>if there are no details, the value will be <code>null</code> |[optional]|
**percentage_discount** | **StrictFloat** | <em>value of the percentage discount</em> |[optional]|
**applicable_vouchers** | **List[Optional[AmazonApplicableVouchersItem]]** | <em>array of objects containing information about applicable vouchers</em> |[optional]|
**rating** | **RatingElement** | <em>seller rating details</em><br>seller popularity rate based on customer reviews |[optional]|
**condition** | **StrictStr** | <em>product condition</em><br>condition of the product offered by the seller |[optional]|
**condition_description** | **StrictStr** | <em>product condition details</em><br>expanded details on the condition of the product offered by the seller |[optional]|
**delivery_info** | **AmazonDeliveryInfo** | <em>delivery information</em><br>delivery information including free and fast delivery date ranges |[optional]|