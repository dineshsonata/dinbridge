from fastapi import FastAPI

app=FastAPI()

lst=[10,20,30]  
#    0  1   2

# @app.get("<path of your url>")
# default url
@app.get("/")
def home():
    return {'data':lst}

@app.post("/add-data")
def addData():
    lst.append(100)
    return {'data':lst}

@app.post("/add-data-dynamic/{num}")
def addData(num:int):
    lst.append(num)
    return {'data':lst}

@app.put('/update-data')
def updateData():
    lst[0]=1000
    return {'data':lst}

@app.put('/update-data-dynamic/{index}')
def updateData(index:int):
    lst[index]=1000
    return {'data':lst}

@app.put('/update-data-data/{index}/{value}')
def updateData(index:int,value:int):
    lst[index]=value
    return {'data':lst}

@app.delete('/delete-data/{index}')
def deleteData(index:int):
    lst.remove(index)
    return {'data':lst}

@app.delete('/delete-all-data')
def deleteAllData():
    global lst
    lst=[]
    return {'data':lst}