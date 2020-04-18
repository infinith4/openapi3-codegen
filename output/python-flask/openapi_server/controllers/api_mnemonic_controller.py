from openapi_server.models.request_add_address_model import RequestAddAddressModel  # noqa: E501
from openapi_server.models.request_upload_text_model import RequestUploadTextModel  # noqa: E501
from openapi_server.models.response_add_address_model import ResponseAddAddressModel  # noqa: E501
from openapi_server.models.response_tx_model import ResponseTxModel  # noqa: E501
from openapi_server.models.response_upload_text_model import ResponseUploadTextModel  # noqa: E501
from openapi_server import util

from pymongo import DESCENDING, ASCENDING
import connexion
import six
import multiprocessing
from openapi_server import app, mongo, bootstrap

from openapi_server.libraires.whats_on_chain_lib import WhatsOnChainLib
import bitsv
from openapi_server.bip39mnemonic import Bip39Mnemonic

def api_mnemonic():  # noqa: E501
    # """get transactions.

    # get transaction from mongodb. # noqa: E501

    # :param addr: bitcoin sv address
    # :type addr: str
    # :param start_index: start index ( default is 0 )
    # :type start_index: int
    # :param count: get transaction count ( default is 5 )
    # :type count: int

    # :rtype: List[ResponseTxModel]
    # """
    # return 'do some magic!'

    try:
        app.app.logger.info("start /api/tx")
        if connexion.request.is_json:
            body = RequestAddAddressModel.from_dict(connexion.request.get_json())  # noqa: E501
        mnemonic = body.mnemonic  #app.config['TESTNET_MNEMONIC']
        bip39Mnemonic = Bip39Mnemonic(mnemonic, passphrase="", network="test")
        privateKey = bitsv.Key(bip39Mnemonic.privatekey_wif, network = 'test')
        address = privateKey.address
        balance_satoshi = privateKey.get_balance()
        balance_bsv = float(balance_satoshi) / float(100000000)
            # html = render_template(
            #     'mnemonic.html',
            #     privatekey_wif = bip39Mnemonic.privatekey_wif,
            #     address = address,
            #     balance_satoshi = balance_satoshi,
            #     balance_bsv = balance_bsv,
            #     title="mnemonic")
        return { 'textdata_list': res_get_textdata }, 200
    except Exception as e:
        print(e)
        return "", 500

