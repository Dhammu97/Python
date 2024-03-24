# Coffee Machine Program Requirements
<ol>
<li>
 Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
<ul>
<li>Check the user’s input to decide what to do next.</li>
<li> The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer.</li>
</ul>



<li>Turn off the Coffee Machine by entering “off” to the prompt.</li>
<ul>
<li>For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens.
</li>
</ul>

<li>Print report.</li>
<ul>
<li>When the user enters “report” to the prompt, a report should be generated that shows the current resource values. </li>
<li>e.g.<br>
Water: 100ml<br>
Milk: 50ml<br>
Coffee: 76g<br>
Money: $2.5
</ul>

<li>Check resources sufficient?</li>
<ul>
<li>When the user chooses a drink, the program should check if there are enough resources to make that drink.</li>

<li>E.g. <br>
if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “Sorry there is not enough water.”

<li> The same should happen if another resource is depleted, e.g. milk or coffee.</li>
</ul>


<li>Process coins.</li>
<ul>
<li>If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.</li>
</ul>


<li>Check transaction successful?</li>
<ul>
<li>Check that the user has inserted enough money to purchase the drink they selected.</li>
<li>E.g. <br>
Latte cost $2.50, but they only inserted $0.52 then after counting the coins the<br>
program should say “Sorry that's not enough money. Money refunded.”.</li>

<li> But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered. </li>
E.g.<br>
Water: 100ml<br>
Milk: 50ml<br>
Coffee: 76g<br>
Money: $2.5<br>

If the user has inserted too much money, the machine should offer change.<br>
<li>E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
places.</li>
</ul>

<li>Make Coffee.</li>
<ul> 
<li>If the transaction is successful and there are enough resources to make the drink the
user selected, then the ingredients to make the drink should be deducted from the
coffee machine resources.</li>

<li>E.g. report before purchasing latte:<br>
Water: 300ml<br>
Milk: 200ml<br>
Coffee: 100g<br>
Money: $0<br>
</li>
<li>Report after purchasing latte:<br>
Water: 100ml<br>
Milk: 50ml <br>
Coffee: 76g <br>
Money: $2.5 <br>
</li>
<li>Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
latte was their choice of drink</li>
</ul>