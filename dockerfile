    FROM python:3.12.7

    WORKDIR /app-restaurante

    # 3. Copie o arquivo requirements.txt para o diretório de trabalho no container
    COPY requirements.txt .

    # 4. Instale as dependências listadas no requirements.txt
    RUN pip install --no-cache-dir -r requirements.txt

    # 5. Copie o restante do código da aplicação para o diretório de trabalho no container
    COPY . . 

    # 6. Exponha a porta que o FastAPI irá usar (por exemplo, a 8000)
    EXPOSE 8000

    # 7. Defina o ENTRYPOINT para iniciar o Uvicorn
    ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

