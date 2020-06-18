"""
Author: Jeff Bella
Summary:
    Building out an auction house application for testing purposes

"""

class Art:
  def __init__(self, artist, title, medium, year):
    self.artist = artist
    self. title = title
    self.medium = medium
    self.year = year

  def __repr__(self):
    return f"{self.artist},  {self.title}, {self.year}, {self.medium}"

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "1910", "oil on canvas")

class Marketplace:
  def __init__(self, listings):
    self.listings = listings
  
  def __repr__(self):
    return f"listings are : {self.listings}"
  def add_listing(self, new_listing):
    return self.listings.append(new_listing)
  def remove_listing(self, listing):
    return self.listings.remove(listing)

  def show_listings(self):
    for i in self.listings:
      print(f"{i}")

class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum
  def __repr__(self):
    return f"{self.name}, {self.location}, {self.is_museum}"

  
#declared variables
veneer = Marketplace([])
edytta = Client(name = "Edytta Halpirt", location = "unknown", is_museum = False )

#Testing
my_stuff = Marketplace(["one", "two"])
print(my_stuff)
#test add listing
my_stuff.add_listing("Three")
print(my_stuff)
#test remove listing
my_stuff.remove_listing("one")
print(my_stuff)
#test show listings
print(my_stuff.show_listings)
#test veneer
print(veneer)
#test edytta
print(edytta)