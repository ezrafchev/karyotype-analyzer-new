
# Karyotype Analyzer

Este é um software simples para análise citogenética automatizada de cariótipos humanos, utilizando inteligência artificial para identificar e classificar aberrações cromossômicas.

## Requisitos

- Python 3.7+
- Bibliotecas listadas em `requirements.txt`

## Instalação

1. Clone este repositório:
   ```
   git clone https://github.com/seu-usuario/karyotype-analyzer.git
   cd karyotype-analyzer
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Uso

1. Execute o programa principal:
   ```
   python main.py
   ```

2. Use a interface gráfica para carregar uma imagem de cariótipo e analisá-la.

3. Os resultados serão exibidos na interface e armazenados no banco de dados SQLite.

## Estrutura do Projeto

- `main.py`: Arquivo principal que integra todos os módulos
- `src/gui.py`: Interface gráfica do usuário
- `src/image_processor.py`: Processamento de imagens e detecção de cromossomos
- `src/database.py`: Gerenciamento do banco de dados SQLite

## Limitações

Este é um projeto simples e pode não ser adequado para uso em ambientes clínicos reais. A precisão da análise depende da qualidade das imagens de entrada e da complexidade dos cariótipos.

## Contribuições

Contribuições são bem-vindas! Por favor, abra uma issue para discutir mudanças importantes antes de enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
