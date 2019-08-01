from apiclient import discovery
import spacy

API_KEY = "AIzaSyD91Ya6ssiNzbcReKdXpxQYSNGVCuIYAy0"
VERSION = "v1alpha1"
API = "factchecktools"
FACTCHECK = discovery.build(API, VERSION, developerKey=API_KEY)


nlp = spacy.load("en_core_web_sm")

# TODO: the word embedding of a full sentence is simply the average over all different words...
# ... consider modify the vectors by a length difference penalty?...
# ... or alternatively, try to compare shorter pieces of the sentence and compute pairwise similarities?


def is_claim_a_quote(claim: str, quote: str, similarity_threshold: float) -> bool:
    """Takes a claim and a quote and determines if the claim is equivalent to the quote.
    """
    parsed_claim = nlp(claim)
    parsed_quote = nlp(quote)

    # remove stop words
    parsed_claim_no_stop_words = nlp(
        " ".join([str(t) for t in parsed_claim if not t.is_stop])
    )
    parsed_quote_no_stop_words = nlp(
        " ".join([str(t) for t in parsed_quote if not t.is_stop])
    )

    return (
        parsed_claim_no_stop_words.similarity(parsed_quote_no_stop_words)
        >= similarity_threshold
    )


def fact_check_claim(claim: str, FACTCHECK: discovery) -> str:
    """Takes a claim and fact checks it.
    """
    # get factcheck items
    items = FACTCHECK.claims().search(query=claim).execute()

    # check similarity of claim to factcheck quotes (first quote only)
    # TODO: check all quotes,  not just first, and determined how to handle
    quotes = [claim["text"] for claim in items["claims"]]
    is_quote = is_claim_a_quote(claim, quotes[0], similarity_threshold=0.70)

    # # TODO: introduce factcheck source preferences, for example:
    # factcheck_preferences = {1: "factcheck.org", 2: "politifact.com"}

    if is_quote:
        claim_reviews = [claim["claimReview"][0] for claim in items["claims"]]
        return claim_reviews[0]
    else:
        return "Claim not found in quoted fact checks"
