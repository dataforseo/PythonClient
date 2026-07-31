# ProductInfoElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | <em>position within a group of elements with identical <code>type</code> values</em><br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em>absolute rank on the product specification page</em><br>absolute position among all the elements found on the product specification page |[optional]|
**position** | **StrictStr** | <em>alignment of the element on the product specification page</em><br>can take the following values:<br><code>right</code>, <code>left</code> |[optional]|
**product_id** | **StrictStr** | <em>product_id received in a POST array</em><br>ilearn more about the parameter in <a href='https://dataforseo.com/help-center/product-id-google-shopping' rel='noopener noreferrer' target='_blank'>this help center guide</a> |[optional]|
**title** | **StrictStr** | <em>title of the product</em> |[optional]|
**description** | **StrictStr** | <em>description of the product</em> |[optional]|
**url** | **StrictStr** | <em>product url</em><br>url of the product on Google Shopping |[optional]|
**images** | **List[Optional[StrictStr]]** | <em>product images</em><br>contains urls to product images |[optional]|
**features** | **List[Optional[StrictStr]]** | <em>product features</em><br>contains snippets with the description of product features |[optional]|
**rating** | **RatingElement** | <em>product rating </em><br>the popularity rate based on reviews |[optional]|
**seller_reviews_count** | **StrictInt** | <em>number of seller reviews</em><br>number of reviews on the product seller's account |[optional]|
**data_docid** | **StrictStr** | <em>unique identifier of the SERP data element</em><br>note that there is no full list of possible values as the <code>data_docid</code> is a dynamic value assigned by Google<br>example:<br><code>17363035694596624076</code> |[optional]|
**gid** | **StrictStr** | <em>global product identifier on Google Shopping</em><br>note that there is no full list of possible values as the gid is a dynamic value assigned by Google<br>if there are no values, you will get <code>null</code><br>example:<br><code>4702526954592161872</code><br>learn more about <code>gid</code> in <a href='https://dataforseo.com/help-center/whats-a-gid-in-google-shopping-api' target='_blank'>this help center guide</a> |[optional]|
**specifications** | **List[Optional[ShoppingSpecification]]** | <em>product specifications</em><br>contains all product attributes and related data listed on the product specification page |[optional]|
**sellers** | **List[Optional[ProductSeller]]** | <em>sellers of the product</em><br>number of reviews on the product seller's account |[optional]|
**variations** | **List[Optional[ProductVariation]]** | <em>variations of the product</em><br>contains brief information about different product variations |[optional]|