import instaloader
from langdetect import detect

# Initialize Instaloader
L = instaloader.Instaloader()

# Load a profile by username
profile = instaloader.Profile.from_username(L.context, "bdgfolk")

# List of expected languages for the user (can be obtained from their profile bio, etc.)
expected_languages = ["id"]

# Function to check if Xenoglossophilia is suspected
def is_xenoglossia(text, expected_languages):
    try:
        detected_language = detect(text)
        if detected_language not in expected_languages:
            return True
        return False
    except Exception as e:
        print(f"Error detecting language: {e}")
        return False

# Analyze each post's caption
for post in profile.get_posts():
    caption = post.caption
    if caption and is_xenoglossia(caption, expected_languages):
        print(f"Xenoglossophilia detected in post: {post.url}")
