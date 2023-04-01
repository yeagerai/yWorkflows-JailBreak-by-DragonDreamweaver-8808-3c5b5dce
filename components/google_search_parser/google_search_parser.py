
import os
from typing import List, Optional
import yaml
import requests
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.abstract_component import AbstractComponent


class GoogleSearchParserInputDict(BaseModel):
    search_query: str


class GoogleSearchParserOutputDict(BaseModel):
    top_10_urls: List[str]


class GoogleSearchParser(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.google_search_api_key: Optional[str] = os.environ.get(
            yaml_data["parameters"]["google_search_api_key"]
        )
        self.google_custom_search_engine_id: Optional[str] = os.environ.get(
            yaml_data["parameters"]["google_custom_search_engine_id"]
        )

    def transform(
        self, args: GoogleSearchParserInputDict
    ) -> GoogleSearchParserOutputDict:
        google_search_endpoint = f"https://www.googleapis.com/customsearch/v1?key={self.google_search_api_key}&cx={self.google_custom_search_engine_id}&q={args.search_query}"
        response = requests.get(google_search_endpoint).json()
        top_10_results = response["items"]

        top_10_urls = [result["link"] for result in top_10_results]

        return GoogleSearchParserOutputDict(top_10_urls=top_10_urls)


load_dotenv()
google_search_parser_app = FastAPI()


@google_search_parser_app.post("/transform/")
async def transform(
    args: GoogleSearchParserInputDict
) -> GoogleSearchParserOutputDict:
    google_search_parser = GoogleSearchParser()
    return google_search_parser.transform(args)
