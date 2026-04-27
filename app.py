import streamlit as st
import pandas as pd

# 标题
st.title("全国100城房地产数据分析与评估平台（Demo）")

# 模拟5城数据
data = {
    "城市": ["北京", "成都", "武汉", "潍坊", "芜湖"],
    "行政区": ["海淀", "锦江", "洪山", "奎文", "镜湖"],
    "均价": [60000, 18000, 15000, 7000, 9000],
    "建成年代": [2010, 2015, 2012, 2008, 2016],
    "容积率": [2.8, 3.0, 2.5, 2.2, 2.6],
    "物业类型": ["住宅", "住宅", "住宅", "住宅", "住宅"]
}
df = pd.DataFrame(data)

# 城市选择
city = st.selectbox("选择城市", df["城市"].unique())
filtered = df[df["城市"] == city]

st.subheader("城市数据")
st.dataframe(filtered)

# 评估功能
st.subheader("简易市场比较法评估")
area = st.number_input("面积(㎡)", value=90)
price = filtered["均价"].values[0]
total = area * price

st.write(f"评估单价：{price} 元/㎡")
st.write(f"评估总价：{total} 元")

st.caption("本Demo为课程作业，数据为模拟脱敏数据")
