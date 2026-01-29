# ---------------------------------------------------------------------------
# Mesclador Automático de PDFs
# 
# Este script agrupa e mescla arquivos PDF baseando-se em prefixos de nome.
# Ideal para digitalizações separadas (ex: 001.1.pdf + 001.2.pdf).
#
# Copyright (c) 2026
# Licenciado sob a MIT License (https://opensource.org/licenses/MIT)
# ---------------------------------------------------------------------------

import os
import re
from pypdf import PdfWriter

__author__ = "Seu Nome"
__license__ = "MIT"

def natural_sort_key(s):
    
    
    
    
    
    
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', s)]

def juntar_pares_pdf(pasta_origem, pasta_destino):
    
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    
    
    arquivos = [f for f in os.listdir(pasta_origem) if f.lower().endswith('.pdf')]
    
    
    grupos = {}
    
    for arquivo in arquivos:
        nome_sem_extensao = os.path.splitext(arquivo)[0]
        
        try:
            
            id_base = nome_sem_extensao.split('.')[0] 
            
            if id_base not in grupos:
                grupos[id_base] = []
            
            grupos[id_base].append(arquivo)
        except Exception as e:
            print(f"Erro ao processar nome do arquivo {arquivo}: {e}")

    
    print(f"Encontrados {len(grupos)} grupos de arquivos para mesclar.\n")

    for id_base, lista_arquivos in grupos.items():
        
        lista_arquivos.sort(key=natural_sort_key)

        print(f"Mesclando grupo {id_base}: {lista_arquivos}")

        merger = PdfWriter()

        try:
            for nome_arquivo in lista_arquivos:
                caminho_completo = os.path.join(pasta_origem, nome_arquivo)
                merger.append(caminho_completo)

            nome_saida = f"{id_base}_completo.pdf"
            caminho_saida = os.path.join(pasta_destino, nome_saida)

            merger.write(caminho_saida)
            merger.close()
            print(f"-> Salvo em: {caminho_saida}\n")
            
        except Exception as e:
            print(f"Erro ao mesclar o grupo {id_base}: {e}")


diretorio_atual = '.' 
diretorio_saida = './mesclados' 

if __name__ == "__main__":
    juntar_pares_pdf(diretorio_atual, diretorio_saida)