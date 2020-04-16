import connexion
import six

from openapi_server.models.request_add_address_model import RequestAddAddressModel  # noqa: E501
from openapi_server.models.request_upload_text_model import RequestUploadTextModel  # noqa: E501
from openapi_server.models.response_add_address_model import ResponseAddAddressModel  # noqa: E501
from openapi_server.models.response_tx_model import ResponseTxModel  # noqa: E501
from openapi_server.models.response_upload_text_model import ResponseUploadTextModel  # noqa: E501
from openapi_server import util


def api_add_address(body):  # noqa: E501
    """/api/address

     # noqa: E501

    :param body: request /api/add_address
    :type body: dict | bytes

    :rtype: ResponseAddAddressModel
    """
    if connexion.request.is_json:
        body = RequestAddAddressModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

