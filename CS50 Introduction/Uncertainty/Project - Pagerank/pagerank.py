import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    # Get the list of pages in the corpus
    pages = list(corpus.keys())
    
    # Initialize the probability distribution
    prob_distribution = dict.fromkeys(pages, 0)
    
    # Get the links on the current page
    links = corpus[page]
    
    if links:
        # Calculate the probabilities for linked pages
        for linked_page in links:
            prob_distribution[linked_page] += damping_factor / len(links)
    
    # Add the probability for choosing any page at random
    for p in pages:
        prob_distribution[p] += (1 - damping_factor) / len(pages)
    
    return prob_distribution
    raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    # Initialize counts of visits to each page
    page_counts = dict.fromkeys(corpus.keys(), 0)
    
    # Choose a random starting page
    current_page = random.choice(list(corpus.keys()))
    
    for _ in range(n):
        # Update the count for the current page
        page_counts[current_page] += 1
        
        # Get the transition model for the current page
        prob_distribution = transition_model(corpus, current_page, damping_factor)
        
        # Choose the next page based on the probability distribution
        next_page = random.choices(list(prob_distribution.keys()), weights=prob_distribution.values(), k=1)[0]
        current_page = next_page
    
    # Convert counts to probabilities
    pagerank = {page: count / n for page, count in page_counts.items()}
    
    return pagerank
    raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    # Initialize PageRank values to 1 / N
    N = len(corpus)
    pagerank = dict.fromkeys(corpus.keys(), 1 / N)
    
    converged = False
    threshold = 0.001  # Convergence threshold
    
    while not converged:
        new_pagerank = {}
        for page in corpus:
            # Calculate the new PageRank for the current page
            new_rank = (1 - damping_factor) / N
            for possible_linker in corpus:
                if page in corpus[possible_linker]:
                    new_rank += damping_factor * pagerank[possible_linker] / len(corpus[possible_linker])
                if not corpus[possible_linker]:  # Handle pages with no outbound links
                    new_rank += damping_factor * pagerank[possible_linker] / N
            new_pagerank[page] = new_rank
        
        # Check if the new PageRank values have converged
        converged = all(abs(new_pagerank[page] - pagerank[page]) < threshold for page in pagerank)
        
        # Update the PageRank values for the next iteration
        pagerank = new_pagerank
    
    return pagerank
    raise NotImplementedError


if __name__ == "__main__":
    main()
