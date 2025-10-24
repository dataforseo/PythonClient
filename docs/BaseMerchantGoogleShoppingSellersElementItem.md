# BaseMerchantGoogleShoppingSellersElementItem

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **string** | type of element |[optional]|
**rank_group** | **number** | position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **number** | absolute rank in SERP<br>absolute position among all the elements found in Google Shopping SERP |[optional]|
**position** | **string** | the alignment of the element in Google Shopping SERP<br>possible values:<br>left, right |[optional]|
**xpath** | **string** | XPath of the element |[optional]|
**domain** | **string** | domain in SERP |[optional]|
**title** | **string** | product title |[optional]|
**url** | **string** | Google Shopping URL forwarding to the product page on the seller’s website<br>if you want to obtain a URL of the advertisement forwarding to the product page on the seller’s website, please refer to the Google Shopping Sellers Ad URL endpoint |[optional]|
**details** | **string** | details and special offers<br>if there are no details, the value will be null |[optional]|
**base_price** | **number** | product price without tax and shipping |[optional]|
**tax** | **number** | the amount of tax<br>tax is specified as the actual amount of money, not as the percentage |[optional]|
**shipping_price** | **number** | product shipping price |[optional]|
**total_price** | **number** | product price including tax and shipping |[optional]|
**currency** | **string** | currency in the ISO format<br>example:<br>USD |[optional]|
**seller_name** | **string** | name of the seller<br>the name of the company that placed a corresponding product on Google Shopping |[optional]|
**shop_ad_aclk** | **string** | unique ad click referral parameter<br>using this parameter you can get a URL of the advertisement in Google Shopping Sellers Ad URL |[optional]|