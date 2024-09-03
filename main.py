import streamlit as st
from langchain_community.document_loaders import YoutubeLoader
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

def get_youtube_subtitles(url):
    """유튜브 URL에서 자막을 추출하는 함수"""
    try:
        loader = YoutubeLoader.from_youtube_url(url, add_video_info=False)
        documents = loader.load()
        combined_content = "\n".join([doc.page_content for doc in documents])
        return combined_content
    except Exception as e:
        st.error(f"자막을 불러오는 중 오류가 발생했습니다: {e}")
        return None

def main():
    st.title("YouTube 자막 가져오기")
    
    st.write("""
    유튜브 URL을 입력하면 해당 영상의 자막을 가져옵니다.
    """)

    # 유저로부터 유튜브 URL 입력 받기
    youtube_url = st.text_input("유튜브 URL을 입력하세요:", "")
    
    if youtube_url:
        with st.spinner("자막을 불러오는 중..."):
            subtitles = get_youtube_subtitles(youtube_url)
            
            if subtitles:
                st.subheader("가져온 자막:")
                st.text_area("유튜브 자막", subtitles, height=300)

if __name__ == "__main__":
    main()
