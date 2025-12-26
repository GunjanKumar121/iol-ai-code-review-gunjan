from pr_context import load_pr_context
from config_loader import load_config
from llm_reviewer import review_code
from comment_parser import parse_comments
from github_poster import post_comments

def main():
    pr_context = load_pr_context()
    config = load_config()
    llm_output = review_code(diff="", config=config)
    comments = parse_comments(llm_output)
    post_comments(comments, pr_context)

if __name__ == "__main__":
    main()
