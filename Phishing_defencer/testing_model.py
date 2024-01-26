import joblib
import pandas as pd
from urllib.parse import urlparse
from model import model_RF

def test_fnx(user_input_url):

    user_input_length_url = len(user_input_url) 
    url_components = urlparse(user_input_url)
    length_hostname = len(url_components.netloc)

    nb_dots = user_input_url.count('.')
    nb_hyphens = user_input_url.count('-')
    nb_at = user_input_url.count('@')
    nb_qm = user_input_url.count('?')
    nb_percent = user_input_url.count('%')
    nb_slash = user_input_url.count('/')
    nb_and = user_input_url.count('&')
    nb_or = user_input_url.count('|')
    nb_eq = user_input_url.count('=')
    nb_star = user_input_url.count('*')
    nb_colon = user_input_url.count(':')
    nb_comma = user_input_url.count(',')
    nb_semicolon = user_input_url.count(';')
    nb_dollar = user_input_url.count('$')
    nb_underscore = user_input_url.count('_')
    nb_tilde = user_input_url.count('~')
    nb_space = user_input_url.count(' ')
    nb_www = user_input_url.count('www')
    nb_com = user_input_url.count('com')

    http_in_path = "http" in url_components.path.lower()
    https_token = "https" in user_input_url.lower()
    try:
        ratio_digits_url = sum(c.isdigit() for c in user_input_url) / len(user_input_url)
        ratio_digits_host = sum(c.isdigit() for c in url_components.netloc) / len(url_components.netloc)
    except Exception as e:
        print("The link is not of the standard type",e)

    punycode = url_components.netloc.encode('idna').decode('utf-8') != url_components.netloc
    port = bool(url_components.port)
    tld_in_path = url_components.path.endswith(('.com', '.net', '.org', '.edu','.in'))  # Adjust TLDs as needed
    tld_in_subdomain = any(subdomain.endswith(('.com', '.net', '.org', '.edu','.in')) for subdomain in url_components.netloc.split('.'))

    subdomain = user_input_url.split('//')[-1].split('/')[0]
    abnormal_subdomain = 1 if subdomain.lower() == 'abnormal_subdomain' else 0
    nb_subdomains = len(url_components.netloc.split('.'))
    prefix_suffix = user_input_url.startswith('http://') or user_input_url.startswith('https://')


    def is_url_shortened(url):
        shortening_service_domains = ['bit.ly', 'goo.gl', "shorte.st", "go2l.ink", "x.co", "ow.ly", "t.co", "tinyurl", "tr.im", "is.gd", "cli.gs", 
                          "ryfrog.com", "migre.me", "ff.im", "tiny.cc", "url4.eu", "twit.ac", "su.pr", "twurl.nl", "snipurl.com",
                          "rshort.to", "BudURL.com", "ping.fm", "post.ly", "Just.as", "bkite.com", "snipr.com", "fic.kr", "loopt.us", 
                          "rdoiop.com", "short.ie", "kl.am", "wp.me", "rubyurl.com", "om.ly", "to.ly", "bit.do", "t.co", "lnkd.in", "db.tt",  
                          "rqr.ae", "adf.ly", "goo.gl", "bitly.com", "cur.lv", "tinyurl.com", "ow.ly", "ity.im", "q.gs", "is.gd",
                          "rpo.st", "bc.vc", "twitthis.com", "u.to", "j.mp", "buzurl.com", "cutt.us", "u.bb", "yourls.org", "x.co",
                          "rprettylinkpro.com", "scrnch.me", "filoops.info", "vzturl.com", "qr.net", "1url.com", "tweez.me"," v.gd",
                          "rtr.im", "link.zip.net"]

        for domain in shortening_service_domains:
            if domain in url:
                return True
        if '/u/' in url or '/go/' in url or '/redirect/' in url:
            return True
        return False

    def has_path_extension(url):
        return '.' in url.split('/')[-1]

    def count_redirections(url):
        redirection_indicators = ['//', '/redirect/', '/go/', '/out/', '/away/', '/exit/', '/leave/']
        return sum(url.count(indicator) for indicator in redirection_indicators)

    def count_external_redirections(url):
        external_redirection_indicators = ['external-link', 'redirect?url=', 'out.php?url=', 'go.php?url=']
        return sum(url.count(indicator) for indicator in external_redirection_indicators)

    def length_words_raw(url):
        words = url.split()
        return len(words)

    def char_repeat(url):
        repeat_count = sum(url.count(char) for char in set(url) if url.count(char) > 1)
        return repeat_count

    def shortest_words_raw(url):
        words = url.split()
        shortest_length = min(len(word) for word in words)
        return shortest_length
    
    def shortest_word_host(url):
        host = url.split('//')[-1].split('/')[0]    
        words = host.split('.')
        shortest_length = min(len(word) for word in words)
        return shortest_length

    def shortest_word_path(url):
        path = url.split('//')[-1].split('/', 1)[-1]
        words = path.split('/')
        shortest_length = min(len(word) for word in words)
        return shortest_length
    
    def longest_words_raw(url):
        words = url.split()
        longest_length = max(len(word) for word in words)
        return longest_length

    def longest_word_host(url):
        host = url.split('//')[-1].split('/')[0]
        words = host.split('.')
        longest_length = max(len(word) for word in words)
        return longest_length
    
    def longest_word_path(url):
        path = url.split('//')[-1].split('/', 1)[-1]
        words = path.split('/')    
        longest_length = max(len(word) for word in words)
        return longest_length

    def avg_words_raw(url):
        words = url.split()
        if len(words) > 0:
            avg_length = sum(len(word) for word in words) / len(words)
        else:
            avg_length = 0
        return avg_length


    

    is_shortened = is_url_shortened(user_input_url)
    path_extension = 1 if has_path_extension(user_input_url) else 0
    nb_redirection = count_redirections(user_input_url)
    nb_external_redirection = count_external_redirections(user_input_url)
    length_words_raw_feature = length_words_raw(user_input_url)
    char_repeat_feature = char_repeat(user_input_url)
    shortest_words_raw_feature = shortest_words_raw(user_input_url)
    shortest_word_host_feature = shortest_word_host(user_input_url)
    shortest_word_path_feature = shortest_word_path(user_input_url)
    longest_words_raw_feature = longest_words_raw(user_input_url)
    longest_word_host_feature = longest_word_host(user_input_url)
    longest_word_path_feature = longest_word_path(user_input_url)
    avg_words_raw_feature = avg_words_raw(user_input_url)
    




    # Additional features

    # # Additional features
    # avg_words_raw = sum(len(word) for word in user_input_url.split()) / len(user_input_url.split())
    # avg_word_host = sum(len(word) for word in url_components.netloc.split('.')) / len(url_components.netloc.split('.'))
    # avg_word_path = sum(len(word) for word in url_components.path.split('/')) / len(url_components.path.split('/'))
    # phish_hints = False  # Placeholder, you can modify this based on your criteria
    # domain_in_brand = False  # Placeholder, you can modify this based on your criteria
    # brand_in_subdomain = False  # Placeholder, you can modify this based on your criteria
    # brand_in_path = False  # Placeholder, you can modify this based on your criteria
    # suspecious_tld = False  # Placeholder, you can modify this based on your criteria
    # statistical_report = False  # Placeholder, you can modify this based on your criteria

    # # Additional features
    # nb_hyperlinks = 0  # Placeholder, you can modify this based on your criteria
    # ratio_intHyperlinks = 0.0  # Placeholder, you can modify this based on your criteria
    # ratio_extHyperlinks = 0.0  # Placeholder, you can modify this based on your criteria
    # ratio_nullHyperlinks = 0.0  # Placeholder, you can modify this based on your criteria
    # nb_extCSS = 0  # Placeholder, you can modify this based on your criteria
    # ratio_intRedirection = 0.0  # Placeholder, you can modify this based on your criteria
    # ratio_extRedirection = 0.0  # Placeholder, you can modify this based on your criteria
    # ratio_intErrors = 0.0  # Placeholder, you can modify this based on your criteria
    # ratio_extErrors = 0.0  # Placeholder, you can modify this based on your criteria
    # login_form = False  # Placeholder, you can modify this based on your criteria
    # external_favicon = False  # Placeholder, you can modify this based on your criteria
    # links_in_tags = 0  # Placeholder, you can modify this based on your criteria
    # submit_email = False  # Placeholder, you can modify this based on your criteria
    # ratio_intMedia = 0.0  # Placeholder, you can modify this based on your criteria
    # ratio_extMedia = 0.0  # Placeholder, you can modify this based on your criteria
    # sfh = False  # Placeholder, you can modify this based on your criteria
    # iframe = False  # Placeholder, you can modify this based on your criteria
    # popup_window = False  # Placeholder, you can modify this based on your criteria
    # safe_anchor = False  # Placeholder, you can modify this based on your criteria
    # onmouseover = False  # Placeholder, you can modify this based on your criteria
    # right_clic = False  # Placeholder, you can modify this based on your criteria
    # empty_title = False  # Placeholder, you can modify this based on your criteria
    # domain_in_title = False  # Placeholder, you can modify this based on your criteria
    # domain_with_copyright = False  # Placeholder, you can modify this based on your criteria
    # whois_registered_domain = False  # Placeholder, you can modify this based on your criteria
    # domain_registration_length = 0  # Placeholder, you can modify this based on your criteria
    # domain_age = 0  # Placeholder, you can modify this based on your criteria
    # web_traffic = 0  # Placeholder, you can modify this based on your criteria
    # dns_record = 0  # Placeholder, you can modify this based on your criteria
    # google_index = 0  # Placeholder, you can modify this based on your criteria
    # page_rank = 0  # Placeholder, you can modify this based on your criteria



    # Create a DataFrame with the user input
    user_input_data = pd.DataFrame({
        'url': [hash(user_input_url)],
        'length_url': [user_input_length_url],
        'length_hostname': [length_hostname],
        'nb_dots': [nb_dots],
        'nb_hyphens': [nb_hyphens],
        'nb_at': [nb_at],
        'nb_qm': [nb_qm],
        'nb_and': [nb_and],
        'nb_or': [nb_or],
        'nb_eq': [nb_eq],
        'nb_underscore': [nb_underscore],
        'nb_tilde': [nb_tilde],
        'nb_percent': [nb_percent],
        'nb_slash': [nb_slash],
        'nb_star': [nb_star],
        'nb_colon': [nb_colon],
        'nb_comma': [nb_comma],
        'nb_semicolumn': [nb_semicolon],
        'nb_dollar': [nb_dollar],
        'nb_space': [nb_space],
        'nb_www': [nb_www],
        'nb_com': [nb_com],
        'http_in_path':[http_in_path],
        'https_token':[https_token],
        'ratio_digits_url':[ratio_digits_url],
        'ratio_digits_host':[ratio_digits_host],
        'punycode':[punycode],
        'port':[port],
        'tld_in_path':[tld_in_path],
        'tld_in_subdomain':[tld_in_subdomain], 
        'abnormal_subdomain': [abnormal_subdomain],
        'nb_subdomains': [nb_subdomains],
        'prefix_suffix':[prefix_suffix],
    #     'random_domain':[random_domain]
        'shortening_service': [is_shortened],
        'path_extension': [path_extension],
        'nb_redirection': [nb_redirection], 
        'nb_external_redirection': [nb_external_redirection],
        'length_words_raw': [length_words_raw_feature],
        'char_repeat': [char_repeat_feature],
        'shortest_words_raw': [shortest_words_raw_feature],
        'shortest_word_host': [shortest_word_host_feature],
        'shortest_word_path': [shortest_word_path_feature],
        'longest_words_raw': [longest_words_raw_feature],
        'longest_word_host': [longest_word_host_feature],
        'longest_word_path': [longest_word_path_feature],
        'avg_words_raw': [avg_words_raw_feature]
        
    })

    prediction = model_RF.predict(user_input_data)


    a=pd.DataFrame(prediction)

    status=a.iloc[0, 0]
    return status
