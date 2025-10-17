# le linha por linha da planilha
def dados():
    import pyautogui as pa
    from openpyxl import load_workbook

    planilha_resultado = load_workbook('resultado - Copia.xlsx')
    pg_principal = planilha_resultado['Sheet1']

    for linhas in pg_principal.iter_rows(values_only=True):
        for loop in range(3):
            celula = linhas[loop]
            pa.write(celula)
            pa.click(x=-1130, y=481)

