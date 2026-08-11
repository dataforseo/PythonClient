# HotelsPackElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**price** | **PriceInfo** | <em>price indicated in the element</em> |[optional]|
**title** | **StrictStr** | <em>title of a given link element</em> |[optional]|
**description** | **StrictStr** | <em>link description</em> |[optional]|
**hotel_identifier** | **StrictStr** | <em>unique hotel identifier</em><br>unique hotel identifier assigned by Google;<br>example: <code>'CgoIjaeSlI6CnNpVEAE'</code> |[optional]|
**domain** | **StrictStr** | <em>domain where a link points</em> |[optional]|
**url** | **StrictStr** | <em>source URL</em> |[optional]|
**is_paid** | **StrictBool** | <em>indicates whether the element is an ad</em> |[optional]|
**rating** | **RatingInfo** | <em>the item's rating </em><br>the popularity rate based on reviews and displayed in SERP;<br>if there is none, equals <code>null</code> |[optional]|