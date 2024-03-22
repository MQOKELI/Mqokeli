books = []
members = []

def add_book(book_id, title, Author):

    books.append({
        book_id:2024001,

        title:"Python Programming",

        Author:"Jacob Zuma"
    })

    def add_member(member_id, name):
      
      members.append({
       member_id:1,

       name:"Anelisa Maleka"
       })
      
      add_book(2024001, "Python Programming", "Jacob Zuma")
      add_member(1, "Anelisa Maleka")

      print("The booklist" + books)
      print("The memberlist" + members)