import json
import os

# 1. 파일에서 퀴즈 불러오기
def load_questions():
    if os.path.exists('questions.json'):
        with open('questions.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# 2. 파일에 퀴즈 저장하기 (새로 추가됨!)
def save_questions(questions):
    with open('questions.json', 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=4)

# 3. 퀴즈 풀기 기능
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
            print("❌ 숫자만 입력 가능합니다.")

    print(f"\n🎊 퀴즈 종료! 점수: {score}/{len(questions)}")

# 4. 문제 추가하기 기능 (새로 추가됨!)
def add_question(questions):
    print("\n➕ 새로운 문제를 추가합니다.")
    question_text = input("문제 내용을 입력하세요: ")
    
    options = []
    for i in range(1, 5):
        opt = input(f"{i}번 보기 내용을 입력하세요: ")
        options.append(f"{i}. {opt}")
    
    try:
        answer = int(input("정답 번호(1~4)를 입력하세요: "))
        
        # 새로운 문제 객체 생성
        new_q = {
            "question": question_text,
            "options": options,
            "answer": answer
        }
        
        questions.append(new_q) # 리스트에 추가
        save_questions(questions) # 파일에 저장
        print("\n✅ 문제가 성공적으로 저장되었습니다!")
    except ValueError:
        print("\n❌ 숫자를 입력해야 합니다. 추가 실패!")

def show_menu():
    print("\n" + "="*20)
    print("🎮 파이썬 퀴즈 게임")
    print("="*20)
    print("1. 퀴즈 풀기")
    print("2. 문제 추가하기")
    print("3. 종료하기")
    print("="*20)

def main():
    # 프로그램 시작할 때 파일에서 문제 로드
    questions = load_questions()
    
    while True:
        show_menu()
        choice = input("원하는 메뉴 번호를 입력하세요: ")

        if choice == '1':
            run_quiz(questions)
        elif choice == '2':
            add_question(questions)
        elif choice == '3':
            print("\n👋 게임을 종료합니다!")
            break
        else:
            print("\n❌ 잘못된 입력입니다.")

if __name__ == "__main__":
    main()