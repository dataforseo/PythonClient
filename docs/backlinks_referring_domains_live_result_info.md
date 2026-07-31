# BacklinksReferringDomainsLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**target** | **StrictStr** | <em><code>target</code> in a POST array</em> |[optional]|
**total_count** | **StrictInt** | <em>total number of relevant items in the database</em><br>total number of main domains referring to your target;<br>example.com and blog.example.com are counted as one referring domain |[optional]|
**items_count** | **StrictInt** | <em>number of items in the <code>items</code> array</em> |[optional]|
**items** | **List[Optional[BacklinksReferringDomainsLiveItem]]** | <em>items array</em> |[optional]|