# xyzbank-web-test

### Descrição

Este projeto contém o código responsável por realizar testes end-to-end (E2E) do sistema [XYZ Bank](https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login).

- [Allure Reports](https://allurereport.org)
- [Python 3.12.0](https://www.python.org/downloads/release/python-3120/)
- [Pytest 8.3.2](https://docs.pytest.org/en/stable/announce/release-8.3.2.html)
- [Selenium 4.24.0](https://www.selenium.dev/blog/2024/selenium-4-24-released/)

### Clone e Execução do projeto

Para clonar o projeto siga os seguintes passos:

No terminal:
```
git clone git@github.com:caldasmatheus/xyzbank-web-test.git
```

No contexto onde o projeto foi clonado:
```
cd xyzbank-web-test
```

Na raiz do projeto:
```
pip install pytest==X.X.X selenium==Y.Y.Y
```

:exclamation: **Observação**: Para questões relacionadas a autenticação por SSH, consulte a documentação do GitHub em "[Crie e Adicione seu Par de Chaves SSH](https://docs.github.com/pt/authentication/connecting-to-github-with-ssh)".

### Tipos de Execução dos Testes

Para executar o projeto **xyzbank-web-test** siga as etapas:

* Exemplo de execução de todos os cenários de testes:

```
pytest tests
```

* Exemplo de execução de uma classe de teste específica:

```
pytest tests/test_CT001.py
```

* Exemplo de execução de um cenário de teste específico:

```
pytest tests/test_CT001.py::Test_CT001::test_deposit
```

### Contribuições

Para contribuir com o projeto, siga estas etapas:

1. Crie um *branch*: *`git checkout -b <branch_name>`*;
2. Faça suas alterações e confirme-as: *`git commit -m '<commit_message>'`*;
3. Envie a *branch* local para o repositório remoto: *`git push origin <branch_name>`*;
4. Crie o *pull request*.

:exclamation: **Observação**: Como alternativa, consulte a documentação do GitHub em "[Criando um Pull Request](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)".

### Contato

Em caso de dúvidas: <raimundo.matheus@dcx.ufpb.br>. :incoming_envelope: