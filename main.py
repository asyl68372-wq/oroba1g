import os

code_content = """
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

Window.clearcolor = (0.05, 0.05, 0.05, 1)

class MyFullApp(App):
    def build(self):
        self.title = "Secret Database"
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        layout.add_widget(Label(text="نظام الاستعلام الكامل والفضائح", font_size=25, color=(1, 0, 1, 1), bold=True, size_hint_y=None, height=50))
        
        self.user_input = TextInput(hint_text="ادخل الاسم هنا...", multiline=False, size_hint_y=None, height=50, font_size=18)
        layout.add_widget(self.user_input)
        
        btn = Button(text="استعلام عادي", size_hint_y=None, height=60, background_color=(0, 0.7, 1, 1), font_size=20)
        btn.bind(on_press=self.search_main)
        layout.add_widget(btn)

        self.scandal_btn = Button(text="كشف المستور (Password Required)", size_hint_y=None, height=60, background_color=(1, 0, 0, 1), font_size=20)
        self.scandal_btn.bind(on_press=self.show_scandal)
        layout.add_widget(self.scandal_btn)
        
        scroll = ScrollView()
        self.result_label = Label(text="النتائج ستظهر هنا...", size_hint_y=None, halign="left", valign="top", font_size=16, color=(1, 1, 1, 1))
        self.result_label.bind(texture_size=self.result_label.setter('size'))
        scroll.add_widget(self.result_label)
        layout.add_widget(scroll)
        
        return layout

    def search_main(self, instance):
        user_name = self.user_input.text.lower().strip()
        boys_of_1 = ["feras, ammar, haitham ibrahim, haitham, youssef, shehab, sadiq, saleh, jalal, qusai, ahmed, rakan, jarrah, saif, khalid"]
        boys_of_2 = ["ashil, ahmad salim, ahmed atiq, amjid, hussein, suhail, saleh ghalib, salah, abdel salam, mohammed, mohab, yasser, hasan, jihad, abu bakr, omar, ahmed, ahmed munir, ahmed abdul aziz"]

        if user_name == "feras":
            res = "feras is a boy from first class\\nname: feras mohammed\\nage: 16\\nweight: 61\\nheight: 165\\nhobby: programming\\nnumber whatsapp: 01032927385\\nnumber phone: 01032927385\\nemail: asel238636@gmail.com\\npermanent address: giza/khatm almorslin\\nnumber of dependents: 0\\nhe is from: taiz\\nhe's have a brother? yes he is 9 years old"
        elif user_name == "ammar":
            res = "ammar is a boy from first class\\nname: ammar muhammad dagis\\nage: 15\\nweight: 45\\nheight: 165\\nhobby: not have\\nnumber whatsapp: 01552613993\\nnumber phone: 01552613993\\nemail: ammar768300@gmail.com\\npermanent address: duki beside the school\\nnumber of dependents: 0\\nhe is from: ibb\\nhe's have a brother? yes he is 25 years old his name is ahmed"
        elif user_name == "haitham ibrahim":
            res = "haitham ibrahim is a boy from first class\\nname: haitham ibrahim\\nage: 15\\nweight: 45\\nheight: 167\\nhobby: not have\\nnumber whatsapp: 01212847883\\nnumber phone: 01212847883\\nemail: not found\\npermanent address: duki\\nnumber of dependents: 0\\nhe is from: hadramout\\nreputation: he's have a bad reputation"
        elif user_name == "haitham":
            res = "haitham is a boy from first class\\nname: haitham mohammed\\nage: 15\\nweight: 45\\nheight: 167\\nhobby: not have\\nnumber whatsapp: 01068214750\\nnumber phone: 01068214750\\nemail: not found\\npermanent address: beside the school\\nnumber of dependents: 0\\nhe is from: taiz\\nreputation: he's have a normal reputation\\nhe's have a brother? yes his 22 years old\\nhe's have a sister? yes\\nhis father is a political"
        elif user_name == "youssef":
            res = "youssef is a boy from first class\\nname: youssef saeed\\nage: 15\\nweight: 50\\nheight: 175\\nhobby: take sometime with his friends\\nnumber whatsapp: 01557392552\\nnumber phone: 01557392552\\nemail: not found\\npermanent address: giza\\nnumber of dependents: 0\\nhe is from: ibb"
        elif user_name == "shehab":
            res = "shehab is a boy from first class\\nname: shehab anwer al-sharaabi\\nage: 15\\nweight: 50\\nheight: 160\\nhobby: fc zlatan\\nnumber whatsapp: 01558044110\\nnumber phone: 01558044110\\nemail: not found\\npermanent address: kit kat\\nnumber of dependents: 0\\nhe is from: taiz but he said ibb\\nreputation: he's have a normal reputation"
        elif user_name == "sadiq":
            res = "sadiq is a boy from first class\\nname: sadiq alabdaly\\nage: 16\\nweight: 52\\nheight: 175\\nhobby: talk to girls\\nnumber whatsapp: 01102869597\\nnumber phone: 01068248494\\nemail: not found\\npermanent address: hadaeq el maadi\\nnumber of dependents: 0\\nhe is from: al dalia\\nreputation: he's have a some bad reputation\\nhe's have a brother? yes 2 the first hi sname is ali alabdaly and the second is his name is moath alabdaly and he is a doctor"
        elif user_name == "saleh":
            res = "saleh is a boy from first class\\nname: saleh\\nage: 15\\nweight: 47\\nheight: 162\\nhobby: talk very much\\nnumber whatsapp: he's not have but he's use the number of his father: 01101644271\\nnumber phone: 01124979840\\nemail: not have\\npermanent address: first in faysal\\nnumber of dependents: 0\\nhe is from: egypt\\nreputation: he's have a somebad reputation\\nhe's have a brother? no he's only child in his family"
        elif user_name == "jalal":
            res = "jalal is a boy from first class\\nname: jalal ahmed\\nage: 16\\nweight: 55\\nheight: 167\\nhobby: stay in drugstore\\nnumber whatsapp: 01125086649\\nnumber phone: 01125086649\\nemail: not found\\npermanent address: tuabik\\nnumber of dependents: 0\\nhe is from: ibb\\nreputation: he's have a somegood reputation in somepeople\\nhe's have a brother? no"
        elif user_name == "qusai":
            res = "qusai is a boy from first class\\nname: qusai ammar\\nage: 16\\nweight: 55\\nheight: 167\\nhobby: us the phone and upgrade his project\\nnumber whatsapp: 01064539620\\nnumber phone: 01064539620\\nemail: not found\\npermanent address: tullabiyah or muhandiseen\\nnumber of dependents: 0\\nhe is from: sna'a\\nreputation: he's have a normal reputation\\nhe's have a brother? no\\nhe's have a sister? yes"
        elif user_name == "ahmed":
            res = "ahmed is a boy from first class\\nname: ahmed abdul aziz\\nage: 16\\nweight: 46\\nheight: 172\\nhobby: edit videos\\nnumber whatsapp: 01206649797\\nnumber phone: 01206649797 but now he's not working\\nemail: not found\\npermanent address: gsheikh zayed\\nnumber of dependents: 0\\nhe is from: hadramout\\nreputation: he's have a bad and angry reputation\\nhe's have a brother? yes his have 14 brother\\nhe's have a sister? yes with 14\\nhe's father married 2 women"
        elif user_name == "rakan":
            res = "rakan is a boy from first class\\nname: rakan ba wazir\\nage: 15\\nweight: 45\\nheight: 158\\nhobby: us snapchat\\nnumber whatsapp: 01559131882\\nnumber phone: 01559131882\\nemail: not found\\npermanent address: sheikh zayed\\nnumber of dependents: 0\\nhe is from: hadramout\\nreputation: he's have a good reputation\\nhe's have a brother? yes\\nhe's have a sister? yes"
        elif user_name == "jarrah":
            res = "jarrah is a boy from first class\\nname: jarrah\\nage: 16\\nweight: 50\\nheight: 165\\nhobby: his calculator\\nnumber whatsapp: 01004303262\\nnumber phone: 01004303262\\nemail: not found\\npermanent address: first in faysal\\nnumber of dependents: 0\\nhe is from: taiz\\nreputation: he's have a good reputation\\nhe's have a brother? yes\\nhe's have a sister? yes"
        elif user_name == "saif":
            res = "saif is a boy from first class\\nname: saif\\nage: 16\\nweight: 60\\nheight: 169\\nhobby: play football\\nnumber whatsapp: 01025699617\\nnumber phone: 01025699617\\nemail: not found\\npermanent address: faysal\\nnumber of dependents: 0\\nhe is from: aden\\nreputation: he's have a good reputation\\nhe's have a brother? yes his name is muhammed"
        elif user_name == "khalid":
            res = "khalid is a boy from first class\\nname: khalid mohammed\\nage: 17\\nweight: 49\\nheight: 173\\nhobby: smoking\\nnumber whatsapp: 01141665958\\nnumber phone: 01141665958\\nemail: not found\\npermanent address: faysal\\nnumber of dependents: 0\\nhe is from: aden\\nreputation: he's have a very bad reputation\\nhe's have a brother? yes\\nhe's have a sister? no"
        elif user_name == "al1":
            res = str(boys_of_1)
        elif user_name == "al2":
            res = str(boys_of_2)
        else:
            res = "*************************************************\\nالاسم غير موجود"
        self.result_label.text = res

    def show_scandal(self, instance):
        text = self.user_input.text.split(",")
        if len(text) < 2:
            self.result_label.text = "يرجى كتابة الباسورد ثم فاصلة ثم الاسم\\nمثال: ashil,sadiq"
            return
        password = text[0].strip()
        fdihaus = text[1].strip().lower()

        if password == "ashil":
            if fdihaus == "ashil":
                self.result_label.text = "ashil is a boy from second class\\n" + "*"*200
            elif fdihaus == "feras":
                self.result_label.text = "feras is a boy from first class\\n" + "*"*200
            elif fdihaus == "ammar":
                self.result_label.text = "ammar is a boy from first class\\nhe's have a very good reputation in his family and his friends.... try stay with him and he's have a good friends"
            elif fdihaus == "sadiq":
                self.result_label.text = "sadiq is a boy from first class\\nAll his talk about girls revolves around an Egyptian girl he's just toying with. His goal in life is to prove to people that he's better and richer than them, and that his father is better too. He and his brothers seem to have a good life, but they're suffering inside. Don't believe anything he says; he's a stupid kid who wants to play with schoolgirls and then embarrass them in front of his friends."
            else:
                self.result_label.text = "هذا الاسم ليس له فضيحة مسجلة"
        else:
            self.result_label.text = "الباسورد خطأ!"

if __name__ == '__main__':
    MyFullApp().run()
"""

with open("main.py", "w", encoding="utf-8") as f:
    f.write(code_content)

print("✅ DONE! All data and scandals are saved in main.py")
