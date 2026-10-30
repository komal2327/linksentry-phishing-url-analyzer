# LinkSentry Manual Test Samples and Evidence

These cases were checked interactively by running `python phishing_checker.py` and entering each sample at the prompt. They document the behavior shown in the captured terminal screenshots; they are manual examples, not an automated unit-test suite. Screenshot filenames refer to the shared [test_results Drive folder](https://drive.google.com/drive/folders/1sslceWflxJ4_b3HjVkr1mbDiP-LFS3UZ?usp=sharing).

| Test | Sample input | Expected/observed result | Screenshot evidence |
|---|---|---|---|
| HTTPS URL with no listed warning signs | `https://www.example.com/login` | Reports that no listed warning signs were found and reminds the user this does not prove safety. | `Screenshot 2026-10-31 012002.png` |
| HTTP URL with an IPv4 hostname | `http://192.0.2.10/account` | Reports an IP-address hostname and HTTP; displays 2 warning indicators. | `Screenshot 2026-10-31 011817.png`, `Screenshot 2026-10-31 012002.png`, `Screenshot 2026-10-31 012046.png` |
| At-sign in an HTTP URL | `http://example.com@sample.invalid/login` | Reports the `@` symbol and HTTP; displays 2 warning indicators. | `Screenshot 2026-10-31 012046.png` |
| Many hostname labels | `https://a.b.c.d.e.example.invalid/path` | Reports many hostname segments/subdomains. | `Screenshot 2026-10-31 012108.png` |
| Punycode-style hostname | `https://xn--example.invalid/` | Reports a punycode-style hostname. | `Screenshot 2026-10-31 012108.png` |
| Malformed URL | `http://[bad` | Reports an invalid URL format and prompts the user to check the syntax. | `Screenshot 2026-10-31 012128.png` |
| Empty input | *(press Enter without typing a URL)* | Reports that no URL was entered. | `Screenshot 2026-10-31 012128.png` |
| Quit command | `q` | Exits the interactive loop and displays the goodbye message. | `Screenshot 2026-10-31 012128.png` |

The same terminal session can include multiple inputs. Results are limited to the checks listed in the README; a result with no warnings must not be interpreted as confirmation that a URL is safe.
