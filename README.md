Link do PDF: [Paulo_Ricardo_atividade_2.pdf](https://github.com/user-attachments/files/16859493/Paulo_Ricardo_atividade_2.pdf)

## 1. Baixando e Configurando o Repositório

Execute o comando "git clone PauloRicardo-01/Teste_Software_Mutantes_2024_Lima_Paulo"

## 2. Pré-requisitos e Instalação de Dependências

Abra o projeto e digite os seguintes comandos:

python -m venv venv
./venv/Scripts/activate
pip install mutmut pytest pytest-cov

## 3. Executando Testes Existentes

Execute o comando abaixo

pytest -v

Ou, caso queira um arquivo em formato html, execute o comando abaixo

pytest --cov=src --cov-report html

## 4. Executando Testes de Mutação

Execute o comando abaixo

mutmut run

Logo após, digite o comando abaixo para uma visão dos resultados

mutmut results
