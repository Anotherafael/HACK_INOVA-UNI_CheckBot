# HACK_INOVA-UNI_CheckBot

Projeto desenvolvido para o evento <a href="https://www.unitins.br/Concursos/Publico/Home/S/4fb1f276c82f5faa8ed3e5c4ac2c6893" alt="Link to event" target="_blank">2ª EDIÇÃO DO HACKATHON INOVAUNI – E-GOV</a>

O Tema deste projeto é: "Sistema mais simples/compreensível de transparência".
Portanto, o sistema desenvolvido consiste em aplicar uma Inteligência Artificial para simplificar a busca por dados no Portal de Transparência do Estado do Tocantins (Expansível para os municípios).

# Como usar?
1. Instale o python, preferencialmente a versão 3.
2. Instale as dependências do arquivo requirements.txt: <br>
``` pip install -r requirements.txt ```
3. Crie um arquivo .env e insira as informações <br>
``` KEY=[INSIRA SUA API_KEY DO OPENAI]``` <br>
``` PROFILE_PRIMARY='Você é uma excelente e carismática assistente virtual.'``` <br>
``` PROFILE_SECONDARY='Seja simples e direto em suas respostas.``` <br>
``` ORGANIZATION=[INSIRA A ORGANIZATION DO OPENAI. EX: org-9FyNfODLsDJn0D8u0L5ac8Gl]``` <br>
4. Rode o uvicorn: <br>
``` uvicorn app:app --host=0.0.0.0 --port=8002 --workers=1 ``` <br>
