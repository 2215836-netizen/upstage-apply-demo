import re
import subprocess
import os
import sys

def parse_task_md(file_path):
    """
    task.md 파일을 파싱하여 이슈 제목과 본문을 추출합니다.
    """
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return []

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    issues = []
    current_issue = None

    # 정규표현식: "- [ ] **제목**" 형태를 찾음
    # 예: - [ ] **Part 1: 데이터 수집 모듈 (`collector.py`)** -> Part 1: 데이터 수집 모듈 (`collector.py`)
    title_pattern = re.compile(r'^\s*-\s*\[\s*\]\s*\*\*(.*?)\*\*')
    
    for line in lines:
        line = line.strip()
        title_match = title_pattern.match(line)

        if title_match:
            # 새로운 메인 태스크 시작, 이전 이슈가 있으면 저장
            if current_issue:
                issues.append(current_issue)
            
            # 새 이슈 초기화
            current_issue = {
                'title': f"[GIM] {title_match.group(1)}",
                'body': "## 작업 내용\n"
            }
        elif current_issue and line.startswith('- [ ]'):
            # 서브 태스크 (체크리스트) 추가
            # 예: - [ ] subtask -> - [ ] subtask
            current_issue['body'] += f"{line}\n"

    # 마지막 이슈 추가
    if current_issue:
        issues.append(current_issue)

    return issues

def create_github_issue(title, body):
    """
    gh CLI를 사용하여 이슈를 생성합니다.
    """
    try:
        # 중복 체크를 위해 기존 이슈 목록 조회 (선택 사항)
        # 여기서는 단순 생성을 수행합니다.
        
        cmd = [
            "gh", "issue", "create",
            "--title", title,
            "--body", body
        ]
        
        # Windows 환경에서 실행 시 shell=True가 필요할 수 있음
        # gh가 PATH에 있어야 함
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"Successfully created issue: {title}")
        print(result.stdout.strip())
        
    except subprocess.CalledProcessError as e:
        print(f"Failed to create issue: {title}")
        print(e.stderr)

def main():
    task_file = "task.md"
    print(f"Parsing {task_file}...")
    
    issues = parse_task_md(task_file)
    
    if not issues:
        print("No tasks found or file is empty.")
        return

    print(f"Found {len(issues)} tasks to convert into issues.")
    
    # 사용자 확인
    response = input("Do you want to proceed with creating these issues on GitHub? (y/n): ")
    if response.lower() != 'y':
        print("Aborted.")
        return

    for issue in issues:
        create_github_issue(issue['title'], issue['body'])

if __name__ == "__main__":
    main()
