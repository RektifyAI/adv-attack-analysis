
## Insights into Web Scraping using Python BeautifulSoup

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

<!-- image -->
<p style="text-align:center;">
  <img src="images/rektnews_inspect_element.png" alt="" width="700" class="center" style="margin-left: 10px;"/>
</p>

## Insights into Web Scraping using Python AutoScraper
