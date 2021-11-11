# Text adventure
To run the program, run "python3 final.py"


To run the tests, run "python3 final.py < input.txt" 

To win the game, you have to rescue your love by one of three ways:

1. Get the keys from the lion's den, break out your love from the dungeon, and escape through the treasury window.
2. Get documents from the treasury table, induce/stab the guard to render him inactive, go to the king's chamber and show the documents to blackmail him.
3. Threaten the king with a sword. Doing this however, you'd still have to go through everything in option 1.

Because the guard's loaction is being varied randomly, if you decide to win the game by threatening or blackmailing the king, it is your responsibility to always try to induce or stab the guard as long as the room descriptions say he is still active.

Functions/Commands:
General Commands (can be called at any location in the game):
“save” --> Saves the player’s current progress (inventory, location, state of other characters).
“load” --> Loads the player’s most recent saved game.
“stats” --> Gives the player details about their current locations and items in their inventory.
“induce” --> Induces the guard with chloroform. (can only be called in a location where the guard is present).
“stab guard” --> If a player has a sword in his/her inventory, Player stabs the guard with the sword and kills the guard instantly.
“close” --> Closes the game without saving progress.
 
Treasury Commands:
“open door” --> Sets the treasury door open.
“close door” --> Sets the treasury door close.
“look at shelf” --> Describes the shelf to the player.
“look at table” --> Describes the table to the player.
“pick bottle” --> Adds bottle of chloroform and handkerchief to player’s inventory.
“pick documents” --> Adds the king’s incriminating documents to the player’s inventory.
“escape” --> Player wins the game if with true love, loses the game if alone.
“go west” --> Moves player to hallway A when door is open.
 
Hallway A Commands:
“go east” --> Moves player to treasury.
“go north” --> Moves player to Weapons storage.
“go south” --> Moves player to lion’s den.
“move left” --> Moves player to hallway B.
 
Hallway B Commands:
“go north” --> Moves player to the dungeon.
“go west” --> Moves player to king’s chamber. Guard has to be induced prior.
“move right” --> Moves player to hallway A.
 
Weapons Storage Commands:
“look at shelf” --> Describes the shelf to the player.
“pick sword” --> Adds sword to player’s inventory.
“pick sling shot” --> Adds sling shot to player’s inventory.
“go south” --> Moves player to hallway A.
 
Dungeon Commands:
“open gate” --> Opens the gate if player has the keys in his/her inventory.
“rescue love” --> Player preps to leave the room with his/her true love.
“go south” --> Moves player and true love to hallway B, moves player only if “rescue love” command hasn’t been called.
 
Lion’s Den Commands:
“stab lion” --> Kills the lion instantly if player has a sword in his/her inventory.
“shoot lion” --> Lions health drops by 50% per shot.
“look at key” --> Describes key to player.
“pick key” --> Adds key to player’s inventory.
“go north” --> Moves player to hallway A.
 
King’s Chamber Commands:
“show documents” --> Player blackmails king with incriminating documents to win the game.
“threaten king” --> Player draws out his/her sword and threatens the king to release his/her true love.
“go east” --> Player leaves the king's chamber. If blackmail was used, wins the game. If threatening the king was used, continues the game (still has to get the key and break out his/her true love, then escape through the treasury window).
 
