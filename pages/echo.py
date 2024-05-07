import streamlit as st
import multiprocessing
import time
from monitor.monitor_center import MonitorCenter

st.markdown("# Echo 🎉")


def echo(text):
    count = 0
    while True:
        count += 1

        print(f"Echo: {text} - {multiprocessing.current_process().pid} - {count}")

        MonitorCenter.update_process_status(
            multiprocessing.current_process().pid, str(count)
        )

        time.sleep(1)


def start_process(text):
    p = multiprocessing.Process(target=echo, args=(text,))
    p.start()

    MonitorCenter.register_process(p.pid, text)

    p.join()


input = st.text_input("Enter text")
st.button("Submit my picks", on_click=start_process, args=(input,))
