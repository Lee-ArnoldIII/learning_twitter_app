# from user import User
# from database import Database
# from twitter_utils import get_request_token, get_oauth_verifier, get_access_token


# Database.initialise(database='learning', user='postgres', password='Outsmart1!@', host='localhost')

# user_email = input("Please enter your e-mail address: ")

# # user = User.load_from_db_by_email(user_email)

# if not user:
#     request_token = get_request_token()

#     oauth_verifier = get_oauth_verifier(request_token)

#     acces_token = get_access_token(request_token, oauth_verifier)

#     first_name = input("Please enter your first name: ")
#     last_name = input("Please enter your last name: ")

#     # user = User(user_email, first_name, last_name, acces_token['oauth_token'], acces_token['oauth_token_secret'], None)
#     # user.save_to_db()


# tweets = user.twitter_request('https://api.twitter.com/1.1/search/tweets.json?q=computers+filters:images')

# for tweet in tweets['statuses']:
#     print(tweet['text'])

    
