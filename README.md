# Automação para Registro de Máquinas no AnyDesk

## Descrição

Na minha empresa, precisamos instalar o AnyDesk em todas as máquinas e depois registrar cada uma delas no AnyDesk Administrator. 
Sabendo que esse processo manual ia dar muito trabalho, criei um programa em Python para automatizar parte disso.

O programa usa duas tabelas:  
- Uma planilha da empresa com o nome dos computadores, nome do usuário e setor  
- Um arquivo CSV exportado do AnyDesk que lista todas as máquinas registradas na conta

A automação compara essas duas listas e gera uma terceira planilha com o código AnyDesk e o nome do usuário, usando o nome da máquina como referência.

Como eu ainda não sei mexer no código-fonte do AnyDesk, a automação funciona controlando o teclado e o mouse, usando as bibliotecas `pyautogui`, `time` e `openpyxl`.

A parte de comparação das tabelas foi feita com ajuda de uma IA (ChatGPT), que usou as bibliotecas `pandas` e `fuzzywuzzy` para fazer a correspondência dos dados.

Usei a IA porque tinha pouco tempo para desenvolver tudo sozinho.

## Tecnologias usadas

- Python  
- pyautogui  
- time  
- openpyxl  
- pandas  
- fuzzywuzzy  

## Como usar

1. Exporte o CSV do AnyDesk com as máquinas registradas  
2. Tenha a planilha da empresa com nome dos computadores e usuários  
3. Configure os nomes dos arquivos no script  
4. Execute o script Python para gerar a planilha final com código AnyDesk e nome do usuário  
5. Mude as coordenadas dos clicks de mouse conforme o seu monitor
## Objetivo

Economizar tempo e evitar erros ao registrar as máquinas no AnyDesk Administrator, automatizando um processo que seria muito trabalhoso manualmente.

---

## Autor

Seu Nome - Automação desenvolvida internamente com ajuda de IA.
