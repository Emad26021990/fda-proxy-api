from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/drug")
def get_drug(ndc: str):
    url = f"https://api.fda.gov/drug/label.json?search=openfda.product_ndc:{ndc}&limit=1"
    r = requests.get(url, timeout=10)
    data = r.json()

    result = data["results"][0]

    return {
        "brand_name": result.get("openfda", {}).get("brand_name", [""])[0],
        "generic_name": result.get("openfda", {}).get("generic_name", [""])[0],
        "manufacturer": result.get("openfda", {}).get("manufacturer_name", [""])[0],
        "active_ingredients": result.get("active_ingredient", [""])[0],
        "purpose": result.get("purpose", [""])[0],
        "indications": result.get("indications_and_usage", [""])[0],
        "do_not_use": result.get("warnings", [""])[0],
        "dosage": result.get("dosage_and_administration", [""])[0]
    }
