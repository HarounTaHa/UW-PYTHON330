import requests

base_url = 'https://api.stackexchange.com/'


def stackoverflow_fetch_latest_question_based_on_tage(tage):
    response = requests.get(base_url + f'/2.3/questions?order=desc&sort=activity&tagged={tage}&site=stackoverflow')
    question = response.json()['items'][0]
    title = question['title']
    user_id = question['owner']['user_id']
    display_name = question['owner']['display_name']
    response = requests.get(base_url + f'/2.3/users/{user_id}?order=desc&sort=reputation&site=stackoverflow')
    creation_date = response.json()['items'][0]['creation_date']
    return f"{display_name} created on {creation_date} asked \"{title}\""


if __name__ == '__main__':
    result = stackoverflow_fetch_latest_question_based_on_tage(tage='django')
    print(result)
