# MF KYC: simulated user test (3 personas)

> **Simulated, not real users.** Claude walked the current Figma screens (2026-10-20, rounds 3–4) in each persona's voice, screen by screen, on the path that persona would take.
> Use it to pick what to test with real people, not as evidence on its own. Screen IDs match `plan.md`.
> Written by the same reviewer as `review.md`, so its agreement with DR-01–DR-05 is not independent confirmation.

## Personas

| | Ramesh Deshmukh, 58 | Sneha Iyer, 27 | Imran Qureshi, 36 |
|---|---|---|---|
| Who | Retired government clerk, Nagpur. Hindi-first, reads English slowly. Budget Android phone his son set up. Uses PhonePe for bills and pension withdrawals | Software engineer, Bengaluru. Already invests through Groww and Zerodha Coin. Impatient, skims, compares apps | Owns a kirana shop, Lucknow. Self-employed, irregular income. Joint savings account with his wife; Paytm for the shop. Wary of sharing data |
| Goal | "₹1,000 har mahine, safe jagah" (₹1,000 a month somewhere safe) | Move one SIP here if it's faster and cheaper | Start saving for his son's education |
| Path | KRA verified · bank found from mobile · nominee: wife · SIP ₹1,000 | KRA verified · Google sign-in · second bank via UPI · SIP ₹5,000 | Not on KRA (DigiLocker) · joint account rejected · Paytm UPI · 2 nominees incl. a minor |

---

## Ramesh, 58 (raw)

**M00 Welcome:** "Direct plans, commission nahi… achha. 'SEBI-registered' padh ke thoda bharosa hua. 5 se 10 minute? Dekhte hain."

**M01 Mobile number:** "Number linked to bank account… mera pension wala SBI account isi number pe hai. Theek hai."

**M02 Verify mobile:** "OTP apne aap aa gaya aur page aage chala gaya. Neeche koi checkbox tha kya? Maine dekha hi nahi." *(The bureau consent was never ticked, so he lands on M07b and has to type his PAN.)*

**M03 Set MPIN:** "MPIN? Ye UPI PIN hai kya? PhonePe wala daal doon?" *(Hesitates for a long time. He nearly types his UPI PIN.)* "Kahin likha hota ki ye sirf is app ke liye hai…"

**M03b Confirm MPIN:** "Phir se daalna hai. Theek."

**M04 Email:** "Google wala button dabaya, ho gaya. Statements email pe aayenge, achha hai."

**M07b Enter PAN & DOB:** "PAN card nikaalna pada. Calendar wala option achha hai, date type karna mushkil hota hai."

