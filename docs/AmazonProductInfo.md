# AmazonProductInfo

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **string** | type of element |[optional]|
**rank_group** | **number** | position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **number** | absolute rank<br>absolute position among all the elements in the response array |[optional]|
**position** | **string** | the alignment of the element in Amazon SERP<br>possible values:<br>left, right |[optional]|
**xpath** | **string** | the XPath of the element |[optional]|
**title** | **string** | product title |[optional]|
**details** | **string** | product specs and other details |[optional]|
**image_url** | **string** | the URL of the product image |[optional]|
**author** | **string** | product brand name |[optional]|
**data_asin** | **string** | ASIN of the product received in a POST array |[optional]|
**parent_asin** | **string** | parent ASIN of the product |[optional]|
**product_asins** | **string[]** | ASINs of all found product modifications |[optional]|
**price_from** | **number** | the lower limit of the product price range<br>example:<br>49.98 |[optional]|
**price_to** | **number** | the upper limit of the product price range<br>example:<br>384.99 |[optional]|
**percentage_discount** | **string** | value of the percentage discount |[optional]|
**currency** | **string** | currency in the ISO format<br>example:<br>USD |[optional]|
**is_amazon_choice** | **boolean** | “Amazon’s choice” label<br>if the value is true, the product is marked with the “Amazon’s choice” label |[optional]|
**rating** | **RatingElement** | product rating info |[optional]|
**is_newer_model_available** | **boolean** | indicates whether the newer model of the product is available |[optional]|
**applicable_vouchers** | **AmazonApplicableVouchersItem[]** | array of objects containing information about applicable vouchers |[optional]|
**newer_model** | **AmazonProductNewerModelInfo** | information about the newer model of the product |[optional]|
**categories** | **ProductCategoryInfo[]** | contains related product categories |[optional]|
**product_information** | **BaseMerchantAmazonProductInformationElementItem[]** | contains related product information |[optional]|
**product_images_list** | **string[]** | contains URLs for all images of the product displayed on the left side of the main image |[optional]|
**product_videos_list** | **string[]** | contains URLs for all videos of the product displayed on the right side of the main video |[optional]|
**description** | **string** | contains description of the product |[optional]|
**is_available** | **boolean** | indicates whether the product is available for ordering<br>if the value is true, the product can be ordered |[optional]|
**top_local_reviews** | **AmazonReviewItem[]** | array of objects with top reviews from target location<br>to obtain additional local reviews, you can specify the load_more_local_reviews parameter in Task POST |[optional]|
**top_global_reviews** | **AmazonReviewItem[]** | array of objects with top reviews from around the world |[optional]|