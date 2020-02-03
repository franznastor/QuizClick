import json

questions_string = '''

{
    "Questions":
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