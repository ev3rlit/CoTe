# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Git Commit Message Convention ⭐ **PRIORITY**

**This is the most important convention in this repository.**

### Format
```
keyword(topic) : 한글 설명
```

### Keywords
- `add` - 새로운 문제 풀이 추가
- `fix` - 기존 풀이 버그 수정
- `update` - 풀이 개선 또는 복잡도 최적화
- `docs` - 문서 수정 (README, CLAUDE.md 등)
- `refactor` - 코드 리팩토링

### Single Problem Commit
```
add(해시) : 완주하지못한선수 문제 풀이
fix(스택) : 올바른괄호 문제 풀이 버그 수정
update(DP) : N으로표현 풀이 최적화 (O(n²) → O(n))
```

### Multiple Changes in One Commit
```
add(updates) : 여러 문제 풀이 및 문서 업데이트

- 해시/Programmers/완주하지못한선수 문제 풀이 추가
- 스택/Programmers/올바른괄호 문제 풀이 추가
- 메인 README.md 인덱스 테이블 업데이트
```

### Key Rules
✅ **DO**:
- 키워드는 **영어** (add, fix, update, docs, refactor)
- 한줄 설명과 본문 리스트는 **한글**
- 알고리즘 유형 명시 예: `해시`, `DP`, `스택`
- 의미 있는 설명 작성 (예: 최적화 전후 복잡도 언급)

❌ **DON'T**:
- 한글로 키워드 사용
- 의미 불명확한 메시지 (예: "수정함", "추가")
- 영어 설명 사용

### Commit Examples
```bash
# 새 문제 풀이
git commit -m "add(해시) : 완주하지못한선수 문제 풀이"

# 버그 수정
git commit -m "fix(정렬) : 가장큰수 풀이 오류 수정"

# 성능 개선
git commit -m "update(DP) : N으로표현 풀이 메모이제이션으로 최적화"

# 문서 수정
git commit -m "docs : CLAUDE.md 커밋 메시지 규칙 추가"

# 여러 문제 한번에 추가
git commit -m "add(problems) : 해시 주제 3문제 풀이 추가

- 해시/Programmers/두개뽑아서더하기
- 해시/Programmers/완주하지못한선수
- 해시/Programmers/전화번호목록"
```

---

## Project Overview

**CoTe** (코딩 테스트 - Coding Test) is a personal algorithm practice repository for daily problem-solving and learning.

### Purpose
- Daily coding test practice with structured problem-solving documentation
- Learning and mastering algorithms and data structures
- Recording problem-solving approaches and reflections
- Building a portfolio of solved problems with detailed explanations

### Key Characteristics
- **Language**: Python 3
- **Documentation**: Korean
- **Structure**: `유형/플랫폼/문제명` 계층 구조 (알고리즘 유형 → 플랫폼 → 문제)
- **Multi-platform**: Programmers, Baekjoon (BOJ), LeetCode 지원
- **No external dependencies**: Standalone pure Python implementations
- **Git-based tracking**: Each problem is a commit checkpoint

## Repository Structure

### Main Files
- `README.md` - Project overview, problem index table, and learning statistics
- `CLAUDE.md` - This guidance file (for AI assistants)
- `AGENTS.md` - Symbolic link to CLAUDE.md (for other AI agents)
- `LICENSE` - Project license
- `.gitignore` - Python-specific ignore patterns

### Problem Organization

```
CoTe/
├── _runners/                            # Test execution environment (multi-platform support)
│   ├── __init__.py                      # Package init (exports run_tests, run_boj_tests, run_leetcode_tests)
│   ├── python.py                        # Programmers test runner (함수 기반)
│   ├── boj.py                           # Baekjoon test runner (stdin/stdout 기반)
│   └── leetcode.py                      # LeetCode test runner (Solution 클래스 기반)
│
├── _template_programmers/               # Programmers 문제 템플릿
│   ├── README.md
│   ├── solution.py                      # def solution(): ...
│   └── test.py                          # run_tests 사용
│
├── _template_boj/                       # Baekjoon 문제 템플릿
│   ├── README.md
│   ├── solution.py                      # stdin/stdout 방식
│   └── test.py                          # run_boj_tests 사용
│
├── _template_leetcode/                  # LeetCode 문제 템플릿
│   ├── README.md
│   ├── solution.py                      # class Solution: ...
│   └── test.py                          # run_leetcode_tests 사용
│
├── _learning/                           # 알고리즘 학습 자료
│
├── 해시/                                # 알고리즘 유형별 최상위 폴더
│   └── Programmers/                     # 플랫폼별 하위 폴더
│       ├── 완주하지못한선수/             # 문제별 폴더
│       │   ├── README.md
│       │   ├── solution.py
│       │   └── test.py
│       ├── 베스트앨범/
│       └── ...
│
├── DP/
│   ├── Programmers/
│   │   └── N으로 표현/
│   ├── Baekjoon/
│   │   └── 평범한배낭/
│   └── LeetCode/
│       └── 300-LongestIncreasingSubsequence/
│
└── 스택/
    ├── Programmers/
    │   └── 괄호짝맞추기/
    └── Baekjoon/
        └── 스택/
```

