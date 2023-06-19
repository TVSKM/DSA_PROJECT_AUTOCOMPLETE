import tkinter as tk
from tkinter import messagebox
class TrieGUI:
    def __init__(self, root):
        self.root = root
        self.build_trie()
        self.create_gui()
 
    def build_trie(self):
        self.trie = Trie()
        self.trie.buildtrie(grp)

    def create_gui(self):
        self.root.title("Trie Spell Checker")

        # Create and position the GUI elements
        self.label = tk.Label(self.root, text="Enter the word that you need to check spelling:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)

        self.button = tk.Button(self.root, text="Check Spelling", command=self.check_spelling)
        self.button.pack(pady=5)

    def check_spelling(self):
        word = self.entry.get()
        print(word)
        keyword = self.trie.search_keyword(word, grp)
        print(keyword)
        if keyword:
            messagebox.showinfo("Spell Checker", f"Did you mean: {keyword}?")
        else:
            messagebox.showinfo("Spell Checker", "No suggestions found!")

class Tnode:
    def __init__(self):
        self.isendword = False
        self.storetrie = {}
 
class Trie:
    def __init__(self):
        self.root = Tnode()

    def insertele(self, key):
        element = self.root
        for a in key: 
            if not element.storetrie.get(a):
                element.storetrie[a] = Tnode()
            element = element.storetrie[a]
        element.isendword = True

    def buildtrie(self, grp):
        for key, values in grp.items():
            for word in values:
                self.insertele(word)

    def search(self, w):
        element = self.root
        for i in w:
            if not element.storetrie.get(i):
                return False
            element = element.storetrie[i]
        return element.isendword

    def suggestionsRec(self, element, w, suggestions):
        if element.isendword:
            suggestions.append(w)
        for i, n in element.storetrie.items():
            self.suggestionsRec(n, w + i, suggestions)

    def spellchk(self, w):
        element = self.root
        tmp = 0
        for i in w:
            if not element.storetrie.get(i):
                suggestions = []
                self.suggestionsRec(element, w[0:tmp], suggestions)
                return suggestions
            tmp += 1
            element = element.storetrie[i]
        if not element.storetrie:
            return []
        suggestions = []
        self.suggestionsRec(element, w, suggestions)
        return suggestions

    def search_keyword(self, query, grp):
        if self.search(query):
            for k, v in grp.items():
                if query in v:
                    return k
        else:
            suggestions = self.spellchk(query)
            if suggestions:
                for suggestion in suggestions:
                    for k, v in grp.items():
                        if suggestion in v:
                            return


grp = {
    "Computer": ["comp", "compute", "com", "computers", "computing"],
    "Python": ["py", "pyth", "pytho", "pyt", "python", "pythn","py"],
    "Operating System" : ["os","OS","operating","systems","oprt"],
    "Data base management system":["data","manage","system","base"],
    "Data structure":["dta","structure","str"],
    "Advance programing":["ad","program","pro"],
    "Artificial intelligence ":["ar","intel","arti"],
    "Cyber security":["cy","sec","cyb"],
    "Internet of thing":["int","thi","inter",],
    
}


root = tk.Tk()


app = TrieGUI(root)


root.mainloop()

# print(grp.items())
print("Enter the word that you need to check spelling:")
key = input()
root = Trie()
root.buildtrie(grp)
print(root.search_keyword(key, grp))
