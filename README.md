## Autora do Projeto: Karina Kato

### Aula: Coding Lab PRO - Digital Innovation One

([EDUARDO DA SILVA FERREIRA — DIO Community Profile](https://www.dio.me/users/eduardo_s_ferreira))

#### Tecnologia: Python

#### Data: 27/03/2025

---

### Descrição

O pacote "image_processing_ferreedu" é usado para:

- Módulo "Processing":

  - Correspondência de histograma;
  - Similaridade estrutural;
  - Redimensionar imagem;
- Módulo "Utils":

  - Ler imagem;
  - Salvar imagem;
  - Plotar imagem;
  - Resultado do gráfico;
  - Plotar histograma;

---

## Passo a passo da configuração para hospedar um pacote em Python no ambiente de testes Test Pypi

- [X]  Instalação das últimas versões de "setuptools" e "wheel"

```
py -m pip install --user --upgrade setuptools wheel
```

- [X]  Tenha certeza que o diretório no terminal seja o mesmo do arquivo "setup.py"

```
C:\temp\image-processing-package> py setup.py sdist bdist_wheel
```

- [X]  Após completar a instalação, verifique se as pastas abaixo foram adicionadas ao projeto:

  - [X]  build;
  - [X]  dist;
  - [X]  image_processing_test.egg-info.
- [X]  Basta subir os arquivos, usando o Twine, para o Test Pypi:

```
py -m twine upload --repository testpypi dist/*
```

- [X]  Após rodar o comando acima no terminal, será pedido para inserir o usuário e senha. Feito isso, o projeto estará hospedado no Test Pypi.hospedá-lo no Pypi diretamente.

### Aqui o objetivo não é utilizar o projeto da Karina para postar em meu perfil do Pypi pessoal, visto que o projeto é dela. Ainda não tenho nenhum projeto que possa ser utilizado como pacote.

### No entanto, tenha em mente que o Test Pypi, como o próprio nome diz, é apenas um ambiente de testes. Para que o projeto esteja disponível como um pacote para ser usado publicamente, é necessário hospedá-lo no site oficial do Pypi.

---

image-processing-package-ferreedu/
├── image_processing_ferreedu/
│   └── __init__.py
│   └── process_image.py
├── tests/
│   └── test_example.py
│   └── test_image_processing.py
├── README.md
├── requirements.txt
├── setup.py
└── pyproject.toml

## Instalação local, após hospedagem no Test Pypi

- [X]  Instalação de dependências

```
pip install -r requirements.txt
```

- [X]  Instalção do Pacote

Use o gerenciador de pacotes ``pip install -i https://test.pypi.org/simple/ image_processing_ferreedu ``para instalar image_processing_ferreedu

```bash
pip install image_processing_ferreedu
```

---

## Como usar em qualquer projeto

```python
from image_processing_ferreedu.processing import combination
combination.find_difference(image1, image2)
```

## Autor (quem hospedou o projeto no Test Pypi)

Eduardo da Silva Ferreira

## Licença

[MIT](https://choosealicense.com/licenses/mit/)
