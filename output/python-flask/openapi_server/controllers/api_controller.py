import connexion
import six

from openapi_server.models.request_add_address_model import RequestAddAddressModel  # noqa: E501
from openapi_server.models.request_mnemonic_model import RequestMnemonicModel  # noqa: E501
from openapi_server.models.request_upload_text_model import RequestUploadTextModel  # noqa: E501
from openapi_server.models.response_add_address_model import ResponseAddAddressModel  # noqa: E501
from openapi_server.models.response_mnemonic_model import ResponseMnemonicModel  # noqa: E501
from openapi_server.models.response_tx_model import ResponseTxModel  # noqa: E501
from openapi_server.models.response_upload_model import ResponseUploadModel  # noqa: E501
from openapi_server.models.response_upload_text_model import ResponseUploadTextModel  # noqa: E501
from openapi_server import util


def api_addaddress(body):  # noqa: E501
    """search data for added address on bitcoin sv

    search data for added address on Bitcoin SV. # noqa: E501

    :param body: request /api/add_address
    :type body: dict | bytes

    :rtype: ResponseAddAddressModel
    """
    if connexion.request.is_json:
        body = RequestAddAddressModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_download(txid):  # noqa: E501
    """get data for transaction id on Bitcoin SV.

    get data for transaction id on Bitcoin SV. # noqa: E501

    :param txid: bitcoin sv transaction id
    :type txid: str

    :rtype: file
    """
    return 'do some magic!'


def api_mnemonic(body):  # noqa: E501
    """convert mnemonic words to wif, asset on Bitcoin SV.

    convert mnemonic words to wif, asset on Bitcoin SV. # noqa: E501

    :param body: request /api/mnemonic
    :type body: dict | bytes

    :rtype: ResponseMnemonicModel
    """
    if connexion.request.is_json:
        body = RequestMnemonicModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_tx(addr, start_index=None, count=None):  # noqa: E501
    """get transactions.

    get transaction from mongodb. # noqa: E501

    :param addr: bitcoin sv address
    :type addr: str
    :param start_index: start index ( default is 0 )
    :type start_index: int
    :param count: get transaction count ( default is 5 )
    :type count: int

    :rtype: List[ResponseTxModel]
    """
    return 'do some magic!'


def api_upload(privatekey_wif=None, file=None):  # noqa: E501
    """upload file on Bitcoin SV. (100kb)

    convert mnemonic words to wif, asset on Bitcoin SV. # noqa: E501

    :param privatekey_wif: 
    :type privatekey_wif: str
    :param file: 
    :type file: str

    :rtype: ResponseUploadModel
    """
    return 'do some magic!'


def api_uploadtext(body):  # noqa: E501
    """upload text data on Bitcoin SV.

    upload text data on Bitcoin SV. # noqa: E501

    :param body: upload text data on Bitcoin SV.
    :type body: dict | bytes

    :rtype: List[ResponseUploadTextModel]
    """
    if connexion.request.is_json:
        body = RequestUploadTextModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
