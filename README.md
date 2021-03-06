# 원티드x위코드 백엔드 프리온보딩 과제 :: 카닥

# 배포 주소 : 3.34.198.3:8000

# 1. 본인소개

안녕하세요.

원티드x위코드 백엔드 프리온보딩 과정 교육생 이기용입니다.

해당 Repository는 "카닥"의 기업과제애 대한 코드가 담겨져 있습니다.

과제 내용과 구현 사항들 아래에 기술되어 있으니, 확인 부탁 드립니다.

읽어주셔서 감사합니다.


------

# 2. 과제

#### [필수 포함 사항]

- READ.ME 작성
  - 프로젝트 빌드, 자세한 실행 방법 명시
  - 구현 방법과 이유에 대한 간략한 설명
  - 완료된 시스템이 배포된 서버의 주소
  - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현

#### [요구 사항] 

- 데이터베이스 환경은 별도로 제공하지 않습니다.
 **RDB중 원하는 방식을 선택**하면 되며, sqlite3 같은 별도의 설치없이 이용 가능한 in-memory DB도 좋으며, 가능하다면 Docker로 준비하셔도 됩니다.
- 단, 결과 제출 시 README.md 파일에 실행 방법을 완벽히 서술하여 DB를 포함하여 전체적인 서버를 구동하는데 문제없도록 해야합니다.
- 데이터베이스 관련처리는 raw query가 아닌 **ORM을 이용하여 구현**합니다.


[과제 안내]

사용자 생성 API

- ID/Password로 사용자를 생성하는 API.
- 인증 토큰을 발급하고 이후의 API는 인증된 사용자만 호출할 수 있다.

사용자가 소유한 타이어 정보를 저장하는 API

- 자동차 차종 ID(trimID)를 이용하여 사용자가 소유한 자동차 정보를 저장한다.
- 한 번에 최대 5명까지의 사용자에 대한 요청을 받을 수 있도록 해야한다. 즉 사용자 정보와 trimId 5쌍을 요청데이터로 하여금 API를 호출할 수 있다는 의미이다.

사용자가 소유한 타이어 정보 조회 API
- 사용자 ID를 통해서 2번 API에서 저장한 타이어 정보를 조회할 수 있어야 한다.

------

# 3. Skill & Tools

