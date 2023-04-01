
# GoogleSearchParser

This component uses the Google Custom Search API to search for the provided query related to ChatGPT jailbreaks and parses the top 10 website URLs. It sends the API request with the search query, retrieves the search results, and extracts the URLs from the top 10 results.

## Initial generation prompt
description: This component uses the Google Custom Search API to search for the provided
  query related to ChatGPT jailbreaks and parses the top 10 website URLs.
inputs:
  FROM_NODE:
    search_query: str
name: GoogleSearchParser


## Transformer breakdown
- Send a request to the Google Custom Search API with search_query
- Retrieve the search results from the API response
- Parse and extract the top 10 website URLs from the search results

## Parameters
[]

        