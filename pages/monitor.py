import streamlit as st
from monitor.monitor_center import MonitorCenter
import pandas as pd


@st.experimental_fragment(run_every="1s")
def show_processes():
    MonitorCenter.update_processes()
    processes = MonitorCenter.get_processes()

    data = {
        "Name": [process.name for process in processes],
        "PID": [process.pid for process in processes],
        "Username": [process.username for process in processes],
        "CPU %": [process.cpu_percent for process in processes],
        "Memory %": [process.memory_percent for process in processes],
        "Status": [process.status for process in processes],
    }
    df = pd.DataFrame(data)
    st.write(df)


@st.experimental_fragment()
def terminate_process():
    st.write("Terminate process")
    pid = st.number_input("PID", value=0, step=1, min_value=0, max_value=9999999999)
    if pid:
        st.button("terminate", on_click=MonitorCenter.terminate_process, args=(pid,))


@st.experimental_fragment()
def terminate_all_process():
    st.write("Terminate all processes")
    st.button("Terminate all", on_click=MonitorCenter.terminate_all_processes)


show_processes()
st.markdown("---")

terminate_process()
st.markdown("---")

terminate_all_process()
