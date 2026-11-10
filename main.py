import json
import os

def load_questions():
    if os.path.exists('questions.json'):
        with open('questions.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_questions(questions):
    with open('questions.json', 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=4)

def run_quiz(questions):
    if not questions:
        print("\n❌ 등록된 문제가 없습니다.")
        return
    
    score = 0
    print("\n📝 퀴즈를 시작합니다!")
    for i, q in enumerate(questions):
        print(f"\n문제 {i+1}. {q['question']}")
        for option in q['options']:
            print(option)
        
        try:
            answer = int(input("정답 번호: "))
            if answer == q['answer']:
                print("✅ 정답!")
                score += 1
            else:
                print(f"❌ 오답! 정답은 {q['answer']}번")
        except ValueError:
            print("❌ 숫자만 입력 가능합니다.")
    
    print(f"\n🎊 종료! 최종 점수: {score}/{len(questions)}")

def add_question(questions):
    print("\n➕ 새 문제 추가")
    question_text = input("문제 내용: ")
    options = [f"{i}. {input(f'{i}번 보기: ')}" for i in range(1, 5)]
    try:
        answer = int(input("정답 번호(1-4): "))
        questions.append({"question": question_text, "options": options, "answer": answer})
        save_questions(questions)
        print("✅ 저장 완료!")
    except ValueError:
        print("❌ 추가 실패 (숫자 입력 오류)")

# --- 새로 추가된 기능들 ---

def view_questions(questions):
    print("\n📋 등록된 문제 목록")
    if not questions:
        print("문제가 없습니다.")
        return
    for i, q in enumerate(questions):
        print(f"{i+1}. {q['question']} (정답: {q['answer']}번)")

def delete_question(questions):
    view_questions(questions)
    if not questions: return
    
    try:
        idx = int(input("\n🗑️ 삭제할 문제 번호를 입력하세요 (취소: 0): "))
        if 0 < idx <= len(questions):
            removed = questions.pop(idx - 1)
            save_questions(questions)
            print(f"✅ '{removed['question']}' 문제가 삭제되었습니다.")
        elif idx == 0:
            print("취소되었습니다.")
        else:
            print("❌ 잘못된 번호입니다.")
    except ValueError:
        print("❌ 숫자만 입력해주세요.")

# -----------------------

def show_menu():
    print("\n" + "="*25)
    print("🎮 파이썬 퀴즈 게임 v1.0")
    print("="*25)
    print("1. 퀴즈 풀기")
    print("2. 문제 추가하기")
    print("3. 문제 목록 보기")
    print("4. 문제 삭제하기")
    print("5. 종료하기")
    print("="*25)

def main():
    questions = load_questions()
    while True:
        show_menu()
        choice = input("선택: ")
        if choice == '1': run_quiz(questions)
        elif choice == '2': add_question(questions)
        elif choice == '3': view_questions(questions)
        elif choice == '4': delete_question(questions)
        elif choice == '5': 
            print("\n👋 게임을 종료합니다!"); break
        else: print("\n❌ 잘못된 입력입니다.")

if __name__ == "__main__":
    main()