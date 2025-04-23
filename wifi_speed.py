import tkinter as tk
from tkinter import ttk
import speedtest
import threading

def run_speedtest():
    def test():
        status_label.config(text="🔄 Test in corso...")
        st = speedtest.Speedtest()
        st.get_best_server()
        download = st.download() / 1_000_000
        upload = st.upload() / 1_000_000
        ping = st.results.ping

        download_label.config(text=f"📥 Download: {download:.2f} Mbps")
        upload_label.config(text=f"📤 Upload: {upload:.2f} Mbps")
        ping_label.config(text=f"🏓 Ping: {ping:.2f} ms")
        status_label.config(text="✅ Test completato!")

    threading.Thread(target=test).start()

# Interfaccia grafica
app = tk.Tk()
app.title("SpeedTest Wi-Fi")
app.geometry("350x250")
app.resizable(False, False)

title_label = ttk.Label(app, text="SpeedTest Wi-Fi", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

status_label = ttk.Label(app, text="Premi il pulsante per iniziare", font=("Arial", 10))
status_label.pack(pady=5)

download_label = ttk.Label(app, text="📥 Download: -", font=("Arial", 12))
download_label.pack(pady=5)

upload_label = ttk.Label(app, text="📤 Upload: -", font=("Arial", 12))
upload_label.pack(pady=5)

ping_label = ttk.Label(app, text="🏓 Ping: -", font=("Arial", 12))
ping_label.pack(pady=5)

start_button = ttk.Button(app, text="Avvia SpeedTest", command=run_speedtest)
start_button.pack(pady=10)

app.mainloop()
