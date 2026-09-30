# PageMetrics


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**links_external** | **StrictInt** | <em>number of external links</em><br>the number of links pointing to other websites |[optional]|
**links_internal** | **StrictInt** | <em>number of internal links</em><br>the number of links pointing to other pages within the target website |[optional]|
**duplicate_title** | **StrictInt** | <em>number of pages with duplicate titles</em> |[optional]|
**duplicate_description** | **StrictInt** | <em>number of pages with duplicate descriptions</em> |[optional]|
**duplicate_content** | **StrictInt** | <em>number of pages with duplicate content</em> |[optional]|
**broken_links** | **StrictInt** | <em>number of broken links</em><br>number of broken links across all crawled pages on a target website |[optional]|
**broken_resources** | **StrictInt** | <em>number of broken resources</em><br>the number of images and other resources with broken links |[optional]|
**links_relation_conflict** | **StrictInt** | <em>number of links present on the target website that may have a conflict</em><br>for example, if <code>'links_relation_conflict': 2</code>, the target website is referring to the same source by at least one internal link with the <code>rel='nofollow'</code> attribute <strong>and</strong> by at least one dofollow link |[optional]|
**redirect_loop** | **StrictInt** | <em>number of redirect chains that start and end at the same URL</em><br>number of redirect chains where the destination URL redirects back to the original URL |[optional]|
**onpage_score** | **StrictFloat** | <em>shows how website is optimized on a 100-point scale</em><br>this field shows how website is optimized considering critical on-page issues and warnings detected;<br><code>100</code> is the highest possible score that means website does not have any critical on-page issues and important warnings;<br><strong>note</strong> that this value depends on the number of crawled pages;<br>learn more about how the metric is calculated in <a href='https://dataforseo.com/help-center/how-is-onpage-score-of-a-domain-calculated' target='_blank' rel='noopener noreferrer'>this help center article</a> |[optional]|
**non_indexable** | **StrictInt** | <em>number of non-indexable pages</em><br>number of pages that are blocked from being indexed by Google and other search engines by robots.txt, HTTP headers, or meta tags settings;<br>you can receive a list of non-indexable URLs using <a href='https://docs.dataforseo.com/v3/on_page/non_indexable/?bash' target='_blank' rel='noopener noreferrer'>this endpoint</a> |[optional]|
**checks** | **Dict[str, Optional[StrictInt]]** | <em>page-specific on-page check-ups</em> |[optional]|