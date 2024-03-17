# Welcome to BlackJack Project
<div>
 <img src="C:\Users\lenovo\OneDrive\Desktop\GitDemo\Python\BlackJack project\blackjack.png">
</div>        
<br>
<p><h3 style ="color:blue">#################### 😎 Our BlackJack House Rule #################### </h3></p>
<br>
<ul>
<li>The deck is unlimited in size.</li> 
<li>There are no jokers. </li>
<li>The Jack/Queen/King all count as 10.</li>
<li>The the Ace can count as 11 or 1.</li>
<li>Use the following list as the deck of cards:</li>
<li>cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]</li>
<li>The cards in the list have equal probability of being drawn.</li>
<li>Cards are not removed from the deck as they are drawn.</li>
</ul>
<br>
<p><h3 style ="color:blue">#################### 😎 Hints #################### </h3></p>
<ul>
<li>Create a deal_card() function that uses the List below to *return* a random card.
<strong>11 is the Ace.</strong></li>

<li>Create a function called calculate_score() that takes a List of cards as input and returns the score. 
<i>Look up the sum() function to help you do this.</i></li>

<li> Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().</li>

<li> Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins</li>

<li>Deal the user and computer 2 cards each using deal_card()</li>
<li>The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.</li>

<li>Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.</li>
<li>If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.</li>
<li>Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.</li>
<li>Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.</li>
</ul>