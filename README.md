# 📚 Sistema de Cadastro de Livros em Python (Console)

Este é um projeto simples de **sistema de cadastro de livros**, desenvolvido em **Python**, com interação via terminal.  
Permite adicionar, consultar e remover livros de uma lista em memória, utilizando um menu dinâmico.

## 💻 Tecnologias utilizadas

- Python 3  
- Terminal/Console

## ⚙️ Funcionalidades

- Cadastro de livros com:
  - Nome  
  - Autor  
  - Editora  
  - ID gerado automaticamente  

- Consulta:
  - Todos os livros cadastrados  
  - Livro por ID  
  - Livros por autor  

- Remoção de livros por ID  

- Interface com menus e feedbacks no terminal

## ▶️ Como executar

1. Copie o código-fonte para um arquivo `.py`, por exemplo: `livraria.py`

2. Execute o programa no terminal com o Python:
```bash
python livraria.py
```

## 📝 Exemplo de uso
```bash
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
|      Bem vindo a Livraria do     |
|        Rodrigo Alcantara         |
|__________________________________|

|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
|           MENU PRINCIPAL         |
|__________________________________|
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
| 1 - Cadastrar Livro              |
| 2 - Consultar Livro(s)           |
| 3 - Remover Livro(s)             |
| 4 - Sair                         |
|__________________________________|
```
## 📌 Observações
- Os dados não são salvos em arquivo, permanecem apenas durante a execução do programa.  
- O sistema utiliza `print()`s formatados com `\u203E` e `_` para criar uma interface amigável no terminal.