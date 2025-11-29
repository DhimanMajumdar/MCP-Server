import trafilatura

def clean_html_to_txt(html):
    try:  
        extracted = trafilatura.extract(
            html,
            include_comments=False,
            include_tables=False,
            favor_recall=False,
        )
        if extracted:
            return extracted
    except Exception as e:
        raise e