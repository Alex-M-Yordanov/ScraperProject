# ScrapperProject
## Site that provides single-page scraping from 3 sites by inputting keywords into a searchbar.


### Usage:
* When the user loads the site, they are presented with a search bar.
* The user shall put search words into the searchbar and press the magnifying glass icon.
* After some time, under the searchbar will appear 3 colums, each corresponding to the sites - Ardes.bg, Emag.bg and Technopolis.bg, as well as a "Sort by price" button.
* Each column will fill with the result items, generated by each site, for the keywords, used as input.
  ####  Note:
   >> The results shows will only be smartphones as that is the purpose of the site. If nothing shows up on an a column, that mean that, with this search input, the cooresponding site is not showing any smartphone products of its first page.
  #### Note:
   >> After multiple searches, if the column for Emag.bg is empty, this may be caused by Cloudfare's defence. You need to go to the site and show that you are not a bot.

  
* The "Sort by price" button sorts each column by the price of the item in ascending order. Any following presses of the button will just switch the sorting order.
* At the bottom, there is a button "About", that when pressed shows information about the Cloudfare problem and that the currency used is Bulgarian lev.

####  Technologies used: Python (Flask, BeautifulSoup4), HTML, CSS, JS
