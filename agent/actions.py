def get_response_time(url):
    if url == "google.com":
        return 0.3
    if url == "openai.com":
        return 0.4
    else:
        return 0.8
    
def test(url):
    if url == "google.com":
        return "1.3"
    if url == "openai.com":
        return "1.4"
    else:
        return "1.8"