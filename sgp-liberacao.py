# -*- coding: utf-8 -*-

import re
import requests
import json
import sys


class WebService:

    def run(self, q, **kwargs):

        reload(sys)
        sys.setdefaultencoding('utf-8')

        TOKEN = 'TOKEN_AQUI'
        APP = 'whatsapp'

        datareq = {}
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
            r = requests.post(
                'http://10.10.10.10:8000/ws/ura/promessapagamento', data=datareq)
            rws = r.json()
            if rws.get('status') is not None:
                if rws.get('status') == 1:
                    return {'redirect_menu': True, 
                             'message': u'Acesso liberado com sucesso. Em alguns minutos a conexão estará normalizada. Caso não normalize o acesso em 5 minutos, favor desligar e ligar o equipamento.'}
                return {'redirect_menu':True,
                        'message': rws.get('msg') or u'Erro Interno, tente novamente posteriormente.'}

                resposta += '\nLink do boleto: %s' % rws.get('link')
            else:
                resposta += u'\nNão localizamos fatura em aberto para envio do link'
            return {'message': resposta}
        else:
            return {'message': u'Erro no processamento. Favor identifique-se novamente digitando a opção #ajuda'}

