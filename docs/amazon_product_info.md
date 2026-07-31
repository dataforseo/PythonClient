# AmazonProductInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | <em>position within a group of elements with identical <code>type</code> values</em><br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em> absolute rank</em><br>absolute position among all the elements in the response array |[optional]|
**position** | **StrictStr** | <em>the alignment of the element in Amazon SERP</em><br>possible values:<br><code>left</code>, <code>right</code> |[optional]|
**xpath** | **StrictStr** | <em>the <a href='https://en.wikipedia.org/wiki/XPath'>XPath</a> of the element</em> |[optional]|
**title** | **StrictStr** | <em>product title</em> |[optional]|
**details** | **StrictStr** | <em>product specs and other details</em> |[optional]|
**image_url** | **StrictStr** | <em>the URL of the product image</em> |[optional]|
**author** | **StrictStr** | <em>product brand name</em> |[optional]|
**data_asin** | **StrictStr** | <em>ASIN of the product received in a POST array</em> |[optional]|
**parent_asin** | **StrictStr** | <em><a href='https://sellercentral.amazon.com/gp/help/external/help.html?itemID=8831&amp;language=en-US&amp;ref=mpbc_200779220_cont_8831&amp;' target='_blank' rel='noopener noreferrer'>parent ASIN</a> of the product</em> |[optional]|
**product_asins** | **List[Optional[StrictStr]]** | <em>ASINs of all found product modifications</em> |[optional]|
**price_from** | **StrictFloat** | <em>the lower limit of the product price range</em><br>example:<br><code>49.98</code> |[optional]|
**price_to** | **StrictFloat** | <em>the upper limit of the product price range</em><br>example:<br><code>384.99</code> |[optional]|
**percentage_discount** | **StrictStr** | <em>value of the percentage discount</em> |[optional]|
**currency** | **StrictStr** | <em>currency in the <a href='https://en.wikipedia.org/wiki/ISO_4217'>ISO</a> format</em><br>example:<br><code>USD</code> |[optional]|
**is_amazon_choice** | **StrictBool** | <em>'Amazon's choice' label</em><br>if the value is <code>true</code>, the product is marked with the 'Amazon's choice' label |[optional]|
**rating** | **RatingElement** | <em>product rating info</em> |[optional]|
**is_newer_model_available** | **StrictBool** | <em>indicates whether the newer model of the product is available</em> |[optional]|
**is_prime_video** | **StrictBool** | <em>indicates whether a product has an Amazon Prime Video label</em><br>if <code>true</code>, specified product is a part of Amazon Prime Video service |[optional]|
**applicable_vouchers** | **List[Optional[AmazonApplicableVouchersItem]]** | <em>array of objects containing information about applicable vouchers</em> |[optional]|
**newer_model** | **NewerModel** | <em>information about the newer model of the product</em> |[optional]|
**categories** | **List[Optional[Categories]]** | <em>contains related product categories</em> |[optional]|
**product_information** | **List[Optional[BaseMerchantAmazonProductInformationElementItem]]** | <em>contains related product information</em> |[optional]|
**product_images_list** | **List[Optional[StrictStr]]** | <em>contains URLs for all images of the product displayed on the left side of the main image</em> |[optional]|
**product_videos_list** | **List[Optional[StrictStr]]** | <em>contains URLs for all videos of the product displayed on the right side of the main video</em> |[optional]|
**description** | **StrictStr** | <em>contains description of the product</em> |[optional]|
**is_available** | **StrictBool** | <em>indicates whether the product is <a href='https://www.amazon.com/gp/help/customer/display.html?nodeId=201910280' rel='noopener noreferrer' target='_blank'>available for ordering</a></em><br>if the value is <code>true</code>, the product can be ordered |[optional]|
**top_local_reviews** | **List[Optional[AmazonReviewItem]]** | <em>array of objects with top reviews from target location</em> |[optional]|
**top_global_reviews** | **List[Optional[AmazonReviewItem]]** | <em>array of objects with top reviews from around the world</em> |[optional]|