class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}\n{self.content}"
    
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all(self):
        return self.posts

    def posts_by_author(self, author):
        return [p for p in self.posts if p.author == author]

    def delete_post(self, title):
        for p in self.posts:
            if p.title == title:
                self.posts.remove(p)
                return "Post deleted."
        return "Post not found."

    def edit_post(self, title, new_content):
        for p in self.posts:
            if p.title == title:
                p.content = new_content
                return "Post updated."
        return "Post not found."

    def latest_posts(self, count=5):
        return self.posts[-count:]


def main():
    blog = Blog()

    while True:
        print("\n1. Add Post")
        print("2. List All Posts")
        print("3. Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Show Latest Posts")
        print("7. Exit")

        ch = input("Choose: ")

        if ch == "1":
            title = input("Title: ")
            content = input("Content: ")
            author = input("Author: ")
            blog.add_post(Post(title, content, author))
            print("Post added.")

        elif ch == "2":
            for p in blog.list_all():
                print(p)

        elif ch == "3":
            author = input("Author: ")
            for p in blog.posts_by_author(author):
                print(p)

        elif ch == "4":
            t = input("Title to delete: ")
            print(blog.delete_post(t))

        elif ch == "5":
            t = input("Title to edit: ")
            c = input("New content: ")
            print(blog.edit_post(t, c))

        elif ch == "6":
            for p in blog.latest_posts():
                print(p)

        elif ch == "7":
            break






    class Account:
    def __init__(self, number, owner, balance=0):
        self.number = number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def __str__(self):
        return f"{self.number} | {self.owner} | Balance: {self.balance}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc):
        self.accounts[acc.number] = acc

    def get(self, number):
        return self.accounts.get(number)

    def transfer(self, from_acc, to_acc, amount):
        a = self.get(from_acc)
        b = self.get(to_acc)
        if not a or not b:
            return False
        if not a.withdraw(amount):
            return False
        b.deposit(amount)
        return True


def main():
    bank = Bank()

    while True:
        print("\n1) Create account")
        print("2) Check balance")
        print("3) Deposit")
        print("4) Withdraw")
        print("5) Transfer")
        print("6) Show account")
        print("7) Exit")

        c = input("Select: ")

        if c == "1":
            num = input("Account number: ")
            name = input("Owner name: ")
            bal = int(input("Initial balance: "))
            bank.create_account(Account(num, name, bal))
            print("Created.")

        elif c == "2":
            num = input("Account number: ")
            acc = bank.get(num)
            print(acc.balance if acc else "Not found.")

        elif c == "3":
            num = input("Account number: ")
            amt = int(input("Amount: "))
            acc = bank.get(num)
            if acc:
                acc.deposit(amt)
                print("OK.")
            else:
                print("Not found.")

        elif c == "4":
            num = input("Account number: ")
            amt = int(input("Amount: "))
            acc = bank.get(num)
            if acc and acc.withdraw(amt):
                print("Withdrawn.")
            else:
                print("Error.")

        elif c == "5":
            f = input("From: ")
            t = input("To: ")
            amt = int(input("Amount: "))
            print("Done." if bank.transfer(f, t, amt) else "Transfer failed.")

        elif c == "6":
            num = input("Account number: ")
            acc = bank.get(num)
            print(acc if acc else "Not found.")

        elif c == "7":
            break


