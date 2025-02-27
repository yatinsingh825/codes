import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import random
import json
import wikipedia
import requests
import subprocess
import time
import platform
import pytz

class VoiceAssistant:
    def __init__(self, name="Swift"):
        # Initialize the assistant
        self.name = name
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.wake_word = name.lower()
        
        # Set voice properties
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)  # Female voice
        self.engine.setProperty('rate', 180)  # Speed of speech
        
        # Initialize commands dictionary - keep these simple for basic matching
        self.commands = {
            "hello": self.hello,
            "time": self.handle_time_request,  # Changed to a general time handler
            "date": self.get_date,
            "search": self.search_web,
            "google": self.search_web,
            "open": self.open_application,
            "who is": self.wiki_search,
            "what is": self.handle_what_is,  # New general handler for "what is" questions
            "exit": self.exit_assistant,
            "goodbye": self.exit_assistant,
            "stop": self.exit_assistant
        }
        
        self.running = True
        self.active_mode = False
        
    def speak(self, text):
        """Convert text to speech"""
        print(f"{self.name}: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
        
    def listen(self, prompt=True):
        """Listen for user commands"""
        with sr.Microphone() as source:
            if prompt:
                print("Listening...")
            # Adjust for ambient noise
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                
                # Use Google's speech recognition
                command = self.recognizer.recognize_google(audio).lower()
                print(f"User: {command}")
                return command
            except sr.UnknownValueError:
                if prompt:
                    print("Sorry, I didn't understand that.")
                return ""
            except sr.RequestError:
                if prompt:
                    print("Speech service is currently unavailable.")
                return ""
            except:
                return ""
    
    def process_command(self, command):
        """Process the user's command with better natural language understanding"""
        # First, check for complex time queries with flexible phrasing
        if any(phrase in command for phrase in ["time in", "time at", "time it is in", "what time is it in", "what's the time in"]):
            self.get_time_zone(command)
            return True
            
        # Then check basic commands
        for key in self.commands:
            if key in command:
                self.commands[key](command)
                return True
                
        # If no command matches
        self.speak("I'm not sure how to help with that yet. Would you like me to search Google for this?")
        response = self.listen()
        if "yes" in response.lower() or "sure" in response.lower():
            self.search_web("search " + command)
        return True
    
    # Command functions
    def hello(self, command):
        """Greeting function"""
        responses = ["Hello! How can I help you?", 
                     "Hi there! What can I do for you?",
                     "Hey! How can I assist you today?"]
        self.speak(random.choice(responses))
    
    def handle_time_request(self, command):
        """General handler for time requests"""
        # Check if this is a time zone query
        if any(word in command for word in ["in", "at", "for"]):
            self.get_time_zone(command)
        else:
            # Just the local time
            self.get_time()
    
    def get_time(self):
        """Tell the current time"""
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        self.speak(f"The current local time is {current_time}")
    
    def handle_what_is(self, command):
        """Handle 'what is' questions with smarter parsing"""
        # Check if it's a time query
        if "time" in command:
            self.handle_time_request(command)
        else:
            # Otherwise treat as a Wikipedia question
            self.wiki_search(command)
    
    def get_time_zone(self, command):
        """Get time for a specific timezone/city with flexible input handling"""
        # Extract the location name with more flexible pattern matching
        location = ""
        for pattern in ["time in", "time at", "time it is in", "time is in", "what time is it in", "what's the time in"]:
            if pattern in command:
                location = command.replace(pattern, "").strip().lower()
                break
                
        if not location:
            # Try one more method - look for the last word after "time"
            if "time" in command:
                parts = command.split("time")[1].strip().split()
                if parts:
                    # Get everything after any prepositions
                    for i, word in enumerate(parts):
                        if word in ["in", "at", "for"]:
                            location = " ".join(parts[i+1:])
                            break
        
        if not location:
            self.speak("Please specify a city or timezone.")
            return
            
        # Common city to timezone mapping
        timezone_map = {
            "london": "Europe/London",
            "new york": "America/New_York",
            "los angeles": "America/Los_Angeles",
            "paris": "Europe/Paris",
            "tokyo": "Asia/Tokyo",
            "sydney": "Australia/Sydney",
            "berlin": "Europe/Berlin",
            "moscow": "Europe/Moscow",
            "beijing": "Asia/Shanghai",
            "dubai": "Asia/Dubai",
            "mumbai": "Asia/Kolkata",
            "singapore": "Asia/Singapore",
            "toronto": "America/Toronto",
            "shanghai": "Asia/Shanghai",
            "sao paulo": "America/Sao_Paulo",
            "mexico city": "America/Mexico_City",
            "cairo": "Africa/Cairo",
            "johannesburg": "Africa/Johannesburg",
            "madrid": "Europe/Madrid",
            "rome": "Europe/Rome"
        }
        
        try:
            # Check if the location is in our map
            if location in timezone_map:
                tz = pytz.timezone(timezone_map[location])
                current_time = datetime.datetime.now(tz).strftime("%I:%M %p")
                self.speak(f"The current time in {location.title()} is {current_time}")
            else:
                # Try to use Google to get accurate time
                self.speak(f"I'll search for the current time in {location}")
                search_query = f"current time in {location}"
                url = f"https://www.google.com/search?q={search_query}"
                webbrowser.open(url)
                self.speak(f"I've opened a search for the current time in {location}")
        except Exception as e:
            self.speak(f"I'm having trouble finding the time for {location}. {str(e)}")
            self.search_web(f"search current time in {location}")
    
    def get_date(self, command):
        """Tell the current date"""
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        self.speak(f"Today is {current_date}")
 
    
    def search_web(self, command):
        """Search the web for a query"""
        if "google" in command:
            search_term = command.replace("google", "").strip()
        else:
            search_term = command.replace("search", "").strip()
            
        if search_term:
            url = f"https://www.google.com/search?q={search_term}"
            webbrowser.open(url)
            self.speak(f"Here's what I found for {search_term}")
        else:
            self.speak("What would you like me to search for?")
    
    def open_application(self, command):
        """Open an application"""
        app_name = command.replace("open", "").strip().lower()
        
        # Common applications dictionary with platform-specific commands
        windows_apps = {
            "notepad": "notepad.exe",
            "calculator": "calc.exe",
            "word": "winword.exe",
            "excel": "excel.exe",
            "powerpoint": "powerpnt.exe",
            "chrome": "chrome.exe",
            "firefox": "firefox.exe",
            "edge": "msedge.exe",
            "explorer": "explorer.exe",
            "paint": "mspaint.exe",
            "cmd": "cmd.exe",
            "control panel": "control.exe",
            "task manager": "taskmgr.exe",
            "settings": "ms-settings:",
            "vs code": "code.exe",
            "visual studio code": "code.exe",
            "note": "notepad.exe",
            "notes": "notepad.exe",
            "brave": "brave.exe",
            "clock":"clock.exe"

        }
        
        mac_apps = {
            "safari": "Safari",
            "chrome": "Google Chrome",
            "firefox": "Firefox",
            "terminal": "Terminal",
            "finder": "Finder",
            "calculator": "Calculator",
            "notes": "Notes",
            "note": "Notes",
            "calendar": "Calendar",
            "system preferences": "System Preferences",
            "music": "Music",
            "photos": "Photos",
            "vs code": "Visual Studio Code",
            "visual studio code": "Visual Studio Code"
        }
        
        # Try to open the application based on the OS
        system = platform.system()
        self.speak(f"Trying to open {app_name}")
        
        try:
            if system == "Windows":
                # First check if it's in our known apps list
                if app_name in windows_apps:
                    app_path = windows_apps[app_name]
                    self.speak(f"Opening {app_name}")
                    subprocess.Popen(app_path, shell=True)
                else:
                    # Try to open it directly by name
                    self.speak(f"Attempting to open {app_name}")
                    subprocess.Popen(app_name, shell=True)
            
            elif system == "Darwin":  # macOS
                if app_name in mac_apps:
                    subprocess.Popen(["open", "-a", mac_apps[app_name]])
                    self.speak(f"Opening {app_name}")
                else:
                    # Try to open it directly by name
                    subprocess.Popen(["open", "-a", app_name])
                    self.speak(f"Attempting to open {app_name}")
            
            elif system == "Linux":
                # For Linux, try to open using the command directly
                subprocess.Popen([app_name])
                self.speak(f"Attempting to open {app_name}")
                
        except Exception as e:
            self.speak(f"I couldn't open {app_name}. The error was: {str(e)}")
    
    def wiki_search(self, command):
        """Search Wikipedia for information"""
        # Determine if it's "who is" or "what is"
        if "who is" in command:
            query = command.replace("who is", "").strip()
            self.speak(f"Searching for information about {query}")
        else:
            query = command.replace("what is", "").strip()
            self.speak(f"Searching for information about {query}")
        
        try:
            # Set language to English
            wikipedia.set_lang("en")
            
            # Get a summary from Wikipedia
            summary = wikipedia.summary(query, sentences=2)
            
            # Speak the summary
            self.speak(summary)
            
            # Offer to search the web for more info
            self.speak("Would you like me to search the web for more information?")
            response = self.listen()
            
            if "yes" in response.lower() or "sure" in response.lower():
                url = f"https://www.google.com/search?q={query}"
                webbrowser.open(url)
                self.speak(f"Here's what I found about {query}")
                
        except wikipedia.exceptions.DisambiguationError as e:
            # Handle disambiguation
            self.speak(f"There are multiple results for {query}. Please be more specific.")
            options = e.options[:5]  # Limit to first 5 options
            self.speak(f"Some options are: {', '.join(options)}")
            
        except wikipedia.exceptions.PageError:
            # Handle page not found
            self.speak(f"I couldn't find any information about {query} on Wikipedia.")
            self.speak("Would you like me to search the web instead?")
            response = self.listen()
            
            if "yes" in response.lower() or "sure" in response.lower():
                url = f"https://www.google.com/search?q={query}"
                webbrowser.open(url)
                self.speak(f"Here's what I found about {query}")
                
        except Exception as e:
            self.speak(f"I encountered an error while searching for {query}. {str(e)}")
    
    def exit_assistant(self, command):
        """Exit the voice assistant"""
        self.speak("Goodbye! Have a great day!")
        self.running = False
    
    def run(self):
        """Main loop for the assistant"""
        self.speak(f"Hello, I'm {self.name}. Say my name to wake me up.")
        
        while self.running:
            if not self.active_mode:
                # Listen for wake word
                print("Listening for wake word...")
                wake_command = self.listen(prompt=False)
                
                # Check if wake word is in the command
                if self.wake_word in wake_command.lower():
                    self.speak(f"Yes, I'm here. How can I help you?")
                    self.active_mode = True
            else:
                # Already in active mode, listen for commands directly
                print("I'm in active mode. Tell me what you need.")
                command = self.listen()
                
                if command:
                    # If the user says "sleep" or "go to sleep", exit active mode
                    if "sleep" in command.lower() or "go to sleep" in command.lower():
                        self.speak("I'll be here if you need me. Just say my name.")
                        self.active_mode = False
                    else:
                        # Process the command
                        self.process_command(command)
            
            # Small delay to prevent excessive CPU usage
            time.sleep(0.1)

if __name__ == "__main__":
    assistant = VoiceAssistant("Swift")  # Named Swift
    assistant.run()