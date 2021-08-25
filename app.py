import uvicorn # for asgi
import fastapi 
from fastapi import FastAPI

# Create the app object 
app = FastAPI()


@app.get("/")
def home():

	return {'Message': 'Hello from JSON'}

@app.get("/home")
def home1():
	return {'Hello':'Prakaysh'}


if __name__ == '__main__':
	uvicorn.run(app)


