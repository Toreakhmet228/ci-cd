from fastapi import FastAPI
import uvicorn
app=FastAPI()


@app.get("/")
def fet_data():
    return {"welcome":"hello world"}



if __name__=="__main__":
    uvicorn.run(port=8000,host="localhost",app=app)
