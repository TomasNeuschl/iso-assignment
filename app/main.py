from fastapi import FastAPI, HTTPException

from app.iso_matcher.iso_matcher import ISOMatcher
from app.iso_matcher.serializers.match_country import CountryMatchResponse, CountryMatchRequest

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/match_country", response_model=CountryMatchResponse)
async def match_country(request_data: CountryMatchRequest):
    iso = request_data.iso
    countries = request_data.countries
    matcher = ISOMatcher()
    success, matches = matcher.match_country(iso, countries)
    if not success:
        raise HTTPException(status_code=404, detail="ISO code does not exist")
    if matches:
        return {
            "iso": iso,
            "match_count": len(matches),
            "matches": matches
        }
    else:
        raise HTTPException(status_code=404, detail="ISO code not found in the list of countries")
