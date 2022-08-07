## Twitter API Repo

Twitter is the most prevalently used social media application for crypto users. Twitter also hosts real-time alerts about on-chain and off-chain activity that is happening to blockchain-based assets. With Twitter we can track user sentiment and hack alerts.


### Tweet Validity Bot Program 
** Goal **
Capture as many phrases from users in the event of a hack to rank the severity of the attack based on their diction. Fake users tend to state they were a "victim" or "wen refund". 

Keywords or phases to look for from scammers:
- $ amounts
-  amoumt [token]
- victim
- refund
- returned
- "any chance of refund"
- 128-bit contract hash
- con't.

Keywords or phases to look for from actual victims:
- $ amounts
- 128-bit contract hash with image attachment


** Challenge **
The challenges arise in the raw data scraped from tweets are scammers fake sentiments. 

** Strategy **

