# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.appendix_content_generation_day_limits_rates_data_info import AppendixContentGenerationDayLimitsRatesDataInfo

class TestAppendixContentGenerationDayLimitsRatesDataInfo(unittest.TestCase):
    """AppendixContentGenerationDayLimitsRatesDataInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppendixContentGenerationDayLimitsRatesDataInfo:
        """Test AppendixContentGenerationDayLimitsRatesDataInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppendixContentGenerationDayLimitsRatesDataInfo`
        """
        model = AppendixContentGenerationDayLimitsRatesDataInfo()
        if include_optional:
            return AppendixContentGenerationDayLimitsRatesDataInfo(
                live = 1.337,
                languages = 1.337
            )
        else:
            return AppendixContentGenerationDayLimitsRatesDataInfo(
        )
        """

    def testAppendixContentGenerationDayLimitsRatesDataInfo(self):
        """Test AppendixContentGenerationDayLimitsRatesDataInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
