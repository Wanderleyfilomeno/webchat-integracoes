# -*- coding: utf-8 -*-

import re
import requests
import json
import sys

class WebService:

    def run(self,q,**kwargs):
        """
        motivoos:
        10: 'Instalação de KIT'
        20: 'Remoção de KIT'
        30: 'Preventiva'
        40: 'Corretiva'
        50: 'Financeiro'
        60: 'Mudança Endereço'
    
        ocorrenciatipo:
        1: 'Suporte - Sem Acesso'
        2: 'Suporte - Alterar MAC Placa de Rede'
        3: 'Suporte - Acesso Lento'
        4: 'Suporte - Problemas com páginas'
        5: 'Suporte - Outros'
        20: 'Financeiro - Alteração de Valor'
        21: 'Financeiro - Bloqueio'
        22: 'Financeiro - Reclamação Fatura'
        23: 'Financeiro - Mudança de Plano'
        24: 'Financeiro - Cancelamento Cobrança'
        25: 'Financeiro - Cancelamento Serviço'
        26: 'Financeiro - Outros'
        27: 'Financeiro - Cancelamento Contrato'
        28: 'Financeiro - Ativação de Contrato'
        29: 'Cobrança - Título em atraso'
        30: 'Cobrança - Lembrança de Pagamento'

        """
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
            datareq['motivoos'] = '40'
            datareq['ocorrenciatipo'] = '3'
            resposta = ''
            r = requests.post('http://10.10.10.1:8000/ws/ura/chamado/',data=datareq)
            rws = r.json()
            if rws.get('msg'):
                if rws.get('protocolo'):
                    resposta += '\nChamado aberto com sucesso. Protocolo: %s' %(rws.get('protocolo'))
                else:
                    resposta += rws.get('msg')
            return {'message': resposta }
        else:
            return {'message': 'Erro no processamento. Favor identifique-se novamente digitando a opção #ajuda'}

