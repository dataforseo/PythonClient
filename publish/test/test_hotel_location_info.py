# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.hotel_location_info import HotelLocationInfo

class TestHotelLocationInfo(unittest.TestCase):
    """HotelLocationInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HotelLocationInfo:
        """Test HotelLocationInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HotelLocationInfo`
        """
        model = HotelLocationInfo()
        if include_optional:
            return HotelLocationInfo(
                neighborhood = '',
                neighborhood_description = '',
                maps_url = '',
                overall_score = 1.337,
                score_by_categories = {
                    'key' : 1.337
                    },
                latitude = 1.337,
                longitude = 1.337,
                location_chain = [
                    dataforseo_client.models.location_chain.LocationChain(
                        card_id = '', 
                        feature_id = '', 
                        cid = '', 
                        title = '', )
                    ]
            )
        else:
            return HotelLocationInfo(
        )
        """

    def testHotelLocationInfo(self):
        """Test HotelLocationInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
