def solution(enroll, referal, seller, amount):
    #parent 딕셔너리는 key는 enroll의 노드, value는 referal의 노드로 구성
    parent = dict(zip(enroll, referal))

    # total 딕셔너리 생성 및 초기화
    total = { name : 0 for name in enroll}

    # seller 리스트와 amount 리스트를 이용해 이익 분배
    for i in range(len(seller)):
        # 판매자가 판매한 총 금액 계산
        money = amount[i] * 100
        cur_name = seller[i]

        #판매자부터 차례대로 상위 노드로 이동해 이익 분배
        while money > 0 and cur_name != '-':
            total[cur_name] += money - money // 10
            cur_name = parent[cur_name]
            # 10%를 제외한 금액 계산
            money //= 10
        #enroll 리스트의 모든 노드에 대해 해당하는 이익을 리스트로 반환
        return [total[name] for name in enroll]
    
enroll = ["john","mary","edward","sam","emily","jaimie","tod","young"]
referal = ["-","-","mary","edward","mary","mary","jaimie","edward"]
seller = ["young","john","tod","emily","mary"]
amount = [12, 4, 2, 5, 10]

solution(enroll, referal,seller,amount)