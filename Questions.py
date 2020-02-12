import json

questions_string = '''

{
    "questions":
    [
        {
            "category" : "True/False",
            "ask_question" : "Insert a true or false question",
            "answers" :
            {
                "answer1" : true,
                "answer2" : false
            }
        },
        
        {
            "category" : "Multiple Choice",
            "ask_question" : "Insert a multiple choice question",
            "answers": 
            {
                "answer1" : "A",
                "answer2" : "B",
                "answer3" : "C",
                "answer4" : "D"
            }
        },
        
        {
            "category" : "Matching",
            "ask_question" : "Insert matching question",
            "answers" : 
            
            {
                "answer1" : "Insert matching description",
                "answer2" : "Insert matching description",
                "answer3" : "Insert matching description",
                "answer4" : "Insert matching description"
            }
        }
    ]
}

'''

data = json.loads(questions_string)
'''The .loads() method converts a JSON string to a Python dictionary'''

#print(data)
'''Output is a Python dictionary'''

#print(type(data))
'''Confirms that data is a dict object'''

#for question in data['questions']:
#    print(question['category'])
'''Output is all the categories'''

new_data = json.dumps(data, indent=3)
'''The .dumps() method converts a Python object into a JSON string'''


with open('data.txt', 'w', encoding='utf-8') as file:
    json.dump(data, file)

