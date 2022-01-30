# Sena Web Scaper

The web scraper is used to extract data from websites using Python's BeautifulSoup. We wish to use DeFi exploit specific APIs to autonmously funnel data into S.E.A.L., but the DeFi industry is still relatively new. The main API we can utilize at this time is the Nansen.ai API. We hope to land them as a potential partner. 

To expand the data-driven functionality of Sena we will have to build our own API with all the DeFi attack data we've curated to be the one-stop shop for the DeFi ecosystem. In the meanwhile, Python's BeautifulSoup allows us to extract qualitative and quantative attack data from HTML/XML text inside of webpages. 

The following websites are used in Sena's web scraper:
>- [rekt.news](https://rekt.news) - #1 Resource for DeFi hacks across the ecosystem
>- [slowmist.io](https://hacked.slowmist.io/en/)
>- [crypto.sec](https://cryptosec.info/defi-hacks/)
>- [defiprime.com](https://defiprime.com/hacks2020)

<!-- image -->
<p style="text-align:center;">
  <img src="data-retrieval.jpg" alt="" width="800" class="center" style="margin: 10px;"/>
</p>

# Get requests through APIs
[DeFi Llama](https://docs.llama.fi/api), [Twitter](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api), [DeFi Pulse](https://docs.defipulse.com/api-docs-by-provider/defi-pulse-data) are a few APIs Sena will be using to curate protocol specific data. DeFi Llama's API is a source to retrieve total value locked at the time of the exploit, a registery of DeFi protocols, and on-chain data. DeFi Pulse's API gives access to ETH gas prices as well as an on-slot of data providers for future needs. Twitter's API allows us to monitor protocol activity. All data curated from these APIs will be curated under columns in the S.E.A.L. dataset. 
