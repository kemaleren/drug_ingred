from suds.client import Client

_url = "http://rxnav.nlm.nih.gov/RxNormDBService.xml"
_rxnav = Client(_url)


def _approx_cui(drug):
    """Returns the CUI of first approximate match in RxNav"""
    result = _rxnav.service.getApproximateMatch(drug, 1, 0)
    if len(result.rxMatchInfo) == 0:
        return -1
    r = result.rxMatchInfo[0]
    return r.RXCUI


def _cui_to_ingredient(cui):
    """Returns the first ingredient for this CUI"""
    result = _rxnav.service.getRelatedByType(cui, ["IN"])
    if len(result) == 0:
        return -1, "UNKNOWN"
    r = result[0].rxConcept
    if len(r) == 0:
        return -1, "UNKNOWN"
    r = r[0]
    return r.RXCUI, r.STR


def drug_ingred(drug):
    """Returns the first ingredient of given drug.

    Uses RxNav SOAP API to do approximate match, then find first
    ingredient.

    Returns "UNKNOWN" if the approximate match fails.

    >>> drug_ingred("Vioxx")
    "rofecoxib"

    """
    cui = _approx_cui(drug)
    if cui == -1:
        return "UNKNOWN"
    ingred_cui, ingred = _cui_to_ingredient(cui)
    return ingred
