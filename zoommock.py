from flask import Flask, jsonify, request, send_file, abort
from credentials import token


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/meetings/123456/registrants', methods=['GET'])
def registrants():
    if request.headers['Authorization'] != 'Bearer ' + token:
        abort(403)
    print(request.headers['Authorization'])
    return """{
                  "next_page_token": "w7587w4eiyfsudgf",
                  "page_count": 1,
                  "page_size": 30,
                  "total_records": 20,
                  "registrants": [
                    {
                      "id": "9tboDiHUQAeOnbmudzWa5g",
                      "address": "1800 Amphibious Blvd.",
                      "city": "Mountain View",
                      "comments": "Looking forward to the discussion.",
                      "country": "US",
                      "custom_questions": [
                        {
                          "title": "What do you hope to learn from this?",
                          "value": "Look forward to learning how you come up with new recipes and what other services you offer."
                        }
                      ],
                      "email": "jchill@example.com",
                      "first_name": "Jill",
                      "industry": "Food",
                      "job_title": "Chef",
                      "last_name": "Chill",
                      "no_of_employees": "1-20",
                      "org": "Cooking Org",
                      "phone": "5550100",
                      "purchasing_time_frame": "1-3 months",
                      "role_in_purchase_process": "Influencer",
                      "state": "CA",
                      "status": "approved",
                      "zip": "94045",
                      "create_time": "2022-03-22T05:59:09Z",
                      "join_url": "https://example.com/j/11111"
                    }, 
                    {
                      "id": "9tboDiHUQAeOnbmudzWa5g",
                      "address": "1800 Amphibious Blvd.",
                      "city": "Mountain View",
                      "comments": "Looking forward to the discussion.",
                      "country": "US",
                      "custom_questions": [
                        {
                          "title": "What do you hope to learn from this?",
                          "value": "Look forward to learning how you come up with new recipes and what other services you offer."
                        }
                      ],
                      "email": "jchill@example.com",
                      "first_name": "Jill",
                      "industry": "Food",
                      "job_title": "Chef",
                      "last_name": "Chill",
                      "no_of_employees": "1-20",
                      "org": "Cooking Org",
                      "phone": "5550100",
                      "purchasing_time_frame": "1-3 months",
                      "role_in_purchase_process": "Influencer",
                      "state": "CA",
                      "status": "approved",
                      "zip": "94045",
                      "create_time": "2022-03-22T05:59:09Z",
                      "join_url": "https://example.com/j/11111"
                    },
                    {
                      "id": "9tboDiHUQAeOnbmudzWa5g",
                      "address": "1800 Amphibious Blvd.",
                      "city": "Mountain View",
                      "comments": "Looking forward to the discussion.",
                      "country": "US",
                      "custom_questions": [
                        {
                          "title": "What do you hope to learn from this?",
                          "value": "Look forward to learning how you come up with new recipes and what other services you offer."
                        }
                      ],
                      "email": "jchill@example.com",
                      "first_name": "Jill",
                      "industry": "Food",
                      "job_title": "Chef",
                      "last_name": "Chill",
                      "no_of_employees": "1-20",
                      "org": "Cooking Org",
                      "phone": "5550100",
                      "purchasing_time_frame": "1-3 months",
                      "role_in_purchase_process": "Influencer",
                      "state": "CA",
                      "status": "approved",
                      "zip": "94045",
                      "create_time": "2022-03-22T05:59:09Z",
                      "join_url": "https://example.com/j/11111"
                    }
                    
                  ]
                }"""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(port=8080)
