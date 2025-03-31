import argparse
from phishing_detector import load_model_and_scaler, predict_url
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

def main():
    parser = argparse.ArgumentParser(description="Phishing URL Detector")
    parser.add_argument("url", type=str, help="URL to evaluate")
    args = parser.parse_args()

    model, scaler = load_model_and_scaler()
    prediction, confidence = predict_url(args.url, model, scaler)

    print(f"URL: {args.url}")
    print(f"Phishing Detected: {'Yes' if prediction == 1 else 'No'}")
    print(f"Confidence Score: {confidence:.2%}")

if __name__ == "__main__":
    main()