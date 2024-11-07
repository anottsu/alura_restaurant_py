From fastapi import fastAPI 

app = fastAPI()

@app.get('/api/hello')

def hello_word():
    return {'Hello':'World'}