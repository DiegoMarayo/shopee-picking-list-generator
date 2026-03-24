import pdfplumber
from collections import defaultdict
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from datetime import datetime

pdf_path = "nfs.pdf"
saida_pdf = "resultado.pdf"

dados = []

# -------------------------
# 🔹 FUNÇÕES SEGURAS
# -------------------------

def formatar_nome(nome):
    return " ".join([p.capitalize() for p in nome.split()])

def limpar_cliente(nome):
    partes = nome.split()
    nome_limpo = []

    for p in partes:
        if "/" in p or p.replace(".", "").replace("-", "").isdigit():
            break
        nome_limpo.append(p)

    return " ".join(nome_limpo)

def agrupar_produtos(produtos):
    agrupado = defaultdict(int)

    for nome, qtd in produtos:
        try:
            qtd = int(qtd)
        except:
            qtd = 1

        agrupado[nome] += qtd

    return list(agrupado.items())

# -------------------------
# 🔹 EXTRAÇÃO
# -------------------------

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:

        text = page.extract_text()

        if not text:
            continue

        cliente = "Não encontrado"
        linhas = text.split("\n")

        for i, linha in enumerate(linhas):

            if "NOME/RAZÃO SOCIAL" in linha:

                nome = linha.replace("NOME/RAZÃO SOCIAL", "").strip()

                if nome and "CNPJ" not in nome:
                    cliente = nome
                    break

                for j in range(i + 1, len(linhas)):
                    prox = linhas[j].strip()

                    if prox and "CNPJ" not in prox and "DATA DE EMISSÃO" not in prox:
                        cliente = prox
                        break

                break

        largura = page.width
        area_produtos = page.within_bbox((0, 300, largura, 750))
        tabela = area_produtos.extract_table()

        produtos = []

        if tabela:
            for linha in tabela:

                if not linha:
                    continue

                if "DESCRIÇÃO" in str(linha):
                    continue

                if len(linha) >= 7:
                    descricao = linha[1]
                    quantidade = linha[6]

                    if descricao and quantidade:
                        descricao = " ".join(descricao.split())
                        produtos.append((descricao.strip(), quantidade.strip()))

        if produtos:
            cliente = formatar_nome(limpar_cliente(cliente))
            produtos = agrupar_produtos(produtos)

            dados.append({
                "cliente": cliente,
                "produtos": produtos
            })

# -------------------------
# 🔹 CÁLCULOS
# -------------------------

total_pedidos = len(dados)
total_itens = sum(qtd for item in dados for _, qtd in item["produtos"])

data_hoje = datetime.now().strftime("%d/%m/%Y")

# -------------------------
# 🔹 PDF PROFISSIONAL
# -------------------------

doc = SimpleDocTemplate(saida_pdf)
styles = getSampleStyleSheet()

style_titulo = ParagraphStyle(
    "titulo",
    fontSize=16,
    leading=18,
    alignment=1,
    spaceAfter=10
)

style_info = ParagraphStyle(
    "info",
    fontSize=10,
    leading=12,
    alignment=1,
    spaceAfter=10
)

conteudo = []

# 🔥 CABEÇALHO
conteudo.append(Paragraph("<b>LISTA DE SEPARAÇÃO DE PEDIDOS</b>", style_titulo))
conteudo.append(Paragraph(f"Data: {data_hoje}", style_info))
conteudo.append(Paragraph(f"Pedidos: {total_pedidos} | Itens: {total_itens}", style_info))
conteudo.append(Spacer(1, 10))

# -------------------------
# 🔹 PEDIDOS
# -------------------------

for item in dados:

    bloco = []

    bloco.append(Paragraph(f"<b>{item['cliente']}</b>", styles["Normal"]))
    bloco.append(Spacer(1, 6))

    for prod, qtd in item["produtos"]:
        bloco.append(Paragraph(f"{qtd}x - {prod}", styles["Normal"]))

    bloco.append(Spacer(1, 2))
    bloco.append(Paragraph("--"*64, styles["Normal"]))
    bloco.append(Spacer(1, 2))

    conteudo.append(KeepTogether(bloco))

doc.build(conteudo)

print("✅ PDF Gerado com Sucesso!")