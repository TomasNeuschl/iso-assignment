from pydantic import BaseModel, constr


class CountryMatchRequest(BaseModel):
    iso: constr(min_length=3, max_length=3)
    countries: list[str]


class CountryMatchResponse(BaseModel):
    iso: str
    match_count: int
    matches: list[str]
