# -*- coding: utf-8 -*-

import re
import requests
import json
import sys

class WebService:

    def responseContrato(self,rws):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        response = {}
        response['contratoId'] = str(rws.get('contratoId'))
        response['razaoSocial'] = str(rws.get('razaoSocial'))
        response['cpfCnpj'] = str(rws.get('cpfCnpj'))
        response['contratoStatus'] = str(rws.get('contratoStatus'))
        response['contratoStatusDisplay'] = str(rws.get('contratoStatusDisplay'))
        response['contratoStatusModo'] = str(rws.get('contratoStatusModo'))
        response['message'] = u'Olá %s, seja bem-vindo ao autoatendimento. Seguem as opções.' %response['razaoSocial']
        response['customer'] = response['razaoSocial']
        response['doc'] = response['cpfCnpj']
        return response

    def run(self,q,**kwargs):

        query = re.sub('[^0-9 ]','',' '.join(q.strip().split()))

        TOKEN = 'TOKEN_AQUI'
        APP = 'whatsapp'
        
        if query:
            datareq={}
            datareq['token'] = TOKEN
            datareq['app'] = APP
            try:
                datareq['cpfcnpj'] = query.split()[0]
            except:
                datareq['cpfcnpj'] = ''

            r = requests.post('http://10.10.10.10:8000/ws/ura/consultacliente',data=datareq)
            rws = r.json()
            contrato = None
            if rws.get('contratos'):
                if len(rws.get('contratos')) == 1:
                    return self.responseContrato(rws.get('contratos')[0])
                else:
                    if len(query.split()) > 1:
                        for c1 in rws.get('contratos'):
                            if query.split()[1].strip() == str(c1.get('contratoId')):
                                return self.responseContrato(c1)

                    mensagem = u"Olá %s, verificamos que há mais de 1 contrato." %(rws.get('contratos')[0].get('razaoSocial'))
                    for c1 in rws.get('contratos'):
                        mensagem += "\n Digite %s %s para selecionar contrato %s" %(query.split()[0],c1.get('contratoId'),c1.get('contratoId'))
                    return {'message': mensagem}
            else:
                return {'message': 'Não localizamos o cliente com as informações informadas'}

        return {'message': 'Digite CPF/CNPJ do Assinante'}

