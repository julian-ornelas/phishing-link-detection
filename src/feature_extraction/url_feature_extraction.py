import pandas as pd
import re
from urllib.parse import urlparse

def extract_url_features(url):
    parsed = urlparse(url)
    
    return {
        "url_length": len(url),
        "path_length": len(parsed.path),
        "subdomain_length": len(parsed.netloc.split('.')[0]) if '.' in parsed.netloc else 0,
        "n_dots": url.count('.'),
        "n_hyphens": url.count('-'),
        "n_underscore": url.count('_'),
        "n_slash": url.count('/'),
        "n_questionmark": url.count('?'),
        "n_equal": url.count('='),
        "n_at": url.count('@'),
        "n_and": url.count('&'),
        "n_redirection": url.count('//') - 1,
        "subdomain_level": parsed.netloc.count('.'),
        "path_level": parsed.path.count('/'),
        "has_https": int(parsed.scheme == "https"),
        "has_ip_address": int(bool(re.match(r'^\d{1,3}(\.\d{1,3}){3}$', parsed.netloc))),
    }

# Loads in one dataset, requires location of output
def process_dataset(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    if "URL" not in df or "Label" not in df:
        raise ValueError("Dataset must contain 'URL' and 'Label' columns.")

    df_features = df["URL"].apply(extract_url_features).apply(pd.Series)
    df_features["Label"] = df["Label"]

    df_features.to_csv(output_csv, index=False)
    print(f"Processed dataset saved to {output_csv}")