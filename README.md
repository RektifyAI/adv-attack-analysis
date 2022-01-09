# Advanced Attack Analysis

The Advanced Attack Analysis is a deep data analysis repo, uncovering the latest insights on attacks within the DeFi ecosystem. Methods such as EDA, web scrapping, Python requests, and API manipulation are used to retrieve attack specific data.

This repo equips Sena with the ability to utilize past attack data to perform predictive and prescriptive analytics using machine learning as well as building models that will be used as data visualizations in the Sena UI stack. The inception of DeFi is a contentious  subject but within our analysis we funnel attack date from the later MakerDAO and Ethereum days around 2016 where more and more new chains began to emerge to partipate in the DeFi ecosystem. Attacks recorded from 2016 till now are utilized to make inferences on the past.

Sena allots for machine learning tactics such as supervised learning to created regression models and predictive models with the Sena attack dataset along with relevant metadata. 

The web scraper is used to web scrap websites using Python's BeautifulSoup and API commands to autonmously funnel data into the attack dataset. The following websites are used in Sena's web scraper:
>- [rekt.news](https://rekt.news) - #1 resource for DeFi hacks across the ecosystem
>- [slowmist.io](https://hacked.slowmist.io/en/)
>- [crypto.sec](https://cryptosec.info/defi-hacks/)
>- [defiprime.com](https://defiprime.com/hacks2020)

----

## Insights into Web Scrapping using Python BeautifulSoup
<!-- image -->
<p style="text-align:center;">
  <img src="main_inspect_element.png" alt="" width="450" class="center" style="margin-right: 5px;"/>
</p>

Each data vector needed to be cleaned: protocol names, dates, and amount lost in attack
The most intricate vector that needed prime attention were the dates. Dates and amounts with concatenated together with excessive spaces and a vertical bar(|). 

> Here's a few lines of code used to extract the dates from the excessive html text data:
```
clean_dates = []
for item in dates:
    regex = " (\\d{2}/\\d{2}/\\d{4})";
    i = item.lstrip(',000,000 | ')
    
    clean_dates.append(i)
```
> [Follow the logic and results within the web scraper directory.](https://github.com/SenaLabs/adv-attack-analysis/blob/main/web-scraper/rekt-news-ws.ipynb)

## Rhythm & Research: Discovering vulnerabilities before the attacks happen
Attacks only exist due to vulnerabilities and [attack vectors](https://github.com/sigp/solidity-security-blog). Throughout building the code base, within the attack analysis repo we will do extensive research into specific vulnerabilities with the code for DeFi protocols. 
