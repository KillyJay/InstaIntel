import instaloader
from instaloader import Profile, Post

#Define and print banner
ascii_art = """  _____           _         _____       _       _ 
  \_   \_ __  ___| |_ __ _  \_   \_ __ | |_ ___| |
   / /\/ '_ \/ __| __/ _` |  / /\/ '_ \| __/ _ \ |
/\/ /_ | | | \__ \ || (_| /\/ /_ | | | | ||  __/ |
\____/ |_| |_|___/\__\__,_\____/ |_| |_|\__\___|_|
        
        Created By Killy Jay \n"""

print(ascii_art)

# Define the Instagram ID of the profile you want to scrape data from 
profile_id = input("Enter Instagram Username: ")

# Create an instance of the Instaloader class
loader = instaloader.Instaloader()

# Load the profile using its ID
profile = Profile.from_username(loader.context, profile_id)

# Get the profile's username, full name, and number of followers
username = profile.username
full_name = profile.full_name
followers = profile.followers
bio = profile.biography
following = profile.followees

# Print the profile's information
print("Username:", username)
print("Full name:", full_name)
print("Followers:", followers)
print("Following:", following)
print("Bio:", bio)

get_posts = input("Would you like to get the posts on this profile? (Y/n): ")

if get_posts.lower() == "y":
# Get the profile's posts
        posts = profile.get_posts()

# Iterate over the posts and print their captions and URLs
        for post in posts:
                date = post.date
                caption = post.caption
                url = post.url
                print("Caption:", caption)
                print("URL:", url)
                print("Date posted:", date)

elif get_posts.lower() == "n":
        exit()



