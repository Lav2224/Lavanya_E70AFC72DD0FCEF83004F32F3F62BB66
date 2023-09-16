class Player:
  def play(self):
    print("The Player is Playing Cricket.")
class Batsman(Player):
  def play(self):
    print("The Batsman is Batting.")
class Bowler(Player):
  def play(self):
    print("The Bowler is Bowling.")

Batsman = Batsman()
Bowler = Bowler()

Batsman.play()
Bowler.play()