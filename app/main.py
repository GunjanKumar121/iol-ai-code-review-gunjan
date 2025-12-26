from pr_context import load_pr_context
from config_loader import load_config
from llm_reviewer import review_code
from github_poster import post_comments

def main():
    pr_context = load_pr_context()
    config = load_config()

    review_results = review_code(
        diff=pr_context["diff"],
        config=config
    )

    post_comments(
        comments=review_results,
        pr_context=pr_context
    )

if __name__ == "__main__":
    main()
