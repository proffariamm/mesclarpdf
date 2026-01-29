# mesclarpdf
# Mesclador Automático de PDFs

Este script em Python automatiza a tarefa de agrupar e mesclar arquivos PDF fragmentados (como páginas soltas ou frentes e versos digitalizados separadamente) em um único arquivo completo, baseando-se no nome dos arquivos.

## Funcionalidades

* **Agrupamento Inteligente:** Identifica arquivos que pertencem ao mesmo documento através do prefixo do nome (ID).
* **Ordenação Automática:** Garante que a "Parte 1" venha antes da "Parte 2" (ordem alfanumérica).
* **Criação de Pasta:** Gera automaticamente uma pasta de saída para não misturar os arquivos originais com os mesclados.
* **Processamento em Lote:** Processa centenas de arquivos de uma só vez.

## Pré-requisitos

* Python 3.x instalado.
* Biblioteca `pypdf`.

### Instalação das dependências

Abra o terminal e execute:

```bash
pip install pypdf
