# drug_ingred

A simple utility to find the first ingredient of a drug. Uses the RxNav SOAP API:

http://rxnav.nlm.nih.gov/RxNormAPISOAP.html

## Usage

```python
import drug_ingred

drug_ingred("Vioxx")
# result: "rofecoxib"
```

## Dependencies

- Python 2.7
- suds, <https://fedorahosted.org/suds/>


