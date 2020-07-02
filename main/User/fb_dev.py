import json
import facebook

def main():
    token = "EAAEOY8AlsIgBACvCb4jfoBBQWSYmfTvOa4YFJjs3qgy3JZC0GcheuiYtQXfZBH2YvDDgddYkY1nCSqTTh7iFle2DYB3tPPyvxl9bKhS5RedcQAeFsH54q5DwsgfFJJBflauhyKuEeZAQtfGCdGO38FkhzuQ6yAOjnb7apo2dBmvt0IZAtm8EeNXd6sXffaAZAR9AdntVZCZCwZDZD"
    graph = facebook.GraphAPI(token)
    fields = ['email' , 'name' , 'picture']
    fields = ','.join(fields)
    profile = graph.get_object('me' , fields =fields)

    print(json.dumps(profile , indent=4))


