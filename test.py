# 실패율
# 
# [문제 설명]
# 슈퍼 게임 개발자 오렐리는 큰 고민에 빠졌다. 그녀가 만든 게임은 재미는 있지만
# 입소문만으로 전혀 퍼져나가지 않았기 때문이다. 따라서 새로운 게임 메뉴를 만들었고,
# 새로운 게임 메뉴에는 다음과 같은 방법으로 "실패율"을 정의하였다.
#
# 실패율은 다음과 같이 정의한다.
# - 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수를 해당 스테이지에 도달한
#   플레이어 수로 나눈 값이다.
#
# 전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가
# 담긴 배열 stages가 주어질 때, 실패율이 높은 스테이지부터 내림차순으로 스테이지의
# 번호가 담긴 배열을 return 하도록 solution 함수를 완성하라.
#
# [제한사항]
# - 스테이지 개수 N은 1 이상 500 이하의 자연수이다.
# - stages의 길이는 1 이상 200,000 이하이다.
# - stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
# - 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
# - N + 1은 마지막 스테이지(N)까지 클리어한 사용자를 나타낸다.
# - 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
# - 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0으로 정의한다.

def solution(N, stages):
    answer = {}
    l = len(stages)
    
    for i in range(1,N+1):
        if l != 0:
            cnt_num = stages.count(i)
            answer[i] = cnt_num / l
            l -= cnt_num
        else: answer[i] = 0
        
    return sorted(answer, key = lambda x:-answer[x])

# 테스트 코드
if __name__ == "__main__":
    # 테스트 1: Programmers 입출력 예제
    N = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]
    result = solution(N, stages)
    print("테스트 1 결과:", result)
    # 정답: [3, 4, 2, 1, 5]

    # 테스트 2: 추가 문제 1
    N = 4
    stages = [4, 4, 4, 4, 4]
    result = solution(N, stages)
    print("테스트 2 결과:", result)
    # 정답: [4, 1, 2, 3]

    # 테스트 3: 추가 문제 2
    N = 3
    stages = [1, 1, 1, 1, 2, 2, 3]
    result = solution(N, stages)
    print("테스트 3 결과:", result)
    # 정답: [1, 2, 3]
