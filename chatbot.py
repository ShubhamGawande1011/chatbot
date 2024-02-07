import random

class InterviewBot:
    def __init__(self):
        self.questions = [
            "Can you tell me about yourself?",
            "What interests you about this position?",
            "What relevant experience do you have?",
            "How do you handle challenges or conflicts in the workplace?",
            "Where do you see yourself in 5 years?",
            "Do you have any questions for us?"
        ]

    def start_interview(self):
        print("HR: Welcome to the interview! Let's begin.")
        for question in self.questions:
            print(f"HR: {question}")
            answer = input("Student: ")
            print(f"HR: Thank you for your response.")
        print("HR: That concludes our interview. Thank you for your time!")

if __name__ == "__main__":
    bot = InterviewBot()
    bot.start_interview()