**M20 Confirm bank account:** "Arre, SBI account khud aa gaya! Naam mera hai. 'Yes, use this account.' Badiya." *(Delight moment. He didn't notice there was no "only my name" question.)*

**M13 Personal details:** "Pitaji ka naam pehle se bhara hai. Gender, marital… daba diya. Address purana wala hai par sahi hai."

**M14 A few more details:** "Occupation: 'Retired' mil gaya. Income… pension ₹3 lakh saal ka, 'Below 5 lakh' hoga. Neeche wala box pehle se tick hai? Theek hai, mujhe kya pata politically exposed kya hota hai." *(He continues without reading the declaration because it is already ticked: DR-02.)*

**M17/M18 Nominee:** "Patni ka naam daal diya, 100%. Easy."

**M27 Make your account investment-ready:** "Application submitted, achha. Autopay… 'Up to ₹15,000'. Kya 15,000 kat jaayega? Mere account mein itna nahi rehta." *(Reads 'Used for your SIPs, on their dates' twice.)* "Matlab jitna SIP utna hi katega? Pakka? Beta se poochhunga." *(He taps "I'll do this later".)*

**M28 Start a SIP:** "₹1,000 likha, 10 tarikh, pension aata hai 1 ko… 5 tarikh theek hai."

**M29 Review your SIP:** "Charges ₹0. Badiya, koi kharcha nahi." *(He believes there is no cost at all: DR-01.)*

**M30 Set up autopay:** "Phir se 15,000. 'Skip for now' hai, achha hai, zabardasti nahi. Par phir SIP chalega kaise?"

**Overall:** "Bank wala part sabse achha tha. MPIN aur 15,000 wali baat samajh nahi aayi. Beta ke saath baith ke karunga."

---

## Sneha, 27 (raw)

**M00 Welcome:** "Skipping. Get started."

**M01 → M02:** "Autofill, auto-verify, nice, zero taps. Wait, was there a consent checkbox? It moved on before I read anything."

**M03 Set MPIN:** "Another PIN. Groww has fingerprint. Can I just use Face ID? If MPIN is a must, fine, but offer biometrics right after."

**M04 Email:** "'Where should we send your statements?' I like that, it tells me why. Google, done."

**M07b Enter PAN & DOB:** "Why am I typing my PAN? Other apps prefill this from my number. Oh, that was the checkbox I skipped on the OTP screen. Annoying."

**M20 Confirm bank account:** "It found my HDFC account, but my salary goes to ICICI. 'Add another account', good that it's there."

**M20b Verify bank with UPI:** "PhonePe, Google Pay, Paytm, BHIM with real logos, feels legit. Pay ₹1, refunded same day. Standard. Easy."

**M13 / M14:** "Gender and marital have no default, good. Occupation sheet is fine. The declaration is pre-ticked? That's sketchy, normally you make me tick it." *(Unticks and re-ticks it, then loses trust a little.)*

**M14 nominee switch:** "Off for now. Wait, does off mean I'm opting out forever? It doesn't say I can add later."

**M27 Make your account investment-ready:** "Autopay first, fine. But the fund list has no returns, no expense ratio, no AUM. 'Popular with first-time investors' isn't a reason to pick a fund. I'll search."

**M27 search:** "Typed Parag Parikh… is there a results screen? I can't tell from here." *(No results or empty state designed.)*

**M28 Start a SIP:** "₹5,000, the +₹1,000 chip is handy. SIP date dropdown, OK."

**M29 Review your SIP:** "'Charges ₹0'? Stamp duty is 0.005%, Groww shows it. And the expense ratio? This looks either wrong or like it's hiding something. That's the first thing that made me doubt this app."

**M30 Set up autopay:** "Up to ₹15,000 limit, UPI Autopay, ₹0. Clear. My SIP is 5k so 15k is fine. Approve."

**M31 SIP scheduled:** "'Scheduled', not 'invested'. Honest, I like that. First instalment after verification."

**Overall:** "Fastest onboarding I've seen until M07b. Fix the charges line and the pre-ticked box, and show me fund data or don't show a list at all."

---

## Imran, 36 (raw)

**M01 Mobile number:** "Bank mein purana number hai, ye dukaan wala naya hai. 'Linked to your bank account' likha hai… to kaunsa daalun? Bank wala band ho gaya." *(Unclear what happens if the numbers differ.)*

**M02 Verify mobile:** "'Credit bureau se details fetch'? CIBIL? Mera loan application chal raha hai, score kharab ho jaayega?" *(Taps 'personal details'.)*

**M02d What we fetch:** "'Not used for credit checks or your credit score.' Achha, theek hai. Tick kar diya." *(Too late: the OTP already submitted itself while he was reading the sheet.)*

**M03 Set MPIN:** "Ek aur PIN. Dukaan ke liye 5 PIN yaad hain already. Chalo, 1234." *(The design rejects easy MPINs only in the annotation; no error screen exists.)*

**M04 → M04b → M05:** "Gmail nahi hai, 'Use another email' pe Rediffmail daala, OTP aaya, khud verify ho gaya. Theek."

**M07b Enter PAN & DOB:** "PAN aur DOB daala. Calendar se date choose karna aasaan tha."

**M10 DigiLocker:** "DigiLocker? Aadhaar wala mobile number bhi purana hai… OTP kahan aayega?" *(The placeholder can't answer this. The real flow needs a "my Aadhaar mobile has changed" path.)*

**M20 Confirm bank account:** "Ye mera aur biwi ka joint account hai. 'Yes, use this account' dabaya." *(No single-holder question, so he only finds out at M23e: DR-05.)*

**M23e This account can't be linked:** "Pehle bata dete! Ab dusra account? Mera current account hai dukaan ka, wo chalega?" *(The screen doesn't say whether a current account works.)*

**M20b Verify bank with UPI:** "Paytm se ₹1 bhej diya, Paytm mein account choose kiya. Ye theek tha."

**M13 Personal details:** "Address Aadhaar wala gaon ka hai. 'Different address for communication' on kiya."

**M11b → M11c → M11d:** "Bijli ka bill upload kiya… par bill abbu ke naam pe hai. 'Your name must be visible.' To ab kya karun? Rent agreement nahi hai." *(Proof-type help doesn't cover a document in a family member's name.)*

**M14 A few more details:** "Occupation: Business ya Self-employed? Dukaan hai… dono lagte hain." *(Picks Business.)* "Income har saal alag hoti hai, andaza laga diya." *(Declaration)* "'Not a politically exposed person'… mera bhai ward parshad hai. Kya ye politically exposed hai? Tick karun ya nahi? Koi option hi nahi aur kuch." *(Dead end or a false tick: DR-03.)*

**M17b Add nominee · minor:** "Beta 10 saal ka hai, guardian biwi. Samajh aa gaya."

**M18b Shares don't add up:** "60 aur 30 likha galti se. 'Divide equally', ek tap mein 50-50. Bahut badiya."

**M27 Make your account investment-ready:** "Autopay ₹15,000 tak… kabhi account mein paisa kam ho to? Bank bounce charge lagata hai ₹500. Ye kahin likha nahi." *(Mandate bounce charges from the bank aren't mentioned anywhere.)*

**M28 Start a SIP:** "Income fix nahi hai. Har mahine same date? Agar kisi mahine nahi daal paaya to? 'Pause anytime' likha hai, achha."

**Overall:** "Shuru mein dar laga (credit bureau, joint account). Nominee wala part sabse aasaan. Address proof aur PEP wali baat pe atak gaya."

---

## What the three agree on

| # | Issue | Who hit it | Screens | Worth reviewing | Ties to |
|---|---|---|---|---|---|
| 1 | Bureau consent is missed because the OTP auto-submits; prefill is lost | Ramesh, Sneha, Imran | M02, M02d, M07b | yes (in review) | DR-04, Q17 |
| 2 | "₹0 charges" on the SIP review is believed (Ramesh) or distrusted (Sneha) | Ramesh, Sneha | M29 | yes (in review) | DR-01 |
| 3 | Pre-ticked declaration: skipped by one, distrusted by another, a dead end for the third | Ramesh, Sneha, Imran | M14 | yes (in review) | DR-02, DR-03, Q12 |
| 4 | The ₹15,000 autopay limit still reads as money leaving the account; bounce charges are never mentioned | Ramesh, Imran | M27, M30 | yes | new; question in review |
| 5 | MPIN is confused with UPI PIN; no biometric option; easy PINs not visibly blocked | Ramesh, Sneha, Imran | M03, M03b | yes | needs research |
| 6 | Joint account is confirmed, then rejected later | Imran | M20, M23e | yes (in review) | DR-05 |
| 7 | Fund list gives no basis to choose (no returns, expense ratio or size), and search has no results state | Sneha | M27 | yes | Q11, missing states |
| 8 | Address proof in a family member's name has no path | Imran | M11c | yes | new |
| 9 | Bank and Aadhaar mobile numbers differ from the one entered | Imran | M01, M10 | yes | new; DigiLocker design |
| 10 | Nominee switch off doesn't say "you can add later" | Sneha | M14 | maybe | new |

## What worked
- **Bank found from the mobile number (M20):** the one moment every persona liked ("khud aa gaya").
- **Real UPI logos (M20b), "Divide equally" (M18b), the calendar on DOB:** quick, obvious, no reading needed.
- **"Scheduled", not "invested" (M31), and "Skip for now" (M30):** felt honest to the sceptical user.

## Worth testing with real users first
1. M03: do first-time users type their UPI PIN as the MPIN? (5 users, think-aloud)
2. M27/M30: after reading the autopay card, what do people think happens to ₹15,000? (first-click plus one question)
3. M02: how many tick the bureau consent before the OTP auto-submits? (prototype with SMS autofill)
