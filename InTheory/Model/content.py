from mongoengine import Document, DictField, EmbeddedDocument, FloatField, EmbeddedDocumentField, StringField, ListField, IntField, BooleanField, ReferenceField, DateTimeField
from datetime import datetime
# ============================ User ================================ #

# Question is-a Document (imported class from Mongoengine)
#Question has-a meta, question, answer, sid, extract, image, question_number

class Question(Document):
    meta = {"collection":"Questions"}
    question = StringField(required=True)
    options = ListField(StringField(), default=list, required=True)
    answer = ListField(StringField(), required=True)
    sid = StringField(required=True, default="")
    extract = StringField(required=True, default="")
    image = StringField(required=False)
    question_number = StringField(required=True)

# MiniQuizQuestion is-a Document
#MiniQuQuiz has-a meta, question, options, and answer
    
class MiniQuizQuestion(Document):
    meta = {"collection":"MiniQuizQuestions"}
    question = StringField(required=True)
    options = ListField(StringField(), default=list, required=True)
    answer = ListField(IntField(), required=True)

# Nugget is-a EmbeddedDocument (mongo)
#Nugget has-a section subtitle, title, img, content
    
class Nugget(EmbeddedDocument):
    section_sub_title = StringField(required=True)
    title = StringField(required=True)
    img = StringField(required=True)
    content = StringField(required=True)

# Section is-a Document
# has-a meta, title, nuggets, questions

class Section(Document):
    meta = {"collection":"Sections"}
    title = StringField(required=True)
    nuggets = ListField(EmbeddedDocumentField(Nugget), default=list)
    questions = ListField(ReferenceField(Question), required=False, default=list)

# Testanswer is-a EmbeddedDoc
# Has-a qid, selected answers

class TestAnswer(EmbeddedDocument):
    qid = StringField(required=True, default="")
    selected_answers = ListField(IntField(), default=list)

# Test  is-a Doc
# has-a meta, user, questions, answers, score
# has a function(s) that calculate the score( takes self parameter), save answers (self, answer parameters), update cursor

class Test(Document):
    meta = {"collection":"Tests", 'allow_inheritance': True}
    user = StringField(required=True)
    questions = ListField(ReferenceField(Question), required=True, default=list)
    answers = ListField(EmbeddedDocumentField(TestAnswer), default=list)
    score = IntField(required=True, default=0)
    cursor = IntField(required=True, default=0) #Indicates which question is currently viewed
    is_completed = BooleanField(required=True, default=False)

    def calculate_score(self):
        '''
        Calculates the test score based on user's answers
        '''
        #Put all correct answers in a list
        correct_answers = []
        for question in self.questions:
            correct_answers.append([int(answer) for answer in question.answer])                

        #Put all user's answers in a list
        user_answers = []
        for user_answer in self.answers:
            user_answers.append([int(answer) for answer in user_answer.selected_answers])

        #Check if user answered correctly by looking at the intersection of correct answers and user answers
        for i, correct_answer in enumerate(correct_answers):     
            try:              
                user_answer = user_answers[i]
            except IndexError:
                #This means that an answer for this question was not provided (timer ended)
                user_answer = [] #just allocate no answer to this question

            inter = set(user_answer).intersection(correct_answer)
            if len(inter) == len(correct_answer): 
                self.score += 1
        self.is_completed = True
        self.save()

    def save_answers(self, answers):
        '''
        Saves user's answers for a question at position cursor
        '''
        ta = TestAnswer()
        ta.qid = str(self.questions[self.cursor].id)
        ta.selected_answers = answers 
        try:
            self.answers[self.cursor] = ta
        except IndexError:
            self.answers.append(ta)
        self.save()

    def update_cursor(self, value):
        # if self.cursor + value >= len(self.questions) :
        #     #Do not overflow 
        #     return
        self.cursor += value
        self.save()

# MockTest is-a Test (inheritance). Has-a fuction that takes self and cursor parameters

class MockTest(Test):
    pass
    #In the future this test will have some different features than the Practise test

class PractiseTest(Test):
    
    def evaluate_question(self, cursor):
        '''
        Evaluates the question at cursor position
        '''
        try:
            #Put correct answers in a list
            correct_answers =[int(answer) for answer in self.questions[cursor].answer]

            #Put user's answers in a list
            user_answers = [int(answer) for answer in self.answers[cursor].selected_answers]

            #Check if user answered correctly by looking at the intersection of correct answers and user answers
            inter = set(user_answers).intersection(correct_answers)
            if len(inter) == len(correct_answers): 
                return 1
            else:
                return 0
        except Exception, e:
            print e


class HazardPoint(EmbeddedDocument):
    start = IntField(required=True) #When the hazard occurs initially
    end = IntField(required=True)

class HazardPerceptionClip(Document):
    meta = {"collection":"HazardPerceptionClips"}
    base_dir = StringField(required=True)
    clip_name = StringField(required=True)
    hazards = ListField(EmbeddedDocumentField(HazardPoint), required=True)
    solution_clip_name = StringField(required=True)

class HazardPerceptionTest(Document):
    meta = {"collection":"HazardPerceptionTests"}
    uid = StringField(required=True)
    cid = StringField(required=True)
    score = IntField(required=True, default=0)

class FeedbackItem(Document):
    meta = {"collection":"FeedbackItems"}
    description = StringField(required=True)
    uid = StringField(required=True)
    timestamp = DateTimeField(required=True, default=datetime.now())