// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SocialVault is Ownable {
    IERC20 public token;
    mapping(address => uint256) public shares;

    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 shares);

    constructor(address _token) Ownable(msg.sender) {
        token = IERC20(_token);
    }

    function deposit(uint256 amount) external {
        token.transferFrom(msg.sender, address(this), amount);
        shares[msg.sender] += amount; // uproszczone – w realu proporcjonalne
        emit Deposit(msg.sender, amount);
    }

    function withdraw(uint256 shareAmount) external {
        require(shares[msg.sender] >= shareAmount, "Insufficient shares");
        uint256 amount = shareAmount; // uproszczone
        shares[msg.sender] -= shareAmount;
        token.transfer(msg.sender, amount);
        emit Withdraw(msg.sender, shareAmount);
    }
}
