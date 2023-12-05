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
    // This mapping will take teh address of the investor as input, return an interger called equity_bascoins of the investor
    mapping(address => uint) equity_bascoins;
    mapping(address => uint) equity_USD;

}