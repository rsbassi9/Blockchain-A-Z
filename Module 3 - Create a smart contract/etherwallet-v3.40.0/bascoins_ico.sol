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

    // Getting the equity in Bascoins of an investor (external constant (now replaced by view / pure) means never modified, and is from outside the contract). 
    // The function just calls the mapping and returns the value mapped
    function equity_in_bascoins(address investor) external view returns (uint) {
        return equity_bascoins[investor];
    }

    // Getting the equity in USD of an investor 
    function equity_in_usd(address investor) external view returns (uint) {
        return equity_usd[investor];
    }

}