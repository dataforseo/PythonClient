# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.page_metrics import PageMetrics

class TestPageMetrics(unittest.TestCase):
    """PageMetrics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageMetrics:
        """Test PageMetrics
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageMetrics`
        """
        model = PageMetrics()
        if include_optional:
            return PageMetrics(
                links_external = 56,
                links_internal = 56,
                duplicate_title = 56,
                duplicate_description = 56,
                duplicate_content = 56,
                broken_links = 56,
                broken_resources = 56,
                links_relation_conflict = 56,
                redirect_loop = 56,
                onpage_score = 1.337,
                non_indexable = 56,
                checks = {
                    'key' : 56
                    }
            )
        else:
            return PageMetrics(
        )
        """

    def testPageMetrics(self):
        """Test PageMetrics"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
