# StoresCountInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**count** | **StrictInt** | <em>number of stores that offer the product</em> |[optional]|
**displayed_text** | **StrictStr** | <em>text displayed on the Google Shopping page</em> |[optional]|
**count_from_text** | **StrictBool** | <em>whether the number of stores is taken from text</em><br>indicates whether the number of stores is taken from <code>displayed_text</code>;<br>if the API finds the exact number of stores in the HTML code of the Google Shopping page, this parameter is <code>false</code>;<br>if the API cannot find the number of stores in the HTML code of the page, it takes the number from the <code>displayed_text</code>;<br>in this case, the parameter is <code>true</code> |[optional]|