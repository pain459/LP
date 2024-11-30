from fastapi import FastAPI, HTTPException
from database import create_tables, add_sku_entry, get_stock_report

app = FastAPI()

# Initialize database
create_tables()

@app.post("/sku/add/")
def add_sku(sku_id: int, quantity: int, price: float = None):
    response = add_sku_entry(sku_id, quantity, price)
    if "error" in response:
        raise HTTPException(status_code=404, detail=response["error"])
    return response

@app.get("/stock-report/")
def stock_report():
    report = get_stock_report()
    return {"stock_report": report}
