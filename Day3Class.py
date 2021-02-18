class Developer:
    languages = ["C","C++","Java","Python"]

    def code(self,language):
        if language in self.languages:
            print ("code in <",language,">")

    def resume(self):
        for lang in self.languages:
            print(lang)

developer = Developer()
developer.code("Python")            
developer.resume()

class SrDeveloper(Developer):
    def review(self):
        print("Review method")
        for lang in self.languages:
            if len(lang) < 4:
                print(lang)
        

senior = SrDeveloper()
senior.review()

class TechLead(SrDeveloper):
    def design(self):
        print("Design method")

lead = TechLead()
lead.design()
