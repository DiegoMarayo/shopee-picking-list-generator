# 📦 Shopee Picking List Generator

Automação para extrair dados de notas fiscais (PDF) da Shopee e gerar uma **lista de separação de pedidos (picking list)** pronta para uso na expedição.

---

## 🚀 Sobre o projeto

Ao vender pela Shopee, cada pedido gera uma nota fiscal em PDF.
Fazer a separação manual dos pedidos pode ser:

* ❌ Demorado
* ❌ Propenso a erros
* ❌ Difícil de escalar

Este projeto resolve esse problema automatizando todo o processo.

---

## ⚙️ Funcionalidades

✔ Extração automática do nome do cliente
✔ Extração de produtos e quantidades
✔ Agrupamento de itens iguais
✔ Manutenção de variações (cor/tamanho)
✔ Geração de PDF organizado para separação
✔ Layout otimizado para operação logística
✔ Cabeçalho com data, total de pedidos e itens

---

## 📄 Exemplo de saída

```
LISTA DE SEPARAÇÃO DE PEDIDOS
Data: 22/03/2026
Pedidos: 18 | Itens: 25

Diego
1x - Suporte Porta Bike...

Marcos
1x - Óculos Esportivo...
```

---

## 🛠 Tecnologias utilizadas

* Python
* pdfplumber
* reportlab

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/DiegoMarayo/shopee-picking-list-generator.git
cd shopee-picking-list-generator
```

Instale as dependências:

```bash
pip install pdfplumber reportlab
```

---

## ▶️ Como usar

1. Coloque seu arquivo de notas fiscais no projeto:

```
nfs.pdf
```

2. Execute o script:

```bash
python main.py
```

3. O arquivo será gerado automaticamente:

```
resultado.pdf
```

---

## 🧠 Como funciona

O sistema:

1. Lê o PDF das notas fiscais
2. Identifica o cliente (mesmo com texto desestruturado)
3. Extrai produtos e quantidades
4. Agrupa itens repetidos
5. Gera um PDF formatado para separação de pedidos

---

## 📈 Melhorias futuras

* 🌐 Interface web para upload de arquivos
* 📊 Exportação para Excel
* 🏷️ Geração de etiquetas
* 🔍 Suporte a OCR (PDFs escaneados)
* ⚡ Integração com APIs de marketplace

---

## 💡 Motivação

Este projeto foi criado para resolver um problema real de operação logística em vendas online, reduzindo tempo e erros no processo de separação de pedidos.

---

## 👨‍💻 Autor

Diego Marayo

---

## ⭐ Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias!

---
