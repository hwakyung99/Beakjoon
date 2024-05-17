for test_case in range(1, 11):
    t = int(input())
    word = input().strip()
    sentence = input().strip()
   
    print(f"#{t} {sentence.count(word)}")
