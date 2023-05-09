import streamlit as st
import pandas as pd
import time

def main():
    col1, col2, col3 = st.columns([5, 10, 1])
    df2 = pd.read_excel('230303-17_MQ_CGM.xlsx', skiprows=1,
                        sheet_name='Scanned_inputs')  # 读取scanned input sheet
    df2 = df2[["Device Timestamp", "Scan Glucose mg/dL", "Notes(Calories)", "Notes(Ingredients)"]]
    df2.columns = ["time", "glu", "calories", "ingredients"]
    df2.head() 
    temp = df2.dropna(subset=["ingredients", "calories"])
    temp["time_col"] = temp["time"].dt.strftime("%Y-%m-%d, %H:%M:%S")
    begin_date = pd.Timestamp('2023-03-03')
    end_date = pd.Timestamp('2023-03-10')

    temp = temp[temp['time'].between(begin_date, end_date)]
    date_range = pd.date_range(start=begin_date, periods=7, freq='D')
    for day_to_filter in date_range:
        single_df = temp[temp['time'].dt.date == day_to_filter.date()]
        with col1:
            st.subheader("day: {}".format(day_to_filter.date().strftime("%Y-%m-%d")))
        with col2:
            st.subheader("Activity")
        with col3:
            st.subheader(" Glucose ")
        for _, row in single_df.iterrows():
            with col1:
                st.write(row['time_col'])
            with col2:
                st.write(row['ingredients'])
            with col3:
                st.write(row["glu"])
            time.sleep(0.01)

if __name__ == "__main__":
    main()
