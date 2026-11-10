import json
import os

# 1. 파일에서 퀴즈 불러오기
def load_questions():
    if os.path.exists('questions.json'):
        with open('questions.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# 2. 퀴즈 풀기 기능
def run_quiz(questions):
    if not questions:
        print("\n❌ 등록된 문제가 없습니다. 문제를 먼저 추가해주세요!")
        return

    score = 0
    print("\n📝 퀴즈를 시작합니다!")
    
    for i, q in enumerate(questions):
        print(f"\n문제 {i+1}. {q['question']}")
        for option in q['options']:
            print(option)
        
        try:
            answer = int(input("정답 번호를 입력하세요: "))
            if answer == q['answer']:
                print("✅ 정답입니다!")
                score += 1
            else:
                print(f"❌ 틀렸습니다. 정답은 {q['answer']}번입니다.")
        except ValueError:
            print("❌ 숫자만 입력 가능합니다. 이번 문제는 틀린 것으로 처리됩니다.")

    print(f"\n🎊 퀴즈 종료! 당신의 점수는 {score}/{len(questions)}입니다.")

def show_menu():
    print("\n" + "="*20)
    print("🎮 파이썬 퀴즈 게임")
    print("="*20)
    print("1. 퀴즈 풀기")
    print("2. 문제 추가하기 (준비중)")
    print("3. 종료하기")
    print("="*20)

def main():
    questions = load_questions()
    
    while True:
        show_menu()
        choice = input("원하는 메뉴 번호를 입력하세요: ")

        if choice == '1':
            run_quiz(questions)
        elif choice == '2':
            print("\n➕ 문제 추가 기능은 다음 단계에서 만들 거예요!")
        elif choice == '3':
            print("\n👋 게임을 종료합니다. 수고하셨습니다!")
            break
        else:
            print("\n❌ 잘못된 입력입니다.")

if __name__ == "__main__":
    main()