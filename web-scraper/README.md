# Sena Web Scraper

The web scraper is used to extract data from webpages using Python's BeautifulSoup. We wish to use DeFi exploit specific APIs to autonmously funnel data into SEAL, but the DeFi industry is still relatively new. The main API we can utilize at this time is the Nansen.ai API. We hope to land them as a potential partner. 

To expand the data-driven functionality of Sena we will have to build our own API with all the DeFi attack data we've curated to be the one-stop shop for the DeFi ecosystem. In the meanwhile, Python's BeautifulSoup allows us to extract qualitative and quantative attack data from HTML/XML text inside of webpages. 

The following websites are used in Sena's web scraper:
>- [rekt.news](https://rekt.news) - #1 resource for DeFi hacks across the ecosystem
>- [CertiK](https://www.certik.com)
>- [coingeek](https://coingeek.com/the-defi-hacks-of-2020/)
>- [cryptobriefing hack archive](https://cryptobriefing.com/tag/hack/)
>- [crypto.sec](https://cryptosec.info/defi-hacks/)
>- [crypto slam](https://cryptoslam.io)
>- [defiprime.com](https://defiprime.com/hacks2020)
>- [etherscan](https://etherscan.io)
>- [hedgewithcrypto](https://www.hedgewithcrypto.com/cryptocurrency-exchange-hacks/)
>- [rugdoc projects](https://rugdoc.io/project/)
>- [slowmist.io](https://hacked.slowmist.io/en/)
>- [squanch](https://github.com/TheSquanch-147/Rugpulls-Hacks-Exploits-List)
>- [quadrigainitiative](https://www.quadrigainitiative.com/hackfraudscam/btfinancehack.php)
>- [wowisme](https://www.wowisme.net/defi-security-vulnerabilities-and-exploits-2021/)

<!-- image -->
<p style="text-align:center;">
  <img src="data-retrieval.jpg" alt="" width="800" class="center" style="margin: 10px;"/>
</p>

# Get requests through APIs
>- TVL data: [DeFi Llama](https://docs.llama.fi/api)
>- Protocol behavior: [Twitter](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api)
>- Overall DeFi market trends: [DeFi Pulse](https://docs.defipulse.com/api-docs-by-provider/defi-pulse-data) 
>- Social behavior of DeFi users/protocols: [LunarCrush](https://legacy.lunarcrush.com/developers/docs), [PyPi page](https://pypi.org/project/lunarcrush/)


The preceding are a few APIs Sena will be using to curate protocol specific data. DeFi Llama's API is a source to retrieve total value locked at the time of the exploit, a registery of DeFi protocols, and on-chain data. DeFi Pulse's API gives access to ETH gas prices as well as an on-slot of data providers for future needs. Twitter's API allows us to monitor protocol activity. All data curated from these APIs will be curated under columns in the S.E.A.L. dataset. 
