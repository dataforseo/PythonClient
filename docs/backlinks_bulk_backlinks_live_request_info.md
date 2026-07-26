# BacklinksBulkBacklinksLiveRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**targets** | **List[Optional[StrictStr]]** | <em>domains, subdomains or webpages to get the number of backlinks for</em><br><strong>required field</strong><br>you can set up to 1000 domains, subdomains or webpages<br>the domain or subdomain should be specified without <code>https://</code> and <code>www.</code><br>the page should be specified with absolute URL (including <code>http://</code> or <code>https://</code>)<br>example:<br>`'targets': [<br>  'forbes.com',<br>  'cnn.com',<br>  'bbc.com',<br>  'yelp.com',<br>  'https://www.apple.com/iphone/',<br>  'https://ahrefs.com/blog/',<br>  'ibm.com',<br>  'https://variety.com/',<br>  'https://stackoverflow.com/',<br>  'www.trustpilot.com'<br>]` |[optional]|
**tag** | **StrictStr** | <em>user-defined task identifier</em><br>optional field<br><em>the character limit is 255</em><br>you can use this parameter to identify the task and match it with the result<br>you will find the specified <code>tag</code> value in the <code>data</code> object of the response |[optional]|