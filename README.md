# website_parsing-make-my-trip
Problem statement: Parse website makemytrip.com or goibibo.com to collect all the listed hotel details.

Step1: pick  website mentioned .
Step 2: analyse and find a pattern in hotel urls with city/ country etc details and also
use

● www.makemytrip.com/robots.txt

Step3: generate a pattern in urls by step 2, so that you can parse all the urls in your loop in the code.

Step 4: use BeautifulSoup library to parse obtained links from step 3, and figure out
html tags, classes or other property you need to extract out details and make a row to
be further added to your csv (result) file.
