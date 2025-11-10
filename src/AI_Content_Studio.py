


from dotenv import load_dotenv
import google.generativeai as genai
import os
import datetime
import json

# Load environment variables
load_dotenv()

class AIContentStudio:
    def __init__(self):
        api_key = os.getenv("YOUR_API_KEY_HERE")
        if not api_key:
            print("❌ Please set YOUR_API_KEY_HERE in your .env file")
            exit()
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("models/gemini-2.0-flash-001")
        self.conversation_history = []
        
    def generate_content(self, prompt, content_type="email"):
        templates = {
            "email": "Write a professional email about: {topic}",
            "business_proposal": "Write a concise business proposal for: {topic}",
            "blog_post": "Write a engaging blog post introduction about: {topic}",
            "social_media": "Create 3 social media posts about: {topic}",
            "cover_letter": "Write a professional cover letter for: {topic}",
            "Summarize_text": "Please summarize the following text in 3 bullet points: {topic}"
        }
        
        full_prompt = templates.get(content_type, templates["email"]).format(topic=prompt)
        
        try:
            response = self.model.generate_content(full_prompt)
            
            # Store conversation history
            self.conversation_history.append({
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "type": content_type,
                "prompt": prompt,
                "response": response.text
            })
            
            return response.text
        except Exception as e:
            return f"❌ Error: {str(e)}"
    
    def show_menu(self):
        print("\n" + "="*50)
        print("🤖 AI CONTENT STUDIO")
        print("="*50)
        print("1. ✉️  Write Professional Email")
        print("2. 📊 Create Business Proposal")
        print("3. ✍️  Write Blog Post")
        print("4. 📱 Generate Social Media Content")
        print("5. 💼 Create Cover Letter")
        print("6. 📝 Summarize Text")
        print("7. 📜 View Generation History")
        print("8. 💾 Save History to File")
        print("9. 🚪 Exit")
        print("="*50)
    
    def view_history(self):
        if not self.conversation_history:
            print("\n📝 No generation history yet.")
            return
        
        print("\n📜 GENERATION HISTORY:")
        print("-" * 40)
        for i, item in enumerate(self.conversation_history, 1):
            print(f"{i}. [{item['timestamp']}] {item['type'].upper()}: {item['prompt'][:50]}...")
    
    def save_history(self):
        if not self.conversation_history:
            print("❌ No history to save.")
            return
        
        filename = f"ai_content_history_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("AI CONTENT STUDIO - GENERATION HISTORY\n")
                f.write("=" * 50 + "\n\n")
                
                for item in self.conversation_history:
                    f.write(f"Timestamp: {item['timestamp']}\n")
                    f.write(f"Type: {item['type'].upper()}\n")
                    f.write(f"Prompt: {item['prompt']}\n")
                    f.write(f"Response:\n{item['response']}\n")
                    f.write("-" * 50 + "\n\n")
            
            print(f"✅ History saved to: {filename}")
        except Exception as e:
            print(f"❌ Error saving file: {e}")


def main():
    studio = AIContentStudio()
    
    print("🚀 Welcome to AI Content Studio!")
    print("Your all-in-one AI content creation tool.")
    
    while True:
        studio.show_menu()
        choice = input("\n👉 Enter your choice (1-9): ").strip()
        
        if choice == '1':
            topic = input("📧 Enter email topic: ")
            result = studio.generate_content(topic, "email")
            print(f"\n--- AI-Generated Email ---\n{result}")
            
        elif choice == '2':
            topic = input("📊 Enter business proposal topic: ")
            result = studio.generate_content(topic, "business_proposal")
            print(f"\n--- Business Proposal ---\n{result}")
            
        elif choice == '3':
            topic = input("✍️  Enter blog post topic: ")
            result = studio.generate_content(topic, "blog_post")
            print(f"\n--- Blog Post ---\n{result}")
            
        elif choice == '4':
            topic = input("📱 Enter social media topic: ")
            result = studio.generate_content(topic, "social_media")
            print(f"\n--- Social Media Posts ---\n{result}")
            
        elif choice == '5':
            topic = input("💼 Enter cover letter context: ")
            result = studio.generate_content(topic, "cover_letter")
            print(f"\n--- Cover Letter ---\n{result}")
        
        elif choice == '6':
            topic = input("Enter the text to summarize: ")
            result = studio.generate_content(topic, "Summarize_text")
            print(f"\n--- Summary of text ---\n{result}")
            
        elif choice == '7':
            studio.view_history()
            
        elif choice == '8':
            studio.save_history()
            
        elif choice == '9':
            print("👋 Thank you for using AI Content Studio!")
            break
            
        else:
            print("❌ Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()