### Folder Hierarchy
```
유형/플랫폼/문제명/
```

- **유형** (Algorithm Category): 해시, 스택, 큐, 트리, DP, BFS, DFS, 구현, 완전탐색, 그래프 등
- **플랫폼** (Platform): `Programmers`, `Baekjoon`, `LeetCode`
- **문제명** (Problem Name):
  - Programmers: 한글 문제명 (예: `완주하지못한선수`)
  - Baekjoon: 한글 문제명 (예: `평범한배낭`)
  - LeetCode: `번호-영문이름` (예: `300-LongestIncreasingSubsequence`)

### Current Algorithm Categories

| 카테고리 | Programmers | Baekjoon | LeetCode |
|---------|------------|----------|----------|
| 맛배기 | ✅ | | |
| 스택 | ✅ | ✅ | |
| 큐 | ✅ | | |
| 해시 | ✅ | | |
| 트리 | ✅ | | |
| 이분탐색 | ✅ | | |
| 순회 | | ✅ | |
| 집합 | ✅ | | |
| DP | ✅ | ✅ | ✅ |
| BFS | ✅ | | |
| DFS | ✅ | | |
| 구현 | ✅ | | |
| 그래프 | ✅ | ✅ | |
| 완전탐색 | ✅ | | |

## Problem Documentation Template

Each problem's `README.md` follows this structure:

```markdown
# [문제명]

#태그1 #태그2 #태그3

## 풀이 과정
### 핵심 아이디어
### 접근 방법
### 코드

## 회고
### 배운 점
### 어려웠던 부분
### 개선할 점

---
**복잡도**: O()
**풀이 날짜**:
```

### Documentation Philosophy
- **Focus on process**: Emphasize thinking process, not just final solution
- **Minimal metadata**: No redundant information (links, problem descriptions already in original sources)
- **Reflective learning**: Strong emphasis on learnings, difficulties, and improvements
- **Concise but detailed**: Balance between brevity and meaningful explanation

## Common Tasks

### Creating a New Problem

#### Programmers
```bash
# 1. Copy template
cp -r _template_programmers 해시/Programmers/전화번호목록
cd 해시/Programmers/전화번호목록

# 2. Add test cases to test.py → Run tests
python3 test.py

# 3. Implement solution.py → Edit README.md
# 4. Commit
git commit -m "add(해시) : 전화번호목록 문제 풀이"
```

#### Baekjoon
```bash
# 1. Copy template
cp -r _template_boj DP/Baekjoon/1로만들기
cd DP/Baekjoon/1로만들기

# 2. Add test cases to test.py → Run tests
python3 test.py

# 3. Implement solution.py → Edit README.md
# 4. Commit
git commit -m "add(DP) : 1로만들기 문제 풀이 (BOJ 1463)"
```

#### LeetCode
```bash
# 1. Copy template
cp -r _template_leetcode DP/LeetCode/300-LongestIncreasingSubsequence
cd DP/LeetCode/300-LongestIncreasingSubsequence

# 2. Add test cases to test.py → Run tests
python3 test.py

# 3. Implement solution.py → Edit README.md
# 4. Commit
git commit -m "add(DP) : LIS 문제 풀이 (LeetCode 300)"
```

