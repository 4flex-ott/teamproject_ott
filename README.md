# 🎬NEXFLEX | OTT Web Service

> Flask 기반 OTT 웹 서비스 프로젝트

---

## 📚 목차

- [📌 프로젝트 소개](#프로젝트-소개)
- [🛠 기술 스택 및 협업 도구](#기술-스택-및-협업-도구)
- [💻 주요 기능](#주요-기능)
- [🎥 주요 기능 실행화면](#주요-기능-실행화면)

--- 

## 📌 프로젝트 소개
NEXFLEX는 실제 OTT 서비스 구조를 기반으로 설계된 웹 애플리케이션으로,
사용자가 콘텐츠를 탐색하고 개인화된 서비스를 경험할 수 있도록 구현되었습니다.
회원가입 및 로그인(인증 시스템), 콘텐츠 검색 및 조회, 찜 기능, 사용자 맞춤 인터페이스 등 핵심 기능을 포함하고 있으며,
Flask 기반 백엔드와 데이터베이스 연동을 통해 동적인 서비스 환경을 구축했습니다.


### 프로젝트 기간
- 전체 개발 기간 : **2026-04-06 ~ 2026-04-29**

### 팀원 소개
| 이름 | GitHub | 역할 |
|------|--------|------|
| 강경근 | [@carrotkang](https://github.com/carrotkang) | - 공지사항 게시판<br>- 메인 페이지 (헤더, 푸터)<br>- 게시물 정렬 기능<br>- Front-end (jQuery) |
| 고성민 | [@rhtjdals00-png](https://github.com/rhtjdals00-png) | - 문의하기 게시판<br>- 채널 페이지, 구독 기능<br>- 회원가입 / 로그인<br>- AWS 배포 |
| 최정민 | [@wjdalsdling-design](https://github.com/wjdalsdling-design) | - 로그인/로그아웃, 회원가입<br>- 비밀번호 암호화<br>- Front-end |

---

##  🛠 기술 스택 및 협업 도구

### 기술 스택
- **Backend**: Python, Flask  
- **Frontend**: HTML, CSS, JavaScript  
- **Database**: SQLite
- **Authentication**: Flask-Login  
- **Security**: Password Hashing (Werkzeug)  
- **Template Engine**: Jinja2  
- **API**: 카카오 OAuth 2.0, 네이버 OAuth 2.0, Gmail SMTP 
- **Version Control**: Git, GitHub
- **UI Framework**: Bootstrap

### 작업 관리
- GitHub를 활용한 소스코드 버전 관리
- 기능 단위 브랜치를 분리하여 개발 후 develop 브랜치에 병합
- Figma를 활용한 UI/UX 설계 및 팀원 간 디자인 협업

---

## 💻 구현 기능

### 상단 고정 메뉴 ( Header )
- 누르면 메인 페이지로 이동시켜주는 로고
  - 로그인이 되어 있지 않은 경우 - 홈으로 이동
  - 로그인이 되어 있는 경우 - 메인으로 이동
- 콘텐츠 검색 기능
- 마이페이지 
- 로그아웃

### 회원가입 / 로그인 페이지
- 인증된 사용자만 마이페이지 등 주요 기능 접근 가능
- 비회원 사용자에 대한 접근 제한 처리
- 소셜 로그인 (카카오, 네이버)
- 조건 충족 시 비밀번호 설정 
- 비밀번호 재설정 시 이메일 인증


### 메인 / 서브 페이지
- 콘텐츠 목록 조회 및 상세 페이지 제공
- 카테고리별 콘텐츠 탐색 기능


### 마이페이지
- 내 정보 수정
- 이용권 결제 기능 (Iamport API)
- 리뷰 작성
- 찜 목록 생성
- 계정 정보 통합 (소셜 로그인 시)

### 관리자 페이지
- 콘텐츠 등록, 수정, 삭제 기능
- 사용자 및 서비스 관리 기능



---


## 💻 주요 기능 소개

### 👤 회원가입 기능
<img width="1000" height="400" alt="회원가입" src="https://github.com/user-attachments/assets/868c413b-0919-4c77-9fa5-b97af40da4b0" />

- 회원가입 시 입력한 사용자 정보를 DB의 user 테이블에 저장합니다.

<img width="1000" height="400" alt="비밀번호 설정" src="https://github.com/user-attachments/assets/6bc57ade-af9e-4e7c-9636-92d9f27c937f" />

- 비밀번호 설정 시 보안 등급 적용 및 비밀번호 확인 일치 여부를 검증할 수 있습니다.
- 회원가입 완료 시 로그인 페이지로 이동합니다.


### 👤 소셜 로그인
<table>
  <tr>
    <td align="center"><b>카카오 로그인</b></td>
    <td align="center"><b>네이버 로그인</b></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/5ed61b25-3de6-4451-aa09-49fca32f934e" width="100%"></td>
    <td><img src="https://github.com/user-attachments/assets/a8c95c22-3fda-43c0-8311-d11c1dc31f9d" width="100%"></td>
  </tr>
</table>

- 기존 소셜 계정을 통해 로그인 가능합니다.

### 👤 계정 통합 및 회원정보 수정
<img width="800" height="380" alt="계정정보통합" src="https://github.com/user-attachments/assets/c2fc30a6-f6af-4ba9-978d-b73cfb8bbcec" />

- 소셜 로그인으로 가입한 사용자는 바로 회원정보 수정이 불가능합니다.
- 먼저 이메일 기반 회원가입을 통해 계정을 통합해야 합니다.
- 계정 통합 완료 후에는 일반 회원과 동일하게 회원정보 수정이 가능합니다.

<img width="800" height="380" alt="회원정보수정" src="https://github.com/user-attachments/assets/66538321-b679-4c69-b6e8-1f4f74727301" />

- 이메일로 회원가입한 사용자는 회원정보 수정 기능을 바로 이용할 수 있습니다.

### 💳 결제 기능
<img width="800" height="380" alt="결제" src="https://github.com/user-attachments/assets/421ebe52-412d-4d6b-b7bc-49cf17683a89" />

- 마이페이지에서 이용권을 구매할 수 있습니다.
- 결제는 토스페이먼츠(Toss Payments) API를 통해 진행됩니다.
- 사용자는 토스를 이용하여 안전하게 결제할 수 있습니다.




