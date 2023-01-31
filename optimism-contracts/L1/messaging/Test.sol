// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

/**
 * @title L1CrossDomainMessenger
 * @dev The L1 Cross Domain Messenger contract sends messages from L1 to L2, and relays messages
 * from L2 onto L1. In the event that a message sent from L1 to L2 is rejected for exceeding the L2
 * epoch gas limit, it can be resubmitted via this contract's replay function.
 *
 */
contract EventListener {
    event WithdrawalInitiated(
        address indexed _l1Token,
        address indexed _l2Token,
        address indexed _from,
        address _to,
        uint256 _amount,
        bytes _data
    );

    event DepositFinalized(
        address indexed _l1Token,
        address indexed _l2Token,
        address indexed _from,
        address _to,
        uint256 _amount,
        bytes _data
    );

    event DepositFailed(
        address indexed _l1Token,
        address indexed _l2Token,
        address indexed _from,
        address _to,
        uint256 _amount,
        bytes _data
    );

    event AddressSet(string indexed _name, address _newAddress, address _oldAddress);

    event StandardL2TokenCreated(address indexed _l1Token, address indexed _l2Token);

    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    //CREATE functions to emit all events using default values
    function emitWithdrawalInitiated() public {
        emit WithdrawalInitiated(address(0), address(0), address(0), address(0), 0, bytes(""));
    }

    function emitDepositFinalized() public {
        emit DepositFinalized(address(0), address(0), address(0), address(0), 0, bytes(""));
    }

    function emitDepositFailed() public {
        emit DepositFailed(address(0), address(0), address(0), address(0), 0, bytes(""));
    }

    function emitAddressSet() public {
        emit AddressSet("", address(0), address(0));
    }

    function emitStandardL2TokenCreated() public {
        emit StandardL2TokenCreated(address(0), address(0));
    }

    function emitOwnershipTransferred() public {
        emit OwnershipTransferred(address(0), address(0));
    }
}
