##### 기본 정보 입력 #####
import streamlit as st
# audiorecorder 패키지 추가
from audiorecorder import audiorecorder
# OpenAI 패키지 추가
import openai
# from openai import OpenAI
# 파일 삭제를 위한 패키지 추가
import os
# 시간 정보를 위한 패키지 추가
from datetime import datetime
# TTS 패키기 추가
from gtts import gTTS
# 음원 파일 재생을 위한 패키지 추가
import base64

##### 기능 구현 함수 #####
def STT(audio):
    # 파일 저장
    filename='input.mp3'
    audio.export(filename, format="mp3")
    # 음원 파일 열기
    audio_file = open(filename, "rb")
    # Whisper 모델을 활용해 텍스트 얻기
    # transcript = openai.Audio.transcribe("whisper-1", audio_file) -- open 1.0.0 이하
    transcript = openai.audio.translations.create(model = "whisper-1", file=audio_file)
    audio_file.close()
    # 파일 삭제
    os.remove(filename)
    return transcript.text

def ask_gpt(prompt, model):
    # response = openai.ChatCompletion.create(model=model, messages=prompt) -- openai 1.0.0 이하
    response = openai.chat.completions.create(model=model, messages=prompt)
    print(response.choices[0].message)
    # system_message = response["choices"][0]["message"]
    system_message = response.choices[0].message
    return system_message.content

def TTS(response, voice_type):
    responseAudio = openai.audio.speech.create(
        model="tts-1",
        voice= voice_type,
        input=response
    )
    filename = "output.mp3"
    responseAudio.stream_to_file(filename)
    # gTTS 를 활용하여 음성 파일 생성
    # filename = "output.mp3"
    # tts = gTTS(text=response,lang="ko")
    # tts.save(filename)

    # 음원 파일 자동 재생생
    with open(filename, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay="True">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md,unsafe_allow_html=True,)
    # 파일 삭제
    os.remove(filename)

def text_input_function(col1):
    with col1:
        st.subheader("text로 질문하기")
        question = st.text_input(label="QUESTION", placeholder="ENTER Your Question", value="", type="default")
        ok_clicked = st.button("OK")
        if ok_clicked and (len(question) > 0) and (st.session_state["check_reset"]==False):
            st.session_state["request"] = True
            now = datetime.now().strftime("%H:%M")
            st.session_state["chat"] += [("user",now, question)]
            st.session_state["messages"] += [{"role": "user", "content": question}]

def audio_input_function(col1):
    with col1:
        st.subheader("질문하기")
        audio = audiorecorder("클릭하여 녹음하기", "녹음중...")
        print(audio)
        if (audio.duration_seconds > 0) and (st.session_state["check_reset"]==False):
            st.audio(audio.export().read())
            st.session_state["request"] = True
            question = STT(audio)
            now = datetime.now().strftime("%H:%M")
            st.session_state["chat"] += [("user",now, question)]
            st.session_state["messages"] += [{"role": "user", "content": question}]

