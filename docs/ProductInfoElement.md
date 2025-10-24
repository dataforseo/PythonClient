# ProductInfoElement

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **string** | type of element |[optional]|
**rank_group** | **number** | position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **number** | absolute rank on the product specification page<br>absolute position among all the elements found on the product specification page |[optional]|
**position** | **string** | alignment of the element on the product specification page<br>can take the following values:<br>right, left |[optional]|
**product_id** | **string** | product_id received in a POST array<br>ilearn more about the parameter in this help center guide |[optional]|
**title** | **string** | title of the product |[optional]|
**description** | **string** | description of the product |[optional]|
**url** | **string** | product url<br>url of the product on Google Shopping |[optional]|
**images** | **string[]** | product images<br>contains urls to product images |[optional]|
**features** | **string[]** | product features<br>contains snippets with the description of product features |[optional]|
**rating** | **RatingElement** | product rating <br>the popularity rate based on reviews |[optional]|
**seller_reviews_count** | **number** | number of seller reviews<br>number of reviews on the product seller’s account |[optional]|
**data_docid** | **string** | unique identifier of the SERP data element<br>note that there is no full list of possible values as the data_docid is a dynamic value assigned by Google<br>example:<br>17363035694596624076 |[optional]|
**gid** | **string** | global product identifier on Google Shopping<br>note that there is no full list of possible values as the gid is a dynamic value assigned by Google<br>if there are no values, you will get null<br>example:<br>4702526954592161872<br>learn more about gid in this help center guide |[optional]|
**specifications** | **ShoppingSpecification[]** | product specifications<br>contains all product attributes and related data listed on the product specification page |[optional]|
**sellers** | **ProductSeller[]** | sellers of the product<br>number of reviews on the product seller’s account |[optional]|
**variations** | **ProductVariation[]** | variations of the product<br>contains brief information about different product variations |[optional]|