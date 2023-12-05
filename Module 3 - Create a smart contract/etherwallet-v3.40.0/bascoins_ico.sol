// Bascoins ICO

// SPDX-License-Identifier: GPL-3.0
// version of compiler
pragma solidity >=0.4.16 <0.9.0;

contract bascoin_ico {

    // Introducing the maximum number of bascoins available for sale
    uint public max_bascoins = 1000000;

    // Introducing the USD to Bascins conversion rate 1:1000
    uint public usd_to_bascoins = 1000;

    // Introducting the total number of Bascoins that have been bought by the investors. Initially = 0
    uint public total_bascoins_bought = 0; 
    
    // Mapping for the investor address to its equity in Bascoins and USD

    // A mapping is a function where the data is stored in an Array
    // This mapping will take the address of the investor as input, return an interger called equity_bascoins of the investor
    mapping(address => uint) equity_bascoins;
    mapping(address => uint) equity_usd;

    // Check if investor can buy Bascoins (if they are available for the amount they want to buy)
    modifier can_buy_bascoins(uint usd_invested){
        // Get the amount of bascoins that the investor wants to buy with their dollar amount + total bascoins already bought. This must be  < maximum no. of bascoins
        require (usd_invested * usd_to_bascoins + total_bascoins_bought <= max_bascoins);
        _;         
    }

    // Getting the equity in Bascoins of an investor (external:is from outside the contract.  view / pure: means never modified (a contstant) ). 
    // The function just calls the mapping and returns the value mapped
    function equity_in_bascoins(address investor) external view returns (uint) {
        return equity_bascoins[investor];
    }

    // Getting the equity in USD of an investor 
    function equity_in_usd(address investor) external view returns (uint) {
        return equity_usd[investor];
    }

    // Buying Bascoins
    // Apply the modifier to see if the investor is able to buy
    function buy_bascoins(address investor,uint usd_invested) external
    can_buy_bascoins(usd_invested) {  // Link the modifier before opening the {} for teh function
        uint bascoins_bought = usd_invested * usd_to_bascoins;
        equity_bascoins[investor] += bascoins_bought;
        equity_usd[investor] = equity_bascoins[investor] / 1000;  // divide bascoins equity by the price of them in USD to find USD equity
        total_bascoins_bought += bascoins_bought;  // update the total bascoins bought by adding the new investement
    }

    // Selling Bascoins
    function sell_bascoins(address investor,uint bascoins_to_sell) external {  
        equity_bascoins[investor] -= bascoins_to_sell; // Update the the investors balance
        equity_usd[investor] = equity_bascoins[investor] / 1000;  // divide bascoins equity by the price of them in USD to find USD equity
        total_bascoins_bought -= bascoins_to_sell;  // update the total bascoins bought by adding the new investement
    }

}