# models make it easy for displaying content

class User():
    def __init__(self, email, password, first_name, notes, images):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.notes = notes
        self.images = images
         

class Note():
    def __init__(self, id, email, user_name, date, data, visibility):
        self.id = id
        self.email = email
        self.user_name = user_name
        self.date = date
        self.data = data
        self.visibility = visibility


class Image():
    def __init__(self, user_name, images):
        self.user_name = user_name
        self.images = images

        