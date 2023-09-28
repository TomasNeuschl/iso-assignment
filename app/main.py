import redis
from fastapi import FastAPI, HTTPException

from app.iso_matcher.iso_matcher import ISOMatcher
from app.iso_matcher.serializers.match_country import CountryMatchResponse, CountryMatchRequest
from app.redis_chacher import cache_result

app = FastAPI()

# Configure the Redis client
redis_host = "127.0.0.1"
redis_port = 6379
redis_db = 0


redis_client = redis.Redis(host=redis_host, port=redis_port, db=redis_db)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/match_country", response_model=CountryMatchResponse)
async def match_country(request_data: CountryMatchRequest):
    iso = request_data.iso
    countries = request_data.countries
    matcher = ISOMatcher(iso, countries)

    @cache_result(redis_client, ttl=600)
    def match_country_cached(iso, countries):
        return matcher.match_country()

    matcher = match_country_cached(iso, countries)

    if not matcher.success:
        raise HTTPException(status_code=404, detail="ISO code does not exist")
    if matcher.matches:
        return {
            "iso": iso,
            "match_count": len(matcher.matches),
            "matches": matcher.matches
        }
    else:
        raise HTTPException(status_code=404, detail="ISO code not found in the list of countries")
