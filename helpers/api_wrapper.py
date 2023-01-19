#!/usr/bin/env python
# coding: utf-8

from dotenv import load_dotenv
import os
import requests as re

## endpoint
apiEndpoint = "https://public-api.defiyield.app"

## headers
headers = {
    'X-Api-Key': os.environ["API_KEY"] 
}

test_query = """
{
    rekts(
        pageNumber:1
        pageSize:10
        searchText: "terra"
        orderBy: {
            fundsLost: desc
        }
    ){
        id
        projectName
        description
    }
}
"""

def runTest():
    return re.post(apiEndpoint + "/graphql", headers = headers, json = {'query':test_query})

def runQuery(gqlQuery):
    response = re.post(apiEndpoint + "/graphql", headers = headers, json = {'query':gqlQuery})
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Query failed - status code: {response.status_code}")