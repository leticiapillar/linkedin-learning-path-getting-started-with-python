# 
# Example file for parsing and processing XML
# LinkedIn Learning Python course by Joe Marini
#

import xml.dom.minidom

def main():
    # use the parse() function to load and parse an XML file
    doc = xml.dom.minidom.parse("samplexml.xml")
    
    # print out the document node and the name of the first child tag
    print(doc.nodeName)
    print(doc.firstChild.tagName)
    

    # get a list of XML tags from the document and print each one
    def list_skills(doc): 
        skills = doc.getElementsByTagName("skill")
        print(skills.length, "skills are listed")
        for skill in skills:
            print(skill.getAttribute("name"))

      
    # create a new XML tag and add it into the document
    def create_skill(doc):
        newSkill = doc.createElement("skill")
        newSkill.setAttribute("name", "Java")
        doc.firstChild.appendChild(newSkill)

    list_skills(doc)
    create_skill(doc)
    list_skills(doc)


if __name__ == "__main__":
    main()

