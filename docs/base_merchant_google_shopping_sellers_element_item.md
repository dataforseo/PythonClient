# BaseMerchantGoogleShoppingSellersElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | <em>position within a group of elements with identical <code>type</code> values</em><br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em> absolute rank in SERP</em><br>absolute position among all the elements found in Google Shopping SERP |[optional]|
**position** | **StrictStr** | <em>the alignment of the element in Google Shopping SERP</em><br>possible values:<br><code>left</code>, <code>right</code> |[optional]|
**xpath** | **StrictStr** | <em><a href='https://en.wikipedia.org/wiki/XPath'>XPath</a> of the element</em> |[optional]|
**domain** | **StrictStr** | <em>domain in SERP</em> |[optional]|
**title** | **StrictStr** | <em>product title</em> |[optional]|
**url** | **StrictStr** | <em>Google Shopping URL forwarding to the product page on the seller’s website</em><br>if you want to obtain a URL of the advertisement forwarding to the product page on the seller's website, please refer to the <a href='/v3/merchant/google/sellers/ad_url/'>Google Shopping Sellers Ad URL</a> endpoint |[optional]|
**details** | **StrictStr** | <em>details and special offers</em><br>if there are no details, the value will be <code>null</code> |[optional]|
**base_price** | **StrictFloat** | <em>product price without tax and shipping</em> |[optional]|
**tax** | **StrictFloat** | <em>the amount of tax</em><br>tax is specified as the actual amount of money, not as the percentage |[optional]|
**shipping_price** | **StrictFloat** | <em>product shipping price</em> |[optional]|
**total_price** | **StrictFloat** | <em>product price including tax and shipping</em> |[optional]|
**currency** | **StrictStr** | <em>currency in the <a href='https://en.wikipedia.org/wiki/ISO_4217'>ISO</a> format</em><br>example:<br><code>USD</code> |[optional]|
**seller_name** | **StrictStr** | <em>name of the seller</em><br>the name of the company that placed a corresponding product on Google Shopping |[optional]|
**shop_ad_aclk** | **StrictStr** | <em>unique ad click referral parameter</em><br>using this parameter you can get a URL of the advertisement in <a href='/v3/merchant/google/sellers/ad_url/'>Google Shopping Sellers Ad URL</a> |[optional]|