##### 메인 함수 #####
def main():
    # 기본 설정
    st.set_page_config(
        page_title="음성 비서 프로그램",
        layout="wide")

    # session state 초기화
    if "chat" not in st.session_state:
        st.session_state["chat"] = []

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "system", "content": "You are a thoughtful assistant. Respond to all input in 25 words and answer in korea"}]

    if "check_reset" not in st.session_state:
        st.session_state["check_reset"] = False

    if "request" not in st.session_state:
        st.session_state["request"] = False

    # 질문 모드 상태 초기화
    if "input_mode_prev" not in st.session_state:
        st.session_state["input_mode_prev"] = None

    # 제목
    st.header("음성 비서 프로그램")
    # 구분선
    st.markdown("---")

    # 기본 설명
    with st.expander("음성비서 프로그램에 관하여", expanded=True):
        st.write(
        """
        - 본 프로그램은 oepn AI의 whisper AI를 사용한 음성 비서 프로그랭빈디ㅏ.
        - 사용을 위해서는 자신이 보유한 OPEN AI KEY를 입력해야 합니다.
        - GPT 모델은 gpt-4와 gpt-3.5-turbo 중 선택할 수 있습니다.
        - 질문 모드는 text와 audio 중 선택할 수 있습니다.
        - text는 직접 텍스트를 입력하는 방식이고, audio는 음성으로 질문하는 방식입니다.
        - 질문 결과는 음성으로 제공됩니다.
        """
        )

        st.markdown("")

    # 사이드바 생성
    with st.sidebar:

        # Open AI API 키 입력받기
        openai.api_key = st.text_input(label="OPENAI API 키", placeholder="Enter Your API Key", value="", type="password")

        st.markdown("---")

        # GPT 모델을 선택하기 위한 라디오 버튼 생성
        model = st.radio(label="GPT 모델",options=["gpt-4", "gpt-3.5-turbo"])

        # 입력 모드 선택 (사이드바에 추가)
        input_mode = st.sidebar.radio("질문 모드 선택", ["text", "audio"], key="input_mode")

        # 입력 모드 선택 (사이드바에 추가)
        voice_type = st.sidebar.radio("음성 선택", ["nova",  "shimmer", "echo", "fable", "onyx", "alloy"], key="voice_type")

        st.markdown("---")

        # 모드가 변경되었는지 검사
        if st.session_state["input_mode_prev"] is not None and st.session_state["input_mode_prev"] != input_mode:
            # 모드가 변경되면 request 상태 초기화
            st.session_state["request"] = False

        # 현재 모드를 이전 모드로 저장
        st.session_state["input_mode_prev"] = input_mode

        # 리셋 버튼 생성
        if st.button(label="초기화"):
            # 리셋 코드
            st.session_state["chat"] = []
            st.session_state["messages"] = [{"role": "system", "content": "You are a thoughtful assistant. Respond to all input in 25 words and answer in korea"}]
            st.session_state["check_reset"] = True
            st.session_state["request"] = False

    # 기능 구현 공간
    col1, col2 =  st.columns(2)

    # 사용자가 선택한 입력 모드에 따라 다른 함수 실행
    if input_mode == "text":
        text_input_function(col1)
    elif input_mode == "audio":
        audio_input_function(col1)


    with col2:
        # 오른쪽 영역 작성
        st.subheader("질문/답변")
        if  (st.session_state["request"] == True )  and (st.session_state["check_reset"]==False):
            # ChatGPT에게 답변 얻기
            response = ask_gpt(st.session_state["messages"], model)

            # GPT 모델에 넣을 프롬프트를 위해 답변 내용 저장
            st.session_state["messages"] = st.session_state["messages"]+ [{"role": "system", "content": response}]

            # 채팅 시각화를 위한 답변 내용 저장
            now = datetime.now().strftime("%H:%M")
            st.session_state["chat"] = st.session_state["chat"]+ [("bot",now, response)]

            # 채팅 형식으로 시각화 하기
            for sender, time, message in st.session_state["chat"]:
                if sender == "user":
                    st.write(f'<div style="display:flex;align-items:center;"><div style="background-color:#007AFF;color:white;border-radius:12px;padding:8px 12px;margin-right:8px;">{message}</div><div style="font-size:0.8rem;color:gray;">{time}</div></div>', unsafe_allow_html=True)
                    st.write("")
                else:
                    st.write(f'<div style="display:flex;align-items:center;justify-content:flex-end;"><div style="background-color:lightgray;border-radius:12px;padding:8px 12px;margin-left:8px;">{message}</div><div style="font-size:0.8rem;color:gray;">{time}</div></div>', unsafe_allow_html=True)
                    st.write("")

            # gTTS 를 활용하여 음성 파일 생성 및 재생
            TTS(response, voice_type)
        else:
            st.session_state["check_reset"] = False

if __name__=="__main__":
    main()
