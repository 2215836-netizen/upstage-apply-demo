import requests
import pandas as pd
import datetime

def fetch_industry_news(query, api_key):
    """
    Fetches news data from NewsAPI based on the query.
    Returns a pandas DataFrame with selected columns.
    """
    if not api_key:
        return pd.DataFrame()

    url = "https://newsapi.org/v2/everything"
    
    # Get news from the last 30 days
    from_date = (datetime.date.today() - datetime.timedelta(days=30)).isoformat()
    
    params = {
        'q': query,
        'from': from_date,
        'sortBy': 'relevancy',
        'apiKey': api_key,
        # 'language': 'en', # Commented out to allow queries like '반도체' to find Korean news
        'pageSize': 20
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        articles = data.get('articles', [])
        if not articles:
            return pd.DataFrame()

        # Extract relevant fields
        cleaned_data = []
        for art in articles:
            cleaned_data.append({
                'title': art.get('title'),
                'description': art.get('description'),
                'source': art.get('source', {}).get('name'),
                'publishedAt': art.get('publishedAt'),
                'url': art.get('url')
            })
            
        return pd.DataFrame(cleaned_data)
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return pd.DataFrame()
