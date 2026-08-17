import streamlit as st
import pandas as pd
import altair as alt

# 대시보드 제목
st.title("매출 대시보드")

# 실습용 데이터 생성
data = pd.DataFrame({
    "지역": ["서울", "서울", "경기", "경기", "부산", "부산"],
    "월": ["1월", "2월", "1월", "2월", "1월", "2월"],
    "매출": [100, 300, 50, 140, 110, 30]
})

# 지역을 선택할 수 있는 드롭다운 생성
region = st.selectbox(
    "지역을 선택하세요",
    data["지역"].unique()
)

# 선택한 지역의 데이터만 필터링
filtered_data = data[data["지역"] == region]

# 선택한 지역의 데이터 출력
st.subheader(f"{region} 매출 현황")
st.dataframe(filtered_data)

# 전체 데이터의 최대 매출값 계산
max_sales = data["매출"].max()

# Altair를 활용한 막대 차트 생성
chart = alt.Chart(filtered_data).mark_bar().encode(
    x=alt.X("월:N", title="월"),
    y=alt.Y(
        "매출:Q",
        title="매출",
        # 모든 지역의 Y축 범위를 동일하게 설정
        scale=alt.Scale(domain=[0, max_sales])
    )
)

# Streamlit 화면에 차트 출력
st.altair_chart(chart, use_container_width=True)