
import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    """
    Analyze URL text for selected phishing warning indicators.
    This function never visits or connects to the URL.
    """

    url = raw_url.strip()
    findings = []

    # Handle empty input
    if not url:
        return ["No URL entered."]

    # Add a default scheme if the user did not provide one
    candidate = url if "://" in url else "http://" + url

    # Improvement 1: Handle malformed URL formats
    try:
        parsed = urlparse(candidate)
        host = parsed.hostname

        if not host:
            return ["Could not identify a hostname."]

        host = host.lower()

    except ValueError:
        return [
            "Invalid URL format detected.",
            "Please check the URL syntax and try again."
        ]

    # Check 1: @ symbol
    if "@" in candidate:
        findings.append(
            "Contains an @ symbol; inspect carefully."
        )

    # Check 2: URL length
    if len(url) > 100:
        findings.append(
            "Unusually long URL (over 100 characters)."
        )

    # Check 3: IP address hostname
    ip_pattern = r"(?:\d{1,3}\.){3}\d{1,3}"

    if re.fullmatch(ip_pattern, host):
        findings.append(
            "Uses an IP address instead of a familiar domain."
        )

    # Check 4: Multiple hostname segments
    labels = [part for part in host.split(".") if part]

    if len(labels) >= 5:
        findings.append(
            "Contains many hostname segments/subdomains."
        )

    # Check 5: Punycode marker
    if "xn--" in host:
        findings.append(
            "Contains a punycode-style hostname."
        )

    # Check 6: HTTP scheme
    if parsed.scheme.lower() == "http":
        findings.append(
            "Uses HTTP. HTTPS alone does not prove trust."
        )

    # No warning indicators found
    if not findings:
        findings.append(
            "No listed warning signs found. "
            "This does NOT prove safety."
        )

    return findings


def main():

    print("=" * 55)
    print("             LINKSENTRY")
    print("       PHISHING URL AWARENESS ANALYZER")
    print("=" * 55)

    print("Mode: Offline URL text analysis")
    print("No websites are opened or contacted.")
    print("\nEnter 'q' to quit the application.")

    # Improvement 2: Continuous URL checking loop
    while True:

        try:
            raw_url = input(
                "\nEnter URL to analyze: "
            )

        except (EOFError, KeyboardInterrupt):
            print("\nExiting LinkSentry. Stay safe online!")
            break

        # Quit functionality
        if raw_url.strip().lower() in (
            "q", "quit", "exit"
        ):
            print("\nThank you for using LinkSentry!")
            print("Stay alert. Stay secure.")
            break

        # Analyze URL
        findings = inspect_url(raw_url)

        print("\n" + "-" * 55)
        print("             ANALYSIS RESULTS")
        print("-" * 55)

        for number, finding in enumerate(findings, start=1):
            print(f"{number}. {finding}")

        # Count actual warning indicators
        is_warning = (
            bool(findings)
            and not findings[0].startswith(
                ("No URL entered.",
                 "Could not identify",
                 "Invalid URL format",
                 "No listed warning")
            )
        )

        if is_warning:
            print("\n[!] REVIEW CAREFULLY")
            print(
                f"Warning indicators detected: {len(findings)}"
            )
        elif findings[0].startswith("Invalid URL format"):
            print("\n[!] INPUT ERROR")
        elif findings[0].startswith("Could not identify"):
            print("\n[!] INPUT ERROR")
        elif findings[0].startswith("No URL entered"):
            print("\n[!] EMPTY INPUT")
        else:
            print("\n[+] No listed warning indicators detected.")

        print(
            "\nReminder: No warning signs do NOT guarantee "
            "that a URL is safe."
        )

        print("-" * 55)


if __name__ == "__main__":
    main()
