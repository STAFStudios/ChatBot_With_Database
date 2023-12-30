import json 
from difflib import get_close_matches

def load_learning_data(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent= 2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answers_for_question(question: str, learning_data: dict) -> str | None:
    for q in learning_data["questions"]:
        if q["question"] == question:
            return q["answer"]

def chat_bot():
    learning_data: dict = load_learning_data('F:\Html Programme\MachineLearning\Learning\learning_data.json')

    while True:
        user_input: str = input('You: ')

        if user_input.lower() == 'quit':
            break
            
        best_match: str | None = find_best_match(user_input, [q["question"] for q in learning_data["questions"]])

        if best_match:
            answer: str = get_answers_for_question(best_match, learning_data)
            print(f'Bot: {answer}')
        else:
            print('Bot: I don\'t know what you are saying. Can you teach me?')
            new_answer: str = input('Give a solution or say "skip" to ignore: ')

            if new_answer.lower() != 'skip':
                learning_data["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base('F:\Html Programme\MachineLearning\Learning\learning_data.json', learning_data)
                print('Bot: Thank you!')

if __name__ == '__main__':
      chat_bot()
