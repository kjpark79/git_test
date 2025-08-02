import streamlit as st

st.set_page_config(
    page_title="자기소개",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("👋 안녕하세요!")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("https://via.placeholder.com/300x300/4CAF50/white?text=프로필+사진", width=250)

with col2:
    st.header("김개발")
    st.subheader("🚀 웹 개발자")
    
    st.write("""
    안녕하세요! 저는 웹 개발에 열정을 가진 개발자입니다.
    새로운 기술을 배우고 적용하는 것을 좋아하며, 
    사용자 경험을 개선하는 것에 관심이 많습니다.
    """)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.header("🎓 학력")
    st.write("• 컴퓨터공학과 학사")
    st.write("• 2020년 졸업")

with col2:
    st.header("💼 경력")
    st.write("• 웹 개발자 (2021-현재)")
    st.write("• 프론트엔드 개발")
    st.write("• 백엔드 개발")

with col3:
    st.header("🛠️ 기술 스택")
    st.write("• Python")
    st.write("• JavaScript")
    st.write("• React")
    st.write("• Django")
    st.write("• Streamlit")

st.divider()

st.header("📁 프로젝트")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🛒 쇼핑몰 웹사이트")
    st.write("React와 Django를 사용한 풀스택 쇼핑몰")
    st.write("**기술**: React, Django, PostgreSQL")
    
with col2:
    st.subheader("📊 데이터 분석 대시보드")
    st.write("Streamlit을 활용한 실시간 데이터 시각화")
    st.write("**기술**: Python, Streamlit, Pandas")

st.divider()

st.header("📞 연락처")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("📧 **이메일**")
    st.write("example@email.com")

with col2:
    st.write("📱 **GitHub**")
    st.write("[github.com/username](https://github.com)")

with col3:
    st.write("💼 **LinkedIn**")
    st.write("[linkedin.com/in/username](https://linkedin.com)")

st.divider()

st.header("💭 한마디")
st.info("항상 배움의 자세로 성장하는 개발자가 되겠습니다!")

with st.expander("더 많은 정보"):
    st.write("""
    **취미**: 독서, 영화감상, 코딩
    
    **관심 분야**: 
    - 웹 개발
    - 데이터 사이언스
    - 인공지능
    - 클라우드 컴퓨팅
    
    **목표**: 
    사용자에게 가치있는 서비스를 제공하는 개발자가 되는 것입니다.
    """)