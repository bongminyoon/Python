#%%
year = int(input())
age_type = input()

if age_type == "korea" :
    answer = 31

elif age_type == "Year":
    30
    


print(answer)
# %%
year = int(input())
age_type = input()

if age_type == "korea":
    answer = 2030 - year + 1

elif age_type == "Year":
    answer = 2030 - year


print(answer)
# %%
start = int(input()) #시작
before = int(input()) #70전까지
after = int(input())  #70<100 까지

money = start
month = 1
while money < 70:
    money += before

    month += 1
while money == 70 < 100:
    after

    month += 1

print(month)
# %%
def solution(numbers, our_score, score_list): #number 번호리스트 our_score 성적 score_list
    answer = []
    for i in range(len(numbers)):
        if numbers[our_score[i]] == score_list[i]:
            answer.append("Same")
        else:
            answer.append("Different")
    
    return answer

# %%
def func1(humidity, val_set):
    if humidity < val_set:
        return 3
     return 1
 def func3(humidity, val_set):
    if humidity < val_set:
        return 1
    return 
0
#%%
def solution(storage, num):
    storage = ["pencil", "pencil", "pencil", "book"]
    num = [2, 4, 3, 1]
    clean_storage = []
    clean_num = []
    for i in range(len(storage)):
        if storage[i] in clean_storage:
            pos = clean_storage.index(storage[i])
            clean_num[pos] += num[i]
        else:
            clean_storage.append(num[i])
            clean_num.append(num[i])
            
    # 아래 코드에는 틀린 부분이 없습니다.
            
    max_num = max(clean_num)
    answer = clean_storage[clean_num.index(max_num)]
    return answer

# %%
