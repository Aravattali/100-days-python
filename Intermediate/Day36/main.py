import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "4af86b960bb34b4f9f3e635c88be2e2b"
STOCK_API_KEY = "0DVEOOMCRJK27JRR"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## get yesterday closing price
stock_parms = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_parms)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
# print(yesterday_closing_price)

## get day before yesterday price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])
# print(day_before_yesterday_closing_price)

# Find the positive difference between 1 and 2
differ = abs(yesterday_closing_price - day_before_yesterday_closing_price)
# print(differ)

# Work out the percentage difference
difference_percetage = (differ / yesterday_closing_price) * 100
up_down = "🔺" if yesterday_closing_price > day_before_yesterday_closing_price else "🔻"
print(f"{STOCK_NAME}: {up_down}{difference_percetage:.2f}%")

# If percentage > 5 then get news
if difference_percetage > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": "Tesla",  # simpler query to ensure results
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 3
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    print(news_response.status_code)

    ## STEP 2: Get the first 3 news pieces for the COMPANY_NAME
    news_data = news_response.json()
    articles = news_data.get("articles", [])

    # TODO 6 - Instead of printing ("Get News"), use the News API to get articles
    # TODO 7 - Use slice to create a list that contains first 3 articles
    top_3_articles = articles[:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # TODO 8 - Create new list of first 3 article's headline and description
    article_summaries = [
        f"Headline: {article['title']}\nBrief: {article['description']}"
        for article in top_3_articles
    ]

    # Print the article summaries
    for summary in article_summaries:
        print(summary + "\n")

    # TODO 9 - Send each article as separate message via Twilio
