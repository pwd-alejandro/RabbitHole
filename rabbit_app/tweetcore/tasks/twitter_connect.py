import tweepy as tp


def api_connect(configuration: dict = None) -> tp.auth.OAuthHandler:
    auth = tp.OAuthHandler(consumer_key=configuration["consumer_key"],
                           consumer_secret=configuration["consumer_secret"])

    auth.set_access_token(key=configuration["access_token"],
                          secret=configuration["access_secret"])

    return auth


def get_client(configuration: dict = None) -> tp.API:
    auth = api_connect(configuration=configuration)

    client = tp.API(auth_handler=auth,
                    wait_on_rate_limit=True)

    return client