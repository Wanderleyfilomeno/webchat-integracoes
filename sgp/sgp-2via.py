# -*- coding: utf-8 -*-

import re
import requests
import json
import sys

class WebService:

    def run(self,q,**kwargs):

        TOKEN = 'TOKEN_AQUI'
        APP = 'whatsapp'
        
        reload(sys)
        sys.setdefaultencoding('utf-8')
        
        datareq={}
        datareq['token'] = TOKEN
        datareq['app'] = APP
        data_json = {}
        try:
            data = kwargs.get('data')
            data_json = json.loads(data)
        except:
            pass
        if data_json:
            datareq['cpfcnpj'] = data_json.get('cpfCnpj')
            datareq['contrato'] = data_json.get('contratoId')
            resposta = ''
            r = requests.post('http://10.10.10.10:8000/ws/ura/fatura2via',data=datareq)
            rws = r.json()
            if rws.get('link'):
                resposta += '\nLink do boleto: %s' %rws.get('link')
            else:
                resposta += u'\nNão localizamos fatura em aberto para envio do link'
            return {'message': resposta}
        else:
            return {'message': 'Erro no processamento. Favor identifique-se novamente digitando a opção #ajuda'}

