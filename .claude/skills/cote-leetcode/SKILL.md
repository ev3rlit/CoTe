---
name: cote-leetcode
description: LeetCode 문제 풀이 템플릿을 자동 생성합니다. "leetcode", "릿코드", "LeetCode 문제", "leetcode 템플릿" 등의 요청에 트리거됩니다.
---

# LeetCode 문제 풀이 템플릿 생성 에이전트

당신은 LeetCode 문제 풀이 환경을 자동으로 세팅하는 에이전트입니다.
사용자가 LeetCode 문제 정보를 제공하면 solution.py, test.py, README.md를 생성합니다.

---

## 1. 정보 수집 (Information Gathering)

사용자에게 다음 정보를 수집하십시오:

### 필수 정보
- **문제 번호**: LeetCode 문제 번호 (예: 300)
- **문제명**: 영문 문제 제목 (예: Longest Increasing Subsequence)
- **메서드명**: LeetCode 채점 메서드명 (예: lengthOfLIS)
- **파라미터**: 메서드의 파라미터 목록 (예: `nums: List[int]`)
- **리턴 타입**: 반환 타입 (예: `int`)

### 선택 정보 (없으면 기본값 사용)
- **난이도**: Easy / Medium / Hard (기본: 미지정)
- **토픽**: 알고리즘 카테고리 (예: DP, Array, Binary Search)
- **저장 경로**: 직접 지정 가능 (기본: 토픽 기반 자동 결정)

사용자가 문제 URL만 제공한 경우, URL에서 문제명을 추출하고 나머지 정보를 질문하십시오.

---

## 2. 저장 경로 결정 (Path Resolution)

우선순위:
1. **사용자가 명시적으로 경로를 지정**한 경우 → 그 경로 사용
2. **토픽이 제공된 경우** → `{Topic}/LeetCode/{num}-{ProblemName}/` 형식
   - 예: `DP/LeetCode/300-LongestIncreasingSubsequence/`
   - ProblemName은 공백을 제거한 PascalCase
3. **토픽이 없는 경우** → 사용자에게 토픽을 질문

### 안전성 검사
- 작성 전 `ls` 명령으로 해당 경로에 파일이 이미 존재하는지 확인
- **파일이 존재할 경우**: "파일이 이미 존재합니다. 덮어쓰시겠습니까?" 확인 요청

---

## 3. 템플릿 읽기 (Template Loading)

**반드시 아래 경로의 레퍼런스 템플릿을 Read 도구로 읽어오십시오:**

```
.claude/skills/cote-leetcode/template-solution.py
.claude/skills/cote-leetcode/template-test.py
.claude/skills/cote-leetcode/template-readme.md
```

---

## 4. 파일 생성 (File Generation)

### 4.1 solution.py
레퍼런스 템플릿(`template-solution.py`)을 기반으로 플레이스홀더를 치환:
- `{{METHOD_NAME}}` → 실제 메서드명
- `{{PARAMS}}` → 실제 파라미터 (self 제외)
- `{{RETURN_TYPE}}` → 실제 리턴 타입
- 필요한 import문 추가 (List, Optional 등)

### 4.2 test.py
레퍼런스 템플릿(`template-test.py`)을 기반으로 플레이스홀더를 치환:
- `{{METHOD_NAME}}` → 실제 메서드명
- test_cases는 빈 예시로 남겨두되, 파라미터 구조에 맞는 주석 예시 포함

### 4.3 README.md
레퍼런스 템플릿(`template-readme.md`)을 기반으로 플레이스홀더를 치환:
- `{{PROBLEM_NUM}}` → 문제 번호
- `{{PROBLEM_NAME}}` → 문제명
- `{{DIFFICULTY}}` → 난이도
- `{{PROBLEM_SLUG}}` → URL용 슬러그 (예: longest-increasing-subsequence)
- `{{TAGS}}` → 관련 태그

---

## 5. 완료 안내 (Completion)

파일 생성 후 다음을 출력:

```
✅ LeetCode 문제 템플릿이 생성되었습니다!

📁 {저장 경로}
  ├── solution.py   (Solution 클래스 + {메서드명} 메서드)
  ├── test.py       (테스트 러너 설정 완료)
  └── README.md     (문제 기록 템플릿)

📝 다음 단계:
1. test.py에 LeetCode 예제 입출력을 추가하세요
2. python3 test.py로 테스트를 실행하세요
3. solution.py에 풀이를 구현하세요
4. README.md에 풀이 과정을 기록하세요
```
