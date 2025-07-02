# AmazonAmazonProductInfoSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**position** | **StrictStr** | the alignment of the element in Amazon SERP<br>possible values:<br>left, right |[optional]|
**title** | **StrictStr** | product title |[optional]|
**details** | **StrictStr** | product specs and other details |[optional]|
**image_url** | **StrictStr** | the URL of the product image |[optional]|
**author** | **StrictStr** | product brand name |[optional]|
**data_asin** | **StrictStr** | ASIN of the product received in a POST array |[optional]|
**parent_asin** | **StrictStr** | parent ASIN of the product |[optional]|
**product_asins** | **List[Optional[StrictStr]]** | ASINs of all found product modifications |[optional]|
**price_from** | **StrictFloat** | the lower limit of the product price range<br>example:<br>49.98 |[optional]|
**price_to** | **StrictFloat** | the upper limit of the product price range<br>example:<br>384.99 |[optional]|
**currency** | **StrictStr** | currency in the ISO format<br>example:<br>USD |[optional]|
**is_amazon_choice** | **StrictBool** | “Amazon’s choice” label<br>if the value is true, the product is marked with the “Amazon’s choice” label |[optional]|
**rating** | **RatingElement** | product rating info |[optional]|
**is_newer_model_available** | **StrictBool** | indicates whether the newer model of the product is available |[optional]|
**applicable_vouchers** | **List[Optional[AmazonApplicableVouchersItem]]** | array of objects containing information about applicable vouchers |[optional]|
**newer_model** | **AmazonProductNewerModelInfo** | information about the newer model of the product |[optional]|
**categories** | **List[Optional[ProductCategoryInfo]]** | contains related product categories |[optional]|
**product_information** | **List[Optional[BaseProductInformationItem]]** | contains related product information |[optional]|
**product_images_list** | **List[Optional[StrictStr]]** | contains URLs for all images of the product displayed on the left side of the main image |[optional]|
**product_videos_list** | **List[Optional[StrictStr]]** | contains URLs for all videos of the product displayed on the right side of the main video |[optional]|
**description** | **StrictStr** | contains description of the product |[optional]|
**is_available** | **StrictBool** | indicates whether the product is available for ordering<br>if the value is true, the product can be ordered |[optional]|
**top_local_reviews** | **List[Optional[BaseAmazonSerpElementItem]]** | array of objects with top reviews from target location<br>to obtain additional local reviews, you can specify the load_more_local_reviews parameter in Task POST |[optional]|
**top_global_reviews** | **List[Optional[BaseAmazonSerpElementItem]]** | array of objects with top reviews from around the world |[optional]|