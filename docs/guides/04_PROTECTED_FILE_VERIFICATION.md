# Protected-file verification

The redesign was implemented only under `web_v2/`, with the friend's repository cloned under `external_reference/` for inspection. `git diff --name-only` reported no tracked modifications to the protected backend, configuration, model-service, feature-extraction, polarization-service, or manuscript paths checked at completion.

Current SHA-256 fingerprints recorded on 2026-10-04:

| Protected file | SHA-256 | Bytes |
|---|---|---:|
| `app.py` | `324C2232CE8C9225F6167E3AF78AC27825737FF2E8C07EED5889A8F6F6DC3E7B` | 11690 |
| `model_service.py` | `F749FFD0E79A951F42555F5083D2056567DE9CCAAF721772601EA0A79856C877` | 9458 |
| `feature_extractor.py` | `45A9AE59E9822528C1E6D64AC107A121BB7291D7C352BF744E6FC9D06F0569CB` | 10044 |
| `polarization_service.py` | `9F93886080C9D6378C670D6365C17A12FE4DDDAECAE145EEFED34A6718C5D738` | 22610 |
| `config/observation_metadata.json` | `09CC397B98F2FA153E791AC03CE955309F7BA7F9785E5D574520C4DAB207F038` | 2210 |
| `model/polix_v2_matrixC_unsupervised_xai_model.pkl` | `D8EFD73C9744ED1CA1098A4599DA91ACDEDC250BB2B6639728364AEF6B8C180D` | 280244 |
| `research_paper_ieee/06_IEEE_Conference_Manuscript_Draft.md` | `6E110EF5FE6570ABB138337BEC53C12D8A89A02C048B2582AE6D9613D90F5305` | 33947 |
| `research_paper_ieee/07_IEEE_Conference_Manuscript.tex` | `C849C8340CE41A08767579BDC0C565F9FB7693C2FBC17023D46C6E1714F5511A` | 23623 |

These hashes document the files as found at completion. The implementation did not rewrite or resave them.

