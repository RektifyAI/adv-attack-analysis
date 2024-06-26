# Rektify AI Web Scraper

The web scraper is used to extract data from webpages using Python's BeautifulSoup and natural language processing. We wish to use DeFi exploit specific APIs to autonmously funnel data into REAL, but the DeFi industry is still relatively new.

<!-- image -->
<p style= "text-align:center;">
  <img src="data-retrieval.jpg" alt="" width="800" class="center" style="margin: 10px;"/>
</p>

To expand the data-driven functionality of Rektify AI we are building our own API with all the DeFi attack data we've curated, aggregated, and wrangled to be the one-stop shop for the DeFi ecosystem. In the meanwhile, Python's BeautifulSoup allows us to extract qualitative and quantative attack data from HTML/XML text inside of webpages. 

The following websites are used in Rektify web scraper:
>- [rekt.news](https://rekt.news) - #1 resource for DeFi hacks across the ecosystem
>- [bitcoinexchangeguide](https://bitcoinexchangeguide.com/bitcoin/scams-hacks/#Picostocks_Cold_Wallet_Hack)
>- [CertiK](https://www.certik.com)
>- [Token Insight](https://tokeninsight-api.readme.io/reference/api-overview)
>- [coingeek](https://coingeek.com/the-defi-hacks-of-2020/)
>- [coinintelligence](https://www.cointelligence.com/exchanges_list/) - Risk scores on CEXs
>- [cryptobriefing hack archive](https://cryptobriefing.com/tag/hack/)
>- [crypto.sec](https://cryptosec.info/defi-hacks/)
>- [crypto slam](https://cryptoslam.io)
>- [flipside crypto](https://app.flipsidecrypto.com/dashboard/solana-exploited-incident-analysis-xauPWQ)
>- [defiprime.com](https://defiprime.com/hacks2020)
>- [defiyieldapp-rektdatabase](https://defiyield.app/rekt-database)
>- [etherscan](https://etherscan.io)
>- [hedgewithcrypto](https://www.hedgewithcrypto.com/cryptocurrency-exchange-hacks/)
>- [idex](https://blog.idex.io/all-posts/a-complete-list-of-cryptocurrency-exchange-hacks-updated/#2012)
>- [rugdoc projects](https://rugdoc.io/project/)
>- [slowmist.io](https://hacked.slowmist.io/en/)
>- [squanch](https://github.com/TheSquanch-147/Rugpulls-Hacks-Exploits-List)
>- [quadrigainitiative](https://www.quadrigainitiative.com/hackfraudscam/btfinancehack.php)
>- [watchpug](https://watchpug.medium.com)
>- [wowisme](https://www.wowisme.net/defi-security-vulnerabilities-and-exploits-2021/)
>- [DeFi Hacks Analysis - Root Cause](https://wooded-meter-1d8.notion.site/0e85e02c5ed34df3855ea9f3ca40f53b?v=22e5e2c506ef4caeb40b4f78e23517ee)
>- [Forta Data](https://github.com/forta-network/labelled-datasets)
>- [Crypto Scam DB](https://cryptoscamdb.org/)
>- [Web3 Rekt](https://www.web3rekt.com/)
>- [Crypto Rank](https://cryptorank.io/news/)

# Get requests through APIs
>- TVL data: [DeFi Llama](https://docs.llama.fi/api)
>- Protocol behavior (real time alerts): [Twitter](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api), Discord
>- Overall DeFi market trends: [DeFi Pulse](https://docs.defipulse.com/api-docs-by-provider/defi-pulse-data) 
>- NFT API: [QuickNode](https://www.quicknode.com/nft-api), CryptoSlam
>- Social behavior of DeFi users/protocols: [LunarCrush](https://legacy.lunarcrush.com/developers/docs), [PyPi page](https://pypi.org/project/lunarcrush/)


The preceding are a few APIs Sena will be using to curate protocol specific data. DeFi Llama's API is a source to retrieve total value locked at the time of the exploit, a registery of DeFi protocols, and on-chain data. DeFi Pulse's API gives access to ETH gas prices as well as an on-slot of data providers for future needs. Twitter's API allows us to monitor protocol activity. All data curated from these APIs will be curated under columns in the SEAL dataset. 

----


## Insights into Web Scraping using Python BeautifulSoup & Autoscraper

Each data vector needed to be cleaned: protocol names, dates, and amount lost in attack.
The most intricate vector that needed prime attention were the dates. Dates and amounts with concatenated together with excessive spaces and a vertical bar(|). 

Here's an example of how the data is formatted within the HTML text: 
```
Input: '$55,000,000 | 11/05/2021'
```
The amount lost and dates are concatenated together which makes the task of curating each item difficult. But with BeautifulSoup the task is much easier.

> Here's a few lines of code used to extract the dates from the unstructured html text data:
```
clean_dates = [] # Empty list to store cleaned dates
for item in dates:
    i = item.lstrip(',000,000 | ') # Removes the leading characters
    
    clean_dates.append(i)
```
> Trial and error was used to find the proper parameters for the .lstrip method used to remove leading chars in Strings.
```
Output: 11/05/2021
```

> Redirect link: [Follow the logic and results in the web scraper directory.](https://github.com/SenaLabs/adv-attack-analysis/blob/main/web-scraper/rekt-news-ws.ipynb)

![](https://github.com/RektifyAI/adv-attack-analysis/web-scraper/gif-2-look.gif)

<!-- image -->
<p style="text-align:center;">
 
</p>
