import unirest


def make_request(first_name, second_name):
    response = unirest.get("https://love-calculator.p.mashape.com/getPercentage?fname=" + first_name + "&sname" + second_name,
                           headers = {
                               "X-Mashape-Key": "mTBkJoLCO4mshZZhnangnsLl3INMp1hakYZjsnmZI9OiopwjvJ",
                               "Accept": "application/json"
                           }
                           )
    return response


make_request("Connor Valenti", "Tim Buesking")
