# [카카오 인턴] 키패드 누르기

def solution(numbers, hand):
    answer = ''

    phone = {
        1:(0, 0), 2:(0, 1), 3:(0, 2),
        4:(1, 0), 5:(1, 1), 6:(1, 2),
        7:(2, 0), 8:(2, 1), 9:(2, 2),
        '*':(3, 0), 0:(3, 1), '#':(3, 2)
    }

    left, right = '*', '#'

    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            left = n
        elif n in [3, 6, 9]:
            answer += 'R'
            right = n
        else:
            l_dist = abs(phone[left][0] - phone[n][0]) + abs(phone[left][1] - phone[n][1])
            r_dist = abs(phone[right][0] - phone[n][0]) + abs(phone[right][1] - phone[n][1])

            if l_dist < r_dist:
                answer += 'L'
                left = n
            elif r_dist < l_dist:
                answer += 'R'
                right = n
            else:
                if hand == 'left':
                    answer += 'L'
                    left = n
                else:
                    answer += 'R'
                    right = n

    return answer
