---
# 커맨드 메타데이터 (모두 선택사항)
description: 이 커맨드가 하는 일을 간단히 설명
allowed-tools: Read, Grep, Write, Bash(python3:*)
argument-hint: [arg1] [arg2]
# model: claude-opus-4-5-20251101
---

# 커맨드 제목

## 지시사항

여기에 Claude가 따라야 할 구체적인 지시사항을 작성하세요.

## 인자 사용법

- `$ARGUMENTS` - 모든 인자를 하나의 문자열로 받음
- `$1`, `$2`, `$3` - 개별 인자 접근

예: 사용자가 `/my-command hello world` 입력시
- `$ARGUMENTS` = "hello world"
- `$1` = "hello"
- `$2` = "world"

## Bash 명령 실행 (선택)

현재 git 상태: !`git status --short`
현재 브랜치: !`git branch --show-current`

## 파일 참조 (선택)

특정 파일 내용 포함: @path/to/file.py

---

## 사용 예시

```
/my-command arg1 arg2
```
