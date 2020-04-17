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

from flaskapp.lib.whats_on_chain_lib import WhatsOnChainLib

def api_tx(addr, start_index=None, count=None):  # noqa: E501
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
        addr = "aaaaaaa"
        app.app.logger.info("start /api/tx")
        start_index_str = app.app.request.args.get('start_index')
        if start_index_str == "":
            start_index = 0
        else: 
            start_index = int(start_index_str)
        cnt_str = app.app.request.args.get('cnt')
        if cnt_str == "":
            cnt = 5
        else:
            cnt = int(cnt_str)
        print("addr: %s; start_index:%s;cnt: %s" % (addr, start_index, cnt))
        # search mongodb transaction records from start_index to cnt.
        trans_list = []
        transaction_list = mongo.db.transaction.find(filter={'address': addr }, sort=[("_id",DESCENDING)])
        if transaction_list.count() > 0:
            maxcount = transaction_list.count()
            if start_index + cnt <= transaction_list.count():
                maxcount = start_index + cnt
            for i in range(start_index, maxcount):
                trans_list.append(transaction_list[i]["txid"])

        res_get_textdata = []
        print(trans_list)
        if len(trans_list) > 0:
            print(trans_list)
            p = multiprocessing.Pool(6) # プロセス数を6に設定
            result = p.map(WhatsOnChainLib.get_textdata, trans_list)  ## arg must be array

            for item in result:
                if item is not None and item.mimetype == "text/plain":
                    res_get_textdata.append(item.data)
        print(res_get_textdata)
        return 200, { 'textdata_list': res_get_textdata }
    except Exception as e:
        print(e)
        return "", 500

