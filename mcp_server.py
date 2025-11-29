# Main Task: Create AI Webscrapping tool

# Step1: Search the web

import http.client
import json
import os
from socket import timeout
import httpx
import asyncio
from dotenv import load_dotenv
load_dotenv()

#query="Chroma DB"

SERPER_URL= "https://google.serper.dev/search"

async def search_web(query:str)-> dict | None:

  payload = json.dumps({
    "q": query, "num":2
  })
  headers = {
    'X-API-KEY': os.getenv("SERPER_API_KEY"),
    'Content-Type': 'application/json'
  }



  #conn = http.client.HTTPSConnection("google.serper.dev")
  async with httpx.AsyncClient() as client:
    response=await client.post(
      SERPER_URL,headers=headers, data=payload,
      timeout=30.0
    )
    response.raise_for_status()
    return response.json()
    #conn.request("POST", "/search", payload, headers)
    #res = conn.getresponse()
    #data = res.read()
    #return (data.decode("utf-8"))

# res=asyncio.run(search_web(query="Chroma DB"))  
# print(res)


# Step2: Open the official documentation

async def fetch_url(url:str):
    # client
      async with httpx.AsyncClient() as client:
        # hit request to url
        response = await client.get(url, timeout=30.0)
        #parse and clean response
        cleaned_response=clean_html_to_txt(response)



# Step3: Read documentation and write code accordingly