### File Responsibilities
- **test.py** (per problem): Test cases definition only (modify)
- **solution.py** (per problem): Problem solution (modify)
- **README.md** (per problem): Problem documentation (modify)
- **_runners/** (root, shared): Test execution environment
  - `__init__.py`: Package initialization (exports all runners)
  - `python.py`: Programmers runner — `run_tests(func, test_cases)` — **DO NOT modify**
  - `boj.py`: Baekjoon runner — `run_boj_tests(...)` — **DO NOT modify**
  - `leetcode.py`: LeetCode runner — `run_leetcode_tests(...)` — **DO NOT modify**

### Test Case Format

#### Programmers (함수 기반)
```python
test_cases = [
    # 여러 매개변수: 튜플 사용 (언팩됨)
    {
        "name": "여러 인자",
        "input": (1, 2, 3),      # 튜플 → solution(1, 2, 3)
        "expected": 6,
    },

    # 단일 매개변수: 리스트, 문자열, 숫자 등 (그대로 전달)
    {
        "name": "단일 리스트",
        "input": [1, 2, 3],      # 리스트 → solution([1, 2, 3])
        "expected": [1, 2, 3],
    },
]
```

**규칙**:
- **튜플** (`(a, b, c)`): 여러 인자로 언팩 → `solution(a, b, c)`
- **그 외** (리스트, 문자열, 숫자): 단일 인자로 전달 → `solution(data)`

### Testing Locally
```bash
cd 유형/플랫폼/문제명

# test.py 실행 (자동으로 _runners 패키지 참조)
python3 test.py

# Output: ✓ 통과 or ✗ 실패, time, memory for each test case
```

### Submitting Solutions

#### Programmers
1. Copy `solution()` function from `solution.py`
2. Paste into Programmers editor → Submit

#### Baekjoon
1. Copy entire `solution.py` (includes stdin/stdout handling)
2. Paste into Baekjoon editor → Submit

#### LeetCode
1. Copy `Solution` class from `solution.py`
2. Paste into LeetCode editor → Submit

### Updating Main README
When adding new problems, update `/README.md`:
- Add row to problem index table
- Update total problem count in statistics
- Add problem tags to algorithm categorization section if new topic

## Algorithm Categories

Supported algorithm topics (mapped to folder names):
- **#맛배기** - Introductory/warm-up problems
- **#해시** - Hash/Dictionary-based problems
- **#스택** **#큐** - Stack/Queue structures
- **#트리** - Tree structures (BST, traversal, etc.)
- **#이분탐색** - Binary search
- **#순회** - Iteration/traversal
- **#집합** - Set operations (Union-Find, etc.)
- **#DP** - Dynamic Programming
- **#BFS** **#DFS** - Graph search techniques
- **#구현** - Implementation/Simulation
- **#완전탐색** - Brute force/exhaustive search
- **#그래프** **#최단경로** - Graph problems
- **#정렬** - Sorting algorithms
- **#그리디** - Greedy algorithms
- **#문자열** - String manipulation
- **#수학** **#조합론** - Mathematical problems

## Code Review Focus Areas

When reviewing solutions, prioritize:

1. **Complexity Analysis**
   - Time complexity: Be explicit about O() notation
   - Space complexity: Consider auxiliary space
   - Is there a more optimal approach?

2. **Code Clarity**
   - Clear variable names
   - Logical problem-solving flow
   - **Comments and Documentation**:
     - Comments are a critical part of the problem-solving process
     - They record the thought process and prevent forgetting key ideas during implementation
     - Evaluate comments as an important feedback element in code reviews
     - **Good comments**: Clear core ideas, approach methods, constraints, and edge cases
     - **Comments to improve**: Inconsistent with code, incorrect concepts, too vague
     - **Note**: Having many comments is NOT a problem - it's a good habit for organizing the solution process
     - Focus on comment quality (clarity, accuracy) rather than quantity

3. **Edge Cases**
   - Empty inputs
   - Single elements
   - Maximum constraints
   - Special cases mentioned in problem

4. **Pythonic Patterns**
   - Use appropriate data structures (dict, set, deque, etc.)
   - Leverage built-in functions efficiently
   - Follow Python conventions

## Key Files to Reference

### For Adding New Problems
- `_template_programmers/` - Programmers 문제 템플릿
- `_template_boj/` - Baekjoon 문제 템플릿
- `_template_leetcode/` - LeetCode 문제 템플릿

### For Testing (Shared Infrastructure)
- `_runners/` (root package) - Test execution environment (common, shared by all test.py)
  - `__init__.py` - Package initialization
    - `run_tests`: Programmers용 (함수 기반)
    - `run_boj_tests`: Baekjoon용 (stdin/stdout 기반)
    - `run_leetcode_tests`: LeetCode용 (Solution 클래스 기반)
  - `python.py`, `boj.py`, `leetcode.py` - 각 플랫폼 러너 (**DO NOT modify**)

### Test Execution Flow
1. Run: `cd 유형/플랫폼/문제명 && python3 test.py`
2. `test.py` imports solution from `solution.py`
3. `test.py` imports appropriate runner from `_runners`
4. Tests run with automatic time/memory measurement

### For Project Context
- `README.md` - Project overview and index
- `.gitignore` - Ignored files/directories

### Separation of Concerns
- **Modify per problem**: `README.md`, `solution.py`, `test.py` (test_cases array only)
- **Common (shared, referenced)**: `_runners/` (root, multi-platform test environment)
  - Single point of maintenance for test logic
  - Platform-specific runners for each submission site

## Guidelines for Claude

When assisting with this repository:

1. **Creating New Problems**: Use appropriate platform template; follow `유형/플랫폼/문제명` structure
2. **Documenting Solutions**: Emphasize process over just code; include reflections
3. **Code Analysis**: Focus on complexity, optimization, and algorithm choice justification
4. **Repo Maintenance**: Help update main README index when problems are added
5. **Learning Support**: Suggest algorithmic patterns and optimization opportunities
6. **Language**: Use Korean for documentation and explanations; Python code can use English variable names
7. **Comment Evaluation**:
   - Recognize comments as an essential part of the learning and problem-solving process
   - DO NOT criticize code for having "too many comments" or being "verbose"
   - Instead, evaluate whether comments clearly capture the problem-solving approach
   - Provide feedback on comment quality: accuracy, clarity, and usefulness for future review
   - Encourage thoughtful commenting as it helps solidify understanding and aids future revisits

## No Special Setup Required

- Pure Python 3 implementation
- No package dependencies
- No build or test framework (testing is manual or manual test cases)
- No development environment setup beyond Python 3

Solutions can be run directly with `python3 solution.py`.
