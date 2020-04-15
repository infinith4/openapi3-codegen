# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.request_add_address_model import RequestAddAddressModel  # noqa: E501
from openapi_server.models.request_upload_text_model import RequestUploadTextModel  # noqa: E501
from openapi_server.models.response_add_address_model import ResponseAddAddressModel  # noqa: E501
from openapi_server.models.response_tx_model import ResponseTxModel  # noqa: E501
from openapi_server.models.response_upload_text_model import ResponseUploadTextModel  # noqa: E501
from openapi_server.test import BaseTestCase


class TestApiController(BaseTestCase):
    """ApiController integration test stubs"""

    def test_api_add_address(self):
        """Test case for api_add_address

        /api/address
        """
        body = {
  "address" : "bitcoin sv address"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'api_key': 'special-key',
        }
        response = self.client.open(
            '/v1/api/add_address',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_tx(self):
        """Test case for api_tx

        get transactions.
        """
        query_string = [('start_index', 56),
                        ('count', 56)]
        headers = { 
            'Accept': 'application/json',
            'api_key': 'special-key',
        }
        response = self.client.open(
            '/v1/api/tx'.format(addr='addr_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_upload_text(self):
        """Test case for api_upload_text

        upload text data on Bitcoin SV.
        """
        body = {
  "mnemonic_words" : "",
  "message" : "upload text"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'api_key': 'special-key',
        }
        response = self.client.open(
            '/v1/api/upload_text',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
