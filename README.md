# Grupo-1-FSI-Tutorial-Flask

## Atividade 006 - Criar um gerenciador de atividades usando python/flask

Requisitos para rodar o código:

- Python 3.14.8 instalado
- pip atualizado
- extensão better jinja

```bash
pip install flask
```

Crie um Gerenciador de Atividades usando python/flask e os tutoriais:

- <https://www.youtube.com/watch?v=BUGZZaChiYw>
- <https://www.youtube.com/watch?v=c67GaAkf1BE>
- <https://www.youtube.com/watch?v=FjQCIfZbHgg> (Esse é o tutorial que usaremos como base)
- <https://www.youtube.com/playlist?list=PLMLdiraLeES2VyXBZusCdkcvDByKStS_->

Uma apresentação mostrando o funcionamento interno da sua aplicação. Nada de código. Separe sua aplicação em módulos e explique usando diagrama de atividades e diagrama de fluxo de tela. Os diagramas deverão ser desenhados no Figma.

- <https://canva.link/wff9ksxj629wl2b> Link da apresentação

Após instalar a extensão Better Jinja no VS Code, crie a pasta `.vscode` na raiz do projeto (se ela ainda não existir) e dentro dela crie o arquivo `settings.json` com o seguinte conteúdo para que o editor reconheça corretamente os arquivos HTML do Flask/Jinja:

```json
{
    "files.associations": {
        "**/templates/**/*.html": "jinja-html"
    }
}
```

Use "python app.py" para iniciar a aplicação Flask localmente. Esse comando executa o arquivo principal `app.py` e sobe o servidor em desenvolvimento, permitindo testar a aplicação no navegador.

- Para iniciar a aplicação localmente, execute:

```bash
cd gerenciador_de_tarefas
python app.py
```
