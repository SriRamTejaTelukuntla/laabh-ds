# Logos

Brand logos for UPI apps, banks and payment apps, as components named `logo/<brand>` on the Logos page (`274:178`, section `Logos`) of the DS file.
Added and published 20 Oct 2026 from designer-supplied SVGs (MF KYC).

| Property | Value |
|---|---|
| Size | 48×48 frame; use at 32–48 (Avatar-sized slots, List Row leading) |
| Variants | `Shape`: Square, Circle |
| Colour | Raw brand colours by brand rule (not tokens), like `icon/brand-google`. They don't change between Light and Dark |
| Count | 67 brands, 134 variants |

## Rules
- Use the component instance; never redraw or recolour a logo.
- Pick a `List Row` leading slot (40) for app/bank pickers. Option Card's leading icon is fixed at 20 px, too small for wordmark logos (Paytm, BHIM).
- Logos are decorative next to their name (`AN-08`): the visible name is the label.
- Wordmark logos (BHIM, Paytm, TMB) are low-contrast on dark surfaces; check Dark before use.

## Brands
UPI and payment apps: `amazonpay`, `bhim`, `cred`, `dhani`, `digikhata`, `fampay`, `flipkart`, `googlepay`, `groww`, `jupiter`, `kiwi`, `make-my-trip`, `mobikwik`, `navi`, `niyo-global`, `omnicard`, `paytm`, `phonepe`, `samsung-pay`, `shriram-one`, `slice`, `tataneu`, `timepay`, `ultracash`, `whatsapp`, `bajaj-finserv`, `aditya-birla-capital-digital`.

Banks: `airtel-payments-bank`, `au-small-finance-bank`, `axis-bank`, `bank-of-baroda`, `bank-of-india`, `bank-of-maharashtra`, `canara-bank`, `central-bank-of-india`, `citi-bank`, `city-union-bank`, `dbs-digibank`, `deutsche-bank`, `equitas-small-finance-bank`, `federal-bank`, `fino-payment-bank`, `hdfc-bank`, `hsbc-bank`, `icici-bank`, `idbi-bank`, `idfc-bank`, `india-post-payments`, `indian-bank`, `indian-overseas-bank`, `indusind-bank`, `jammu-and-kashmir-bank`, `jio-payments-bank`, `karnataka-bank`, `karur-vysya-bank`, `kotak-mahindra-bank`, `nsdl-payments-bank`, `punjab-national-bank`, `punjab-sind-bank`, `rbl-bank`, `south-indian-bank`, `standard-chartered-bank`, `state-bank-of-india`, `tamilnad-mercantile-bank`, `uco-bank`, `union-bank`, `yes-bank`.

Source names were cleaned up: `krur-vyasya` → `karur-vysya`, `standard-charted` → `standard-chartered`, `deutsch` → `deutsche`, `mobiqwik` → `mobikwik`, `-apps`/`-bank-apps` suffixes dropped, and the CUB logo mislabelled `idbi-bank-apps` → `city-union-bank`.
