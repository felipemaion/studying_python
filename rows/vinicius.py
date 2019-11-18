#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# vinicius.py
# @author Felipe Maion
# @description Reads REL_1_12_2018.pdf for Vinicius Costa
# @created Mon Feb 04 2019 01:24:15 GMT-0200 (-02)
# @last-modified Mon Feb 04 2019 01:24:28 GMT-0200 (-02)
#


import os
import rows
from collections import OrderedDict
from io import BytesIO
from decimal import *


def carregar_arquivo(arquivo, encoding="latin-1"):
    file_source = os.getcwd().replace("/", "//")
    return rows.import_from_csv(file_source + "//" +  arquivo, encoding=encoding)

rel = carregar_arquivo("REL_1_12_2018.pdf")
# rec = carregar_arquivo("rec.csv")
# bip = carregar_arquivo("bip.csv")
# dic = carregar_arquivo("dic.csv")

def campos():
    campos_tabela = []
    for field_name, field_type in rec.fields.items():
        campos_tabela.append(field_name)
        print('{} is {}'.format(field_name, field_type))
    return campos_tabela

# def converter(valor):
#     return Decimal(valor.replace(".","").replace(",","."))

# def lucro(item):
#     subgrupo =["SNAPLOC", "QUICKLOC", "TEPRO", "RIVKLE ELASTICO"]
#     big_group = ["ONSERT", "FLEXITOL", "PLASTEC"]
#     if item in subgrupo:
#         return sum(converter(row.lucro_bruto) for row in rec if row.descrgrupo_plastec == item)
#     elif item in big_group: # TODO
#         return sum(converter(row.lucro_bruto) for row in rec if row.grupo_wbh == item)
#     elif item == "TOTAL":
#         return sum(converter(row.lucro_bruto) for row in rec if row.grupo_wbh == "PLASTEC" or row.grupo_wbh == "FLEXITOL" or row.grupo_wbh == "ONSERT")
#     #grupo_wbh


# def faturamento(item):
#     subgrupo =["SNAPLOC", "QUICKLOC", "TEPRO", "RIVKLE ELASTICO"]
#     big_group = ["ONSERT", "FLEXITOL", "PLASTEC"]
#     if item in subgrupo:
#         return sum(converter(row.faturamento_liquido) for row in rec if row.descrgrupo_plastec == item)
#     elif item in big_group: # TODO
#         return sum(converter(row.faturamento_liquido) for row in rec if row.grupo_wbh == item)
#     elif item == "TOTAL":
#         return sum(converter(row.faturamento_liquido) for row in rec if row.grupo_wbh == "PLASTEC" or row.grupo_wbh == "FLEXITOL" or row.grupo_wbh == "ONSERT")
#     #grupo_wbh

# def print_line(data_line):
#     print("Data:{} Cliente:{} Desc:{} Quant:{} Fat_liq:{} Margem:{} BIP:{}".format(data_line.data,data_line.nome_do_cliente, 
#     data_line.descricao_do_produto, data_line.quantidade, data_line.faturamento_liquido, data_line.margem, data_line.bip))

# def carregar_grupo(grupo):
#     return [item for item in rec if item.descrgrupo_plastec == grupo]

# abril = [item for item in rec if item.mes == 4 and (item.grupo_wbh == "FLEXITOL" or item.grupo_wbh=="PLASTEC" or item.grupo_wbh=="ONSERT") ]

# snaplocs = carregar_grupo("SNAPLOC")
# tepros = carregar_grupo("TEPRO")
# quicklocs = carregar_grupo("QUICKLOC")


# lucro_snaploc = lucro("SNAPLOC")
# lucro_flexitol = lucro("FLEXITOL")
# lucro_quickloc = lucro("QUICKLOC")
# lucro_plastec = lucro("PLASTEC")
# lucro_total = lucro("TOTAL")

# faturamento_plastec = faturamento("PLASTEC")
# faturamento_flexitol = faturamento("FLEXITOL")
# faturamento_snaploc = faturamento("SNAPLOC")
# faturamento_quickloc = faturamento("QUICKLOC")
# faturamento_total = faturamento("TOTAL")



# # data is <class 'rows.fields.TextField'>
# # nofiscal is <class 'rows.fields.IntegerField'>
# # serie is <class 'rows.fields.TextField'>
# # cfop is <class 'rows.fields.IntegerField'>
# # tipo is <class 'rows.fields.TextField'>
# # rg is <class 'rows.fields.TextField'>
# # codproduto is <class 'rows.fields.TextField'>
# # descricao_do_produto is <class 'rows.fields.TextField'>
# # gpprod is <class 'rows.fields.TextField'>
# # quantidade is <class 'rows.fields.TextField'>
# # vlrunitcento is <class 'rows.fields.TextField'>
# # faturamento_bruto is <class 'rows.fields.TextField'>
# # faturamento_liquido is <class 'rows.fields.TextField'>
# # vlripi is <class 'rows.fields.TextField'>
# # vlricms is <class 'rows.fields.TextField'>
# # vlrpis is <class 'rows.fields.TextField'>
# # vlrcofins is <class 'rows.fields.TextField'>
# # custo_cento is <class 'rows.fields.TextField'>
# # custo_indust is <class 'rows.fields.TextField'>
# # lucro_bruto is <class 'rows.fields.TextField'>
# # margem is <class 'rows.fields.TextField'>
# # filial is <class 'rows.fields.IntegerField'>
# # codcliente is <class 'rows.fields.IntegerField'>
# # loja is <class 'rows.fields.TextField'>
# # nome_do_cliente is <class 'rows.fields.TextField'>
# # cnpj is <class 'rows.fields.TextField'>
# # uf is <class 'rows.fields.TextField'>
# # segmento is <class 'rows.fields.TextField'>
# # segmento_2 is <class 'rows.fields.TextField'>
# # grupo_cliente is <class 'rows.fields.TextField'>
# # grupo is <class 'rows.fields.TextField'>
# # descrgrupo_1 is <class 'rows.fields.TextField'>
# # descrgrupo_2 is <class 'rows.fields.TextField'>
# # descrgrupo_3 is <class 'rows.fields.TextField'>
# # grupo_alemanha is <class 'rows.fields.IntegerField'>
# # descgrupo_alemanha is <class 'rows.fields.TextField'>
# # vendext is <class 'rows.fields.IntegerField'>
# # nome_vendext is <class 'rows.fields.TextField'>
# # vendint is <class 'rows.fields.IntegerField'>
# # nome_vendint is <class 'rows.fields.TextField'>
# # icms_st is <class 'rows.fields.TextField'>
# # grau_de_inovacao is <class 'rows.fields.TextField'>
# # ncm is <class 'rows.fields.IntegerField'>
# # cp is <class 'rows.fields.TextField'>
# # fabricante is <class 'rows.fields.TextField'>
# # inss is <class 'rows.fields.TextField'>
# # obs is <class 'rows.fields.TextField'>
# # mes is <class 'rows.fields.IntegerField'>
# # cont_nf is <class 'rows.fields.TextField'>
# # mes_txt is <class 'rows.fields.TextField'>
# # descrgrupo_plastec is <class 'rows.fields.TextField'>
# # grupo_wbh is <class 'rows.fields.TextField'>
# # bip is <class 'rows.fields.TextField'>
# # custo_internado_usd is <class 'rows.fields.TextField'>
# # rmagin is <class 'rows.fields.TextField'>
