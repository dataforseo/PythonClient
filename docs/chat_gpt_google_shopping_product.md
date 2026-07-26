# ChatGptGoogleShoppingProduct


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**ei** | **StrictStr** | <em>event identifier</em><br>internal event identifier used by Google |[optional]|
**product_id** | **StrictStr** | <em>product identifier</em><br>can be used as a <code>data_docid</code> in <a href='https://docs.dataforseo.com/v3/merchant/google/overview/' target='_blank'>Google Shopping API endpoints |[optional]|
**catalog_id** | **StrictStr** | <em>Google Shopping catalog identifier of the product</em><br>can be used as a <code>product_id</code> in <a href='https://docs.dataforseo.com/v3/merchant/google/overview/' target='_blank'>Google Shopping API endpoints</a> |[optional]|
**gpcid** | **StrictStr** | <em>Google product cluster identifier</em><br>can be used as a <code>gid</code> in <a href='https://docs.dataforseo.com/v3/merchant/google/overview/' target='_blank'>Google Shopping API endpoints</a> |[optional]|
**headline_offer_docid** | **StrictStr** | <em>document identifier of the main offer in the headline</em><br>can be used as a <code>data_docid</code> in <a href='https://docs.dataforseo.com/v3/merchant/google/overview/' target='_blank'>Google Shopping API endpoints</a> |[optional]|
**image_docid** | **StrictStr** | <em>identifier for the displayed product’s image</em> |[optional]|
**rds** | **StrictStr** | <em>resource descriptor string </em><br>internal Google resource descriptor string that identifies the product within Google's Shopping index |[optional]|
**query** | **StrictStr** | <em>search query</em><br>search query used by ChatGPT to retrieve the product from Google Shopping |[optional]|
**mid** | **StrictStr** | <em>merchant identifier</em><br>identifier of the seller or merchant account in Google Shopping |[optional]|
**pvt** | **StrictStr** | <em>product view type</em><br>internal Google parameter that specifies the product view type used when rendering the product item |[optional]|
**uule** | **StrictStr** | <em>encoded location parameter</em><br>indicates the location for a search |[optional]|
**gl** | **StrictStr** | <em>country code</em><br>indicates the location for which search results are displayed |[optional]|
**hl** | **StrictStr** | <em>host language code</em><br>indicates the language in which search results are displayed |[optional]|