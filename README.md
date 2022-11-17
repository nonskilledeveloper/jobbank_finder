# JobBank_Finder 

## What it does?

This is a Web Scraper specially designed to find job offers from the canadian website [Job Bank](https://jobbank.gc.ca/) that matches with specific criterias that are not possible to configure in the own website, at least up today.

### GitHub Link -> [JobBank_Finder](github.com/)

Also, this software ranks the job offers, and generates a file with the results found that is very easy to read.

![](https://assets.nonskilledeveloper.com/16675304997229.jpg)


For example, I'm going to check the job offers avalaible today, which have a positive LMIA (Approved), that do not requires high education, that do not require previous experience...  Until now, all these criterias are possible to configure in the website, yes, but here it comes the interesting part:

We are going to point higher those offers that adds a link to their website, and that has an official email

Why? 

Because these offers are most likely possible to be oficial, real offers. It's known that there are too many scams on this website, and scammers commonly are lazy, they won't complicate themselves buying a website, and if they do it, probably this website will not be so well built, or it will be very generic, anyway, we'll have another thing to analyze before sending our curriculum, or any other kind of information.

![](https://assets.nonskilledeveloper.com/16675314895783.jpg)

So, the software starts analyzing every job offer in the website by itself, in the console it give us a small summary about what this software is finding, the section "Stars Rank" is the important part, since it will rank higher as it matches with our criterias, and these criterias are completely customizable by code (For the moment) and in the running time (I'll be working on it).

![](https://assets.nonskilledeveloper.com/16675319232825.jpg)

Finally as we can see, we get a folder, with the date of today, which contains all the information found. 

Let's open it... 

![](https://assets.nonskilledeveloper.com/16675320324870.jpg)

Inside we have an HTML file

![](https://assets.nonskilledeveloper.com/16675321433976.jpg)

And here we have... 

Certainly today we were not so lucky, because the maximun punctuation getted it was 0.5 in the Stars Rank (This rank works from 0 to 5 points), but i've had much better days, in fact, with this software I'm looking for a job for my father, and we have already got a call for an interview 

(Wish us luck) 🌵

## Legallity 

Neither the users agreements, the "robots.txt" section of the website or the canadian laws forbides to scrap in this website

## It worths it?

I'm completely sure that it worths to use it, since it can analyze, maybe hundred of offers per minute and rank them, a thing that for a human, it would be absolutely impossible to do 
