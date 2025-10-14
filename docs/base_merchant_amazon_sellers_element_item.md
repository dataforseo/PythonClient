# BaseMerchantAmazonSellersElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements found in Amazon Sellers SERP |[optional]|
**position** | **StrictStr** | alignment of the element in SERP<br>possible values:<br>left, right |[optional]|
**xpath** | **StrictStr** | XPath of the element |[optional]|
**seller_name** | **StrictStr** | business name of the seller |[optional]|
**seller_url** | **StrictStr** | url forwarding to the seller’s page on Amazon |[optional]|
**ships_from** | **StrictStr** | sender company name |[optional]|
**price** | **PriceInfo** | product pricing details<br>if there are no details, the value will be null |[optional]|
**percentage_discount** | **StrictFloat** | value of the percentage discount |[optional]|
**applicable_vouchers** | **List[Optional[AmazonApplicableVouchersItem]]** | array of objects containing information about applicable vouchers |[optional]|
**rating** | **RatingElement** | seller rating details<br>seller popularity rate based on customer reviews |[optional]|
**condition** | **StrictStr** | product condition<br>condition of the product offered by the seller |[optional]|
**condition_description** | **StrictStr** | product condition details<br>expanded details on the condition of the product offered by the seller |[optional]|
**delivery_info** | **AmazonDeliveryInfo** | delivery information<br>delivery information including free and fast delivery date ranges |[optional]|