from fastapi import FastAPI, HTTPException
from etcd import Client

app = FastAPI()

# etcd client configuration
etcd_client = Client(host='etcd', port=2379)


# Create (POST) a new key-value pair
@app.post('/set_key')
async def set_key(key: str, value: str):
    if not key or not value:
        raise HTTPException(status_code=400, detail='Key and value are required.')
    try:
        etcd_client.write(key, value)
        return {'message': 'Key-value pair created successfully.'}
    except etcd.EtcdAlreadyExist:
        raise HTTPException(status_code=409, detail='Key already exists.')


# Read (GET) a value by key
@app.get('/get_key/{key}')
async def get_key(key: str):
    try:
        value = etcd_client.read(key).value
        return {key: value}
    except etcd.EtcdKeyNotFound:
        raise HTTPException(status_code=404, detail='Key not found.')


# Update (PUT/PATCH) an existing key-value pair
@app.put('/update_key/{key}')
@app.patch('/update_key/{key}')
async def update_key(key: str, value: str):
    if not value:
        raise HTTPException(status_code=400, detail='Value is required.')
    try:
        etcd_client.write(key, value)
        return {'message': 'Key-value pair updated successfully.'}
    except etcd.EtcdKeyNotFound:
        raise HTTPException(status_code=404, detail='Key not found.')


# Delete (DELETE) a key-value pair
@app.delete('/delete_key/{key}')
async def delete_key(key: str):
    try:
        etcd_client.delete(key)
        return {'message': 'Key deleted successfully.'}
    except etcd.EtcdKeyNotFound:
        raise HTTPException(status_code=404, detail='Key not found.')


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)
