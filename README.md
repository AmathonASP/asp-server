## Audio Streaming Player Backend

- ### Refer

  - ##### [HLS on naverD2](https://d2.naver.com/helloworld/7122)

  - ##### [ffmpeg DOCS](https://ffmpeg.org/ffmpeg-formats.html)

- ### Tech Stack

   - Python 3.6
   - Django 2.0

- 
  ### Member
   - #### 박정욱

   - #### 서장원

- ### 최소기능

  1. 음원 파일 업로드(음질 분할)
     1. 음질별로 파일 생성
     2. 320, 192, 128이하는 한개만
  2. 음원 파일 재생(auto)
     1. 인터넷 속도에 따른 음질 변화
  3. 음원 파일 리스트

- ### 추가기능

  1. 유저별 리스트
  2. 플레이리스트

- ### API

  - ##### `post` audios/

  - ##### `get` audios/

    - ##### `get` audios/<id>/

  - ##### 