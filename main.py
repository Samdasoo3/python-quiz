import json
import os

# 1. 개별 퀴즈 정보를 담는 클래스
class Quiz:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def to_dict(self):
        """JSON 저장을 위해 딕셔너리로 변환"""
        return {
            "question": self.question,
            "options": self.options,
            "answer": self.answer
        }

# 2. 게임의 전체 로직을 관리하는 클래스
class QuizGame:
    def __init__(self, filename='questions.json'):
        self.filename = filename
        self.questions = self.load_questions()

    def load_questions(self):
        """파일에서 데이터를 읽어 Quiz 객체 리스트로 변환"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # 딕셔너리 리스트를 Quiz 객체 리스트로 변환
                return [Quiz(q['question'], q['options'], q['answer']) for q in data]
        return []

    def save_questions(self):
        """Quiz 객체들을 딕셔너리로 변환하여 파일에 저장"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            data = [q.to_dict() for q in self.questions]
            json.dump(data, f, ensure_ascii=False, indent=4)

    def play(self):
        """퀴즈 풀기 기능"""
        if not self.questions:
            print("\n❌ 등록된 문제가 없습니다.")
            return
        
        score = 0
        for i, q in enumerate(self.questions):
            print(f"\n문제 {i+1}. {q.question}")
            for opt in q.options:
                print(opt)
            
            try:
                user_ans = int(input("정답 번호: "))
                if user_ans == q.answer:
                    print("✅ 정답!")
                    score += 1
                else:
                    print(f"❌ 오답! 정답은 {q.answer}번")
            except ValueError:
                print("❌ 숫자만 입력 가능합니다.")
        
        print(f"\n🎊 종료! 최종 점수: {score}/{len(self.questions)}")

    def add_quiz(self):
        """퀴즈 추가 기능"""
        print("\n➕ 새 문제 추가")
        q_text = input("문제 내용: ")
        opts = [f"{i}. {input(f'{i}번 보기: ')}" for i in range(1, 5)]
        try:
            ans = int(input("정답 번호(1-4): "))
            self.questions.append(Quiz(q_text, opts, ans))
            self.save_questions()
            print("✅ 저장 완료!")
        except ValueError:
            print("❌ 숫자 입력 오류로 실패!")

    def list_quizzes(self):
        """퀴즈 목록 보기"""
        print("\n📋 문제 목록")
        for i, q in enumerate(self.questions):
            print(f"{i+1}. {q.question} (정답: {q.answer})")

    def delete_quiz(self):
        """퀴즈 삭제 기능"""
        self.list_quizzes()
        try:
            idx = int(input("\n🗑️ 삭제할 번호 (취소: 0): "))
            if 0 < idx <= len(self.questions):
                self.questions.pop(idx - 1)
                self.save_questions()
                print("✅ 삭제되었습니다.")
        except ValueError:
            print("❌ 숫자만 입력 가능합니다.")

# 3. 메인 실행부
def main():
    game = QuizGame() # 게임 객체 생성
    
    while True:
        print("\n" + "="*25)
        print("🎮 클래스 기반 퀴즈 게임")
        print("="*25)
        print("1. 퀴즈 풀기\n2. 문제 추가\n3. 목록 보기\n4. 문제 삭제\n5. 종료")
        
        choice = input("선택: ")
        if choice == '1': game.play()
        elif choice == '2': game.add_quiz()
        elif choice == '3': game.list_quizzes()
        elif choice == '4': game.delete_quiz()
        elif choice == '5': break
        else: print("❌ 잘못된 입력")

if __name__ == "__main__":
    main()