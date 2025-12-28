from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/drug")
def get_drug(ndc: str):
    url = f"https://api.fda.gov/drug/label.json?search=openfda.product_ndc:{ndc}&limit=1"

    response = requests.get(url, timeout=10)
    data = response.json()

    result = data["results"][0]
    openfda = result.get("openfda", {})

    return {
        "brand_name": openfda.get("brand_name", [""])[0],
        "generic_name": openfda.get("generic_name", [""])[0],
        "manufacturer": openfda.get("manufacturer_name", [""])[0],
        "warnings": result.get("warnings", [""])[0]
    }
