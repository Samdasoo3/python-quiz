import json
import os

class Quiz:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def to_dict(self):
        return {"question": self.question, "options": self.options, "answer": self.answer}

class QuizGame:
    def __init__(self, quiz_file='questions.json', state_file='state.json'):
        self.quiz_file = quiz_file
        self.state_file = state_file
        self.questions = self.load_questions()
        self.high_score = self.load_high_score() # 최고 점수 불러오기

    def load_questions(self):
        if os.path.exists(self.quiz_file):
            with open(self.quiz_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Quiz(q['question'], q['options'], q['answer']) for q in data]
        return []

    def load_high_score(self):
        """state.json에서 최고 점수 읽기"""
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get("high_score", 0)
        return 0

    def save_high_score(self, score):
        """최고 점수 업데이트 및 저장"""
        if score > self.high_score:
            self.high_score = score
            with open(self.state_file, 'w', encoding='utf-8') as f:
                json.dump({"high_score": self.high_score}, f)
            print(f"🎊 새로운 최고 기록 달성: {self.high_score}점!")

    def play(self):
        if not self.questions:
            print("\n❌ 등록된 문제가 없습니다.")
            return
        
        score = 0
        for i, q in enumerate(self.questions):
            print(f"\n문제 {i+1}. {q.question}")
            for opt in q.options: print(opt)
            try:
                user_ans = int(input("정답 번호: "))
                if user_ans == q.answer:
                    print("✅ 정답!"); score += 1
                else:
                    print(f"❌ 오답! 정답은 {q.answer}번")
            except ValueError:
                print("❌ 숫자만 입력 가능합니다.")
        
        print(f"\n🎮 이번 게임 점수: {score}/{len(self.questions)}")
        self.save_high_score(score) # 게임 종료 후 점수 저장 체크

    # ... (add_quiz, list_quizzes, delete_quiz 함수는 이전과 동일) ...
    def add_quiz(self):
        print("\n➕ 새 문제 추가")
        q_text = input("문제 내용: ")
        opts = [f"{i}. {input(f'{i}번 보기: ')}" for i in range(1, 5)]
        try:
            ans = int(input("정답 번호(1-4): "))
            self.questions.append(Quiz(q_text, opts, ans))
            with open(self.quiz_file, 'w', encoding='utf-8') as f:
                json.dump([q.to_dict() for q in self.questions], f, ensure_ascii=False, indent=4)
            print("✅ 저장 완료!")
        except ValueError: print("❌ 입력 오류!")

    def list_quizzes(self):
        print("\n📋 문제 목록")
        for i, q in enumerate(self.questions):
            print(f"{i+1}. {q.question} (정답: {q.answer})")

    def delete_quiz(self):
        self.list_quizzes()
        try:
            idx = int(input("\n🗑️ 삭제할 번호 (취소: 0): "))
            if 0 < idx <= len(self.questions):
                self.questions.pop(idx - 1)
                with open(self.quiz_file, 'w', encoding='utf-8') as f:
                    json.dump([q.to_dict() for q in self.questions], f, ensure_ascii=False, indent=4)
                print("✅ 삭제되었습니다.")
        except ValueError: print("❌ 숫자 입력!")

def main():
    game = QuizGame()
    while True:
        print(f"\n🏆 현재 최고 점수: {game.high_score}") # 상단에 최고 점수 표시
        print("1. 🚀 퀴즈 시작하기 2. 문제 추가 3. 목록 보기 4. 문제 삭제 5. 종료")
        choice = input("선택: ")
        if choice == '1': game.play()
        elif choice == '2': game.add_quiz()
        elif choice == '3': game.list_quizzes()
        elif choice == '4': game.delete_quiz()
        elif choice == '5': break
        else: print("❌ 잘못된 입력")

if __name__ == "__main__":
    main()