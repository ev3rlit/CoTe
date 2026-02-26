def solution(record):
    
    # record로 발생한 모든 이벤트를 처리한 결과를 토대로
    # 최종 결과 메시지를  채팅방에 표기하는 것임.

    # 길이가 10만이므로, O(N), O(NlogN) 방법이 필요
    # 닉네임의 고유 식별자는 유저아디이를 제공함
    # 여기서 핵심은 record 이벤트를 순서대로 표기하되. 최종 닉네임 결과를 출력하는 것임.
    # 즉, 최종 닉네임을 계산후 record의 이벤트들을 다시 표기하면됨.

    
    # record의 각 이벤트별 시작 문자로 어떻게 처리할지를 분기
    # 모든 이벤트는 공백으로 구분되며  커맨드, UID, 닉네임 스냅샷으로 구성됨

    # 레코드를 순회하면서 이벤트를 처리
    # 각 이벤트의 커맨드를 토대로 닉네임을 기록
    # 입장 :  닉네임 업데이트
    # 퇴장 :  유지
    # 변경 :  닉네임 업데이트
    
    # 레코드를 순회하면서 이벤트를 텍스트로 변환


    message_formats = {
        'Enter' : '{}님이 들어왔습니다.',
        'Leave':'{}님이 나갔습니다.' 
    }

    # UID : 닉네임
    nicknames = {}
    events = [tuple(raw_event.split(' ')) for raw_event in record]
    for event in events:

        if event[0] == 'Enter':
            nicknames[event[1]] = event[2]
        elif event[0] == 'Change':
            nicknames[event[1]] = event[2]
        

    result = []    
    for event in events:
        cmd = event[0]
        nickname = nicknames.get(event[1], '')
        if cmd in message_formats:
            result.append(message_formats[cmd].format(nickname))

    return result
    