from linked_list import Node, LinkedList
from blossom_lib import flower_definitions 

##################################################################
flower_definitions = [
['begonia', 'cautiousness'],
['chrysanthemum', 'cheerfulness'],
['carnation', 'memories'],
['daisy', 'innocence'],
['hyacinth', 'playfulness'],
['lavender', 'devotion'],
['magnolia', 'dignity'],
['morning glory', 'unrequited love'],
['periwinkle', 'new friendship'],
['poppy', 'rest'], ['rose', 'love'],
['snapdragon', 'grace'],
['sunflower', 'longevity'],
['wisteria', 'good luck']
]
##################################################################

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for x in range(size)]

  def hash(self, key):
    return sum(key.encode())

  def compress(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    
    for item in list_at_array:
      if key == item[0]:
        item[1] = value
        return
    list_at_array.insert(payload)
        

  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    
    for record in list_at_index:
      if record[0] == key:
        return record[1]
      return None

blossom = HashMap(len(flower_definitions))
for record in flower_definitions:
  blossom.assign(record[0], record[1])

print(blossom.retrieve('daisy'))
