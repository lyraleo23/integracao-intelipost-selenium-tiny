# 🚀 Integração Manual dos Pedidos Tiny x Intelipost

## 📋 Objetivo

Automatizar o processo de integração de pedidos do sistema Tiny ERP com a Intelipost, facilitando o envio de pedidos por transportadoras.


## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação principal do projeto.
- **Selenium**: Biblioteca para automação de navegadores web.


## 🏗️ Arquitetura

O projeto é estruturado da seguinte forma:

```plaintext
├── .gitignore
├── README.md
├── bot_web.py
├── main.py
└── tiny_web.py
```

- bot_web.py: Contém as funções relacionadas à automação do navegador utilizando o Selenium.
- main.py: Script principal que executa o processo de integração.
- tiny_web.py: Módulo responsável por interagir com o sistema Tiny ERP.


## 🚀 Como Executar

1. **Instale as Dependências**:
   Certifique-se de que o Python e o Selenium estejam instalados em seu ambiente.

2. **Crie o Executável**:
   Utilize a ferramenta [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/) para converter o script Python em um executável:
   ```bash
   auto-py-to-exe
   ```
3. **Execute o Programa**:
   Após a criação do executável, execute-o e aguarde a conclusão do processo de integração.
   

## ⚠️ Observações

- **Novas Transportadoras**:
  Caso sejam adicionadas novas transportadoras, é necessário incluí-las nas listas correspondentes no código `main.py`:
  - `transportadoras_miligrama`
  - `transportadoras_mili_nordeste`

Certifique-se de atualizar essas listas para garantir que as novas transportadoras sejam integradas corretamente.


## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias ou correções.


## 📞 Contato

- **Autor**: Leonardo Lyra
- **GitHub**: [lyraleo23](https://github.com/lyraleo23)
- **Linkdin**: [leonardo-lyra]([https://github.com/lyraleo23](https://www.linkedin.com/in/leonardo-lyra/))
