import speech_recognition as sr
import os
import threading
import customtkinter as ctk
import webbrowser
import pywhatkit
from AppOpener import open as open_app

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class DCMSApp(ctk.CTk):
    def __init__ (self):
        super().__init__()

        # Window Configuration
        self.title("DCMS - Dynamic Command Management System")
        self.geometry("500x400")
        self.resizable(False, False)

        self.chat_display = ctk.CTkTextbox(self, width=400, height=300, font=("Consolas", 15))
        self.chat_display.pack(pady=10)
        self.chat_display.insert("0.0", "--SYSTEM INITIALIZED--\n")
        self.chat_display.configure(state="disabled")

        self.status_label = ctk.CTkLabel(self, text="Status: STANDBY (Say 'Dynamic' or 'DCMS')", font=("Consolas", 12))
        self.status_label.pack(pady=10)

        self.close_btn = ctk.CTkButton(self, text="Hide System", command=self.hide_window)
        self.close_btn.pack(pady=10)

        self.protocol("WM_DELETE_WINDOW", self.hide_window)

        self.is_awake = False
        self.silence_count = 0

        self.listen_thread = threading.Thread(target=self.start_listening)
        self.listen_thread.daemon = True
        self.listen_thread.start()

    def show_window(self):
        self.deiconify()
        self.lift()

    def hide_window(self):
        self.withdraw()

    # Update chat display with new messages
    def update_chat(self, sender, message):
        self.chat_display.configure(state="normal")
        self.chat_display.insert("end", f"{sender}: {message}\n")
        self.chat_display.see("end")
        self.chat_display.configure(state="disabled")

    # Command execution logic
    def execute_command(self, command):
        self.update_chat("You", command)
        response = ""
        self.status_label.configure(text="Processing command..., say 'sleep' or 'rest' to enter sleep mode, or 'shut down' to exit DCMS")

        if "shut down" in command or "stop" in command:
            response = "Shutting down DCMS. Goodbye Sir"
            self.update_chat("DCMS", response)
            self.quit()

        elif "sleep" in command or "rest" in command:
            response = "Entering sleep mode. Say 'Dynamic' or 'DCMS' to wake me up"
            self.update_chat("DCMS", response)
            self.is_awake = False
            self.status_label.configure(text="Status: STANDBY", text_color="white")
    
        elif "open" in command or "launch" in command:
            app_name = command.replace("open", "").replace("launch", "").strip()
            try:
                response = f"Opening {app_name}..."
                self.update_chat("DCMS", response)
                open_app(app_name, match_closest = True)
            except:
                response = f"Sorry, I couldn't find the application {app_name}."
                self.update_chat("DCMS", response)
                pass
    
        elif "play" in command:
            song_name = command.replace("play", "").strip()
            response = f"Playing {song_name} on Chrome YouTube..."
            self.update_chat("DCMS", response)
            pywhatkit.playonyt(song_name)

        elif "search" in command:
            query = command.replace("search", "").strip()
            response = f"Searching for {query} on Google..."
            self.update_chat("DCMS", response)
            webbrowser.open(f"https://www.google.com/search?q={query}")
            

    # Start listening for voice commands
    def start_listening(self):
        recognizer = sr.Recognizer()

        while True:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                try:
                    if not self.is_awake:
                        print("Background listening for activation phrase...")
                        audio = recognizer.listen(source, timeout = 5, phrase_time_limit = 5)
                        text = recognizer.recognize_google(audio).lower()

                        if "dcms" in text or "dynamic" in text:
                            print("Activation phrase detected.")
                            self.is_awake = True
                            self.silence_count = 0
                            self.after(0, self.show_window)
                            self.after(0, lambda: self.status_label.configure(text="Status: AWAKE", text_color="green"))
                            self.after(0, lambda: self.update_chat("DCMS", "I am now awake. How can I assist you?"))

                    else:
                        print("Active listening...")
                        audio = recognizer.listen(source, timeout = 5, phrase_time_limit = 7)
                        command = recognizer.recognize_google(audio).lower()
                        
                        self.silence_count = 0

                        self.after(0, lambda: self.execute_command(command))
                        
                
                except sr.WaitTimeoutError:
                    if self.is_awake:
                        self.silence_count += 1
                        print(f"Silence count: {self.silence_count}")
                        
                        if self.silence_count >= 3:
                            self.is_awake = False
                            self.after(0, lambda: self.update_chat("DCMS", "Entering sleep mode due to inactivity. Say 'Dynamic' or 'DCMS' to wake me up"))
                            self.after(0, lambda: self.status_label.configure(text="Status: STANDBY", text_color="white"))
                            self.after(10, self.hide_window)
                
                    

                except Exception as e:
                    pass

# Main entry point
if __name__ == "__main__":
    app = DCMSApp()
    app.mainloop()
            