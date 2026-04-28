# 🎬NEXFLEX | OTT Web Service

> Flask 기반 OTT 웹 서비스 프로젝트

---
## 📚 목차
- [📌 프로젝트 소개](#-프로젝트-소개)
- [🛠 기술 스택 및 협업 도구](#--기술-스택-및-협업-도구)
- [💻 주요 기능](#-주요-기능)
- [💻 구현 기능 소개](#-구현-기능-소개)

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
| 강경근 | [@carrotkang](https://github.com/carrotkang) | - DB설계<br>- term페이지<br>- 서브페이지<br>- 마이페이지<br>- 고객센터페이지 |
| 고성민 | [@rhtjdals00-png](https://github.com/rhtjdals00-png) | - home페이지<br>- 관리자페이지<br>- 검색기능들 구현 |
| 유창현 | [@wjdalsdling-design](https://github.com/wjdalsdling-design) | -메인페이지<br>- 서브페이지<br>- 이미지DB |
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

## 💻 주요 기능

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


## 💻 구현 기능 소개

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

### 서브페이지(추천컨텐츠, 에피소드기능)
<img width="800" height="380" alt="subpage_1" src="https://github.com/user-attachments/assets/cf9a5d56-ab4f-4f9e-b3d8-9ddfb3916c09" />

- 쿼리문을 이용한 에피소드, 추천 콘텐츠 기능입니다.

### 서브페이지(리뷰, 별점, 찜, 이어보기 기능)
<img width="800" height="380" alt="subpage_2" src="https://github.com/user-attachments/assets/cd2e3229-2e17-42c8-97ba-91c9d5ea43d8" />
<img width="800" height="380" alt="subpage_3" src="https://github.com/user-attachments/assets/d8afb7c5-ff10-43fe-bff3-62d74749e886" />

- 실시간 별점기능, 리뷰기능, 찜, 이어보기 기능이 구현되어 있습니다.
- 리뷰는 본인이 작성한 리뷰는 최상단으로, 1개의 영상엔 1개의 리뷰만 남기실 수 있습니다.
- 영상을 다 시청하신 분만 리뷰를 작성하실 수 있습니다.
- 찜, 시청한 내역은 마이페이지에서 조회가 가능하며 이어보기 기능은 이어보기, 처음부터 보기를 선택가능하게 구현했습니다.

### 마이페이지(시청내역, 구매내역, 찜, 문의내역)
<img width="800" height="380" alt="mypage" src="https://github.com/user-attachments/assets/cc9fcd8a-ff53-4bbf-8cbc-a465e28226ef" />



- 시청하신 영상의 내역을 최신순으로 DB에 저장이 되어있습니다.
- 결제하신 구독권 내역을 확인할 수 있는 구매내역페이지가 있으며 구매하실 경우 구독권만료예정일이 연장되게 구현되어있습니다.
- 찜한 영상을 조회할 수 있으며 관리자에게 문의한 내역을 확인할 수 있습니다.

### 고객센터
<img width="800" height="380" alt="mypage" src="https://github.com/user-attachments/assets/ca1cbfbd-42ec-45e3-a0a6-424df005c123" />

- 공지사항중 중요 공지사항은 DB에 pinned속성을 줘 상단에 노출할 수 있도록 해놨습니다.
- 고객은 고객센터 페이지에서, 마이페이지에서 1대1 문의를 남길 수 있습니다.
- 검색기능을 통해 공지사항중 필요한 내용(제목)을 조회하기 편하게 구현되어있습니다.
- 공지사항 조회시 조회수가 증가되게 구현되어있습니다.

### 관리자페이지
<img width="800" height="380" alt="admin_page" src="https://github.com/user-attachments/assets/97ddd912-3af0-4fc4-a506-934cde1a5f9c" />


- 회원, 콘텐츠, 문의, 리뷰, 공지사항을 관리할 수 있는 관리자 페이지 입니다.
- 회원의 로그인을 차단할 수 있으며 콘텐츠의 등록, 수정, 삭제가 가능합니다.
- 회원이 남긴 1대1문의를 확인, 답변할 수 있으며 답변시 자동으로 답변완료 status로 변경됩니다.
- 공지사항은 pinned DB column을 이용해 상단 노출 공지사항을 선택할 수 있게 되어있습니다.
- 검색기능을 추가하여 더 빠른 조회를 할 수 있게 구현되어있습니다.
