# ChatGptGoogleShoppingProduct


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**ei** | **StrictStr** | event identifier<br>internal event identifier used by Google |[optional]|
**product_id** | **StrictStr** | product identifier<br>can be used as a data_docid in Google Shopping API endpoints |[optional]|
**catalog_id** | **StrictStr** | Google Shopping catalog identifier of the product<br>can be used as a product_id in Google Shopping API endpoints |[optional]|
**gpcid** | **StrictStr** | Google product cluster identifier<br>can be used as a gid in Google Shopping API endpoints |[optional]|
**headline_offer_docid** | **StrictStr** | document identifier of the main offer in the headline<br>can be used as a data_docid in Google Shopping API endpoints |[optional]|
**image_docid** | **StrictStr** | identifier for the displayed product’s image |[optional]|
**rds** | **StrictStr** | resource descriptor string <br>internal Google resource descriptor string that identifies the product within Google’s Shopping index |[optional]|
**query** | **StrictStr** | search query<br>search query used by ChatGPT to retrieve the product from Google Shopping |[optional]|
**mid** | **StrictStr** | merchant identifier<br>identifier of the seller or merchant account in Google Shopping |[optional]|
**pvt** | **StrictStr** | product view type<br>internal Google parameter that specifies the product view type used when rendering the product item |[optional]|
**uule** | **StrictStr** | encoded location parameter<br>indicates the location for a search |[optional]|
**gl** | **StrictStr** | country code<br>indicates the location for which search results are displayed |[optional]|
**hl** | **StrictStr** | host language code<br>indicates the language in which search results are displayed |[optional]|