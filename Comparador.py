import pandas as pd
from fuzzywuzzy import process

# ==== CONFIGURAÇÃO ====
arquivo_csv = "lista.csv"         # Contém os dados como o 'alias'
arquivo_excel = "tabela.xlsx"     # Contém o nome dos computadores e setor
arquivo_saida = "resultado.xlsx"  # Arquivo final

# ==== 1. Leitura dos arquivos ====
csv_df = pd.read_csv(arquivo_csv)
excel_df = pd.read_excel(arquivo_excel)

# ==== 2. Função de limpeza ====
def limpar_nome(nome):
    if pd.isna(nome):
        return ""
    nome = str(nome).strip().lower()
    nome = nome.replace(".anydesk.com", "").replace(".local", "")
    nome = nome.split("@")[0]  # Remover domínio tipo 'eqpcap454@ad'
    return nome

# ==== 3. Criar colunas de nome limpo ====
csv_df["nome_limpo"] = csv_df["alias"].apply(limpar_nome)
excel_df["nome_limpo"] = excel_df.iloc[:, 0].apply(limpar_nome)

# ==== 4. Separar nome_usuario e setor da coluna 2 do Excel ====
def separar_nome_setor(valor):
    if pd.isna(valor):
        return pd.Series(["", ""])
    partes = str(valor).split(" - ")
    nome = partes[0].strip()
    setor = partes[1].strip() if len(partes) > 1 else ""
    return pd.Series([nome, setor])

excel_df[["nome_usuario", "setor"]] = excel_df.iloc[:, 1].apply(separar_nome_setor)

# ==== 5. Fazer correspondência aproximada entre as máquinas ====
resultados = []
for _, row in csv_df.iterrows():
    nome_csv = row["nome_limpo"]
    resultado_match = process.extractOne(nome_csv, excel_df["nome_limpo"], score_cutoff=80)
    print(f"Resultado para '{nome_csv}': {resultado_match}")
    if resultado_match and isinstance(resultado_match, tuple):
        match, score = resultado_match[:2]
        linha_excel = excel_df[excel_df["nome_limpo"] == match].iloc[0]
        resultados.append({
            "codigo_anydesk": row["cid"],
            "nome_usuario": linha_excel["nome_usuario"]
        })

# ==== 6. Exportar resultado (somente duas colunas) ====
resultado_df = pd.DataFrame(resultados, columns=["codigo_anydesk", "nome_usuario"])
resultado_df.to_excel(arquivo_saida, index=False)

print(f"✅ Arquivo '{arquivo_saida}' criado com {len(resultado_df)} correspondências.")
