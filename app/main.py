from pr_context import load_pr_context
from config_loader import load_config
from llm_reviewer import review_code
from comment_parser import parse_comments
from github_poster import post_comments

from pr_context import get_pr_context


def main():
    ctx = get_pr_context()

    print("PR NUMBER:", ctx["pr_number"])
    print("PR TITLE:", ctx["title"])
    print("DIFF PREVIEW:")
    print(ctx["diff"][:1000])


if __name__ == "__main__":
    main()
