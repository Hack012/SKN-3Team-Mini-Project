# 🖼️ 밈 생성기 프로젝트

로컬에서 실행 가능한 텍스트 기반 밈 이미지 생성기입니다.  
정해진 템플릿에 텍스트를 삽입하고, 원하는 폰트로 저장할 수 있습니다.

---

## 📁 프로젝트 구조

- `templates/` : 밈 템플릿 이미지
- `outputs/` : 생성된 이미지 저장 폴더
- `fonts/` : 사용자 지정 폰트
- `history.json` : 생성 내역 저장
- `main.py` : 실행 스크립트
- `meme_generator.py` : 이미지 처리 로직

---

## 🧑‍💻 브랜치 전략


| 브랜치명 | 목적 |
|----------|------|
| `main` | 메인 |
| `feature/template-list` | 템플릿 목록 조회 기능 개발 |
| `feature/text-input` | 텍스트 입력 및 처리 기능 개발 |
| `feature/font-select` | 폰트 선택 기능 개발 |
| `feature/save-image` | 이미지 저장 기능 개발 |
| `feature/history-log` | 생성 기록 조회 기능 개발 |


