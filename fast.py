from fastapi import FastAPI, Request
 
app = FastAPI()
 
@app.get("/sample/{name}")
def root (name):
   return {"message": f"Hello {name}"} 


@app.post("/signup")
async def post_api(request: Request):

    return {"status":"success","message":" post API works","payload":eval(await request.body())}