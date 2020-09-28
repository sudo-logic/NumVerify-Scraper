# Phone-Number-Location-Scraper

A script to scrape data from http://numverify.com/ for free without having to make an account.

How To:

`
git clone https://github.com/Awesome-Logic/Phone-Number-Data-Scraper.git
cd Phone-Number\-Data\-Scraper
pip install -r requirements.txt
python scraper.py
`

Example Response:

`{
  "valid": true,
  "number": "14158586273",
  "local_format": "4158586273",
  "international_format": "+14158586273",
  "country_prefix": "+1",
  "country_code": "US",
  "country_name": "United States of America",
  "location": "Novato",
  "carrier": "AT&T Mobility LLC",
  "line_type": "mobile"
}`