- **Skill :** [![img](https://camo.githubusercontent.com/0f3eb5f3e4c61d94657f16605ea420a0216673dfb085d100c458ed15be0599d2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d3337373641423f7374796c653d666f722d7468652d6261646765266c6f676f3d507974686f6e266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/0f3eb5f3e4c61d94657f16605ea420a0216673dfb085d100c458ed15be0599d2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d3337373641423f7374796c653d666f722d7468652d6261646765266c6f676f3d507974686f6e266c6f676f436f6c6f723d7768697465) [![img](https://camo.githubusercontent.com/c4c1014e1f168ff271282b67ec9059c3cfc16b2a5cba6e0c7c98c3530f47f45c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446a616e676f2d3039324532303f7374796c653d666f722d7468652d6261646765266c6f676f3d446a616e676f266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/c4c1014e1f168ff271282b67ec9059c3cfc16b2a5cba6e0c7c98c3530f47f45c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446a616e676f2d3039324532303f7374796c653d666f722d7468652d6261646765266c6f676f3d446a616e676f266c6f676f436f6c6f723d7768697465) [![img](https://camo.githubusercontent.com/9bf3ab62e0f872ed37f7d590e4577137b2dda11ffb0786f9b858cd39c2dc8c7f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f73716c6974652d3039324532303f7374796c653d666f722d7468652d6261646765266c6f676f3d73716c697465266c6f676f436f6c6f723d23303033423537)](https://camo.githubusercontent.com/9bf3ab62e0f872ed37f7d590e4577137b2dda11ffb0786f9b858cd39c2dc8c7f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f73716c6974652d3039324532303f7374796c653d666f722d7468652d6261646765266c6f676f3d73716c697465266c6f676f436f6c6f723d23303033423537)
- **Depoly :** [![img](https://camo.githubusercontent.com/9ad32f291fa1163a77cd2e919f8378b38bf66fd9de517178bf890e521178f341/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f415753204543322d3233324633453f7374796c653d666f722d7468652d6261646765266c6f676f3d416d617a6f6e20415753266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/9ad32f291fa1163a77cd2e919f8378b38bf66fd9de517178bf890e521178f341/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f415753204543322d3233324633453f7374796c653d666f722d7468652d6261646765266c6f676f3d416d617a6f6e20415753266c6f676f436f6c6f723d7768697465) [![img](https://camo.githubusercontent.com/fbef20533fc559c07dcaae57d63beab86709421dfd5428391a563096c88ead5a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f636b65722d3234393645443f7374796c653d666f722d7468652d6261646765266c6f676f3d446f636b6572266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/fbef20533fc559c07dcaae57d63beab86709421dfd5428391a563096c88ead5a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f636b65722d3234393645443f7374796c653d666f722d7468652d6261646765266c6f676f3d446f636b6572266c6f676f436f6c6f723d7768697465)
- **ETC :** [![img](https://camo.githubusercontent.com/fdb91eb7d32ba58701c8e564694cbe60e706378baefa180dbb96e2c1cfb9ec0f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769742d4630353033323f7374796c653d666f722d7468652d6261646765266c6f676f3d476974266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/fdb91eb7d32ba58701c8e564694cbe60e706378baefa180dbb96e2c1cfb9ec0f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769742d4630353033323f7374796c653d666f722d7468652d6261646765266c6f676f3d476974266c6f676f436f6c6f723d7768697465) [![img](https://camo.githubusercontent.com/23a917c56e310800a66c58a03447dd42c0dea2abff415ef9719e3e837c1cff82/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769746875622d3138313731373f7374796c653d666f722d7468652d6261646765266c6f676f3d476974687562266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/23a917c56e310800a66c58a03447dd42c0dea2abff415ef9719e3e837c1cff82/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769746875622d3138313731373f7374796c653d666f722d7468652d6261646765266c6f676f3d476974687562266c6f676f436f6c6f723d7768697465) [![img](https://camo.githubusercontent.com/879423585ed087f3c973857c43ba7e7d84f52c993d2c937055726339fbf921d9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f506f73746d616e2d4646364333373f7374796c653d666f722d7468652d6261646765266c6f676f3d506f73746d616e266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/879423585ed087f3c973857c43ba7e7d84f52c993d2c937055726339fbf921d9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f506f73746d616e2d4646364333373f7374796c653d666f722d7468652d6261646765266c6f676f3d506f73746d616e266c6f676f436f6c6f723d7768697465)

------

# 4. 모델링


![image](https://user-images.githubusercontent.com/88086271/143210573-310ab152-01ae-44aa-862d-47adea3034ff.png)



------

# 5. Postman API 테스트

### API 테스트 : https://www.postman.com/grey-comet-304334/workspace/cardoc

### 기본 주소는 배포주소로 되어 있으며, 콜렉션 fork 후 테스트 부탁드립니다.

### API 명세서 : https://documenter.getpostman.com/view/17716434/UVJYLKfD#9b26edd8-6cb8-40e6-80c0-951098afbbc6

------

# 6. 구현 사항 상세 설명

## 1. POST /users/signup (회원가입)

- username과 password를 body에서 받은 뒤 저장합니다.
- 일반적인 웹사이트에서 사용하는 ID는 username이라는 변수로 설정했습니다.
- 그에 따라 username은 중복되면 안되는 값이기 때문에 unique=True를 설정했습니다.
- 회원가입 시, username이 이미 존재하는 지 체크한 뒤 그에 따라 저장 혹은 에러가 발생하도록 되어 있습니다.
- 이상없다면 회원가입이 되며, 비밀번호는 암호화되도록 설정되었습니다.

## 2. POST /users/signin (로그인)

- 로그인 시 username, password의 일치여부를 판단하며 그에 따른 에러 핸들링도 되어 있습니다.
- 이상없다면, 로그인 시 토큰이 발급됩니다.

## 3. POST /trims (trim 추가)

- 사용자별 trim을 추가하는 로직입니다.
- 다만, 처음에는 로그인한 유저만 저장하는 줄 알았는데 예시에는 유저 아이디가 각기 달라서 로그인 유저 식별은 하지 않았습니다.
- 대신, 없는 유저이거나 trim일 경우 에러가 발생되도록 설정했습니다.
- 저장 시, 한 번에 5개 초과하여 저장할 수 없도록 해야한다는 과제를 반영하였고 모든 점검결과 이상없을 시 저장됩니다.

## 4. GET /trims (유저별 trim조회)

- 사용자별 trim을 조회하는 로직입니다.
- 특정 유저의 리스트를 봐야하기 때문에 유저 식별을 위한 login_required 함수가 우선실행되도록 설정되어 있습니다.

## 5. GET /trims/{int:trim_id} (trim별 조회)

- trim의 id를 Path Parameter로 입력 받아서 특정 trim의 데이터를 조회합니다.

------

# 7. UnitTest 결과

![image](https://user-images.githubusercontent.com/88086271/143210801-2ecc3265-bbdc-4876-9173-aee6ae02de8f.png)

# 8 . Reference

이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 카닥에서 출제한 과제를 기반으로 만들었습니다. 감사합니다.

