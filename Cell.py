class Cell:
  def __init__(self):
    self.isPickUp = False
    self.isDropOff = False
    self.numBlocks = 0
    self.qValueNorth = 0
    self.qValueEast = 0
    self.qValueSouth = 0
    self.qValueWest = 0

  def pickUpBlock(self):
    if(self.isPickUp and self.numBlocks > 0):
      self.numBlocks -= 1

  def dropOffBlock(self):
    if(self.isDropOff and self.numBlocks < 5):
      self.numBlocks += 1
      
  def canPickUpBlock(self):
    if (self.isPickUp and self.numBlocks > 0):
      return True
    return False

  def canDropOffBlock(self):
    if(self.isDropOff and self.numBlocks < 5):
      return True
    return False
