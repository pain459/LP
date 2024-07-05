pragma solidity ^0.8.0;

contract Voting {
    struct Voter {
        bool voted;
        uint vote;
    }

    mapping(address => Voter) public voters;
    uint[] public votes;
    address public admin;

    constructor(uint numProposals) {
        admin = msg.sender;
        votes.length = numProposals;
    }

    function vote(uint proposal) external {
        require(!voters[msg.sender].voted, "Already voted.");
        voters[msg.sender].voted = true;
        voters[msg.sender].vote = proposal;
        votes[proposal] += 1;
    }

    function getVotes() external view returns (uint[] memory) {
        return votes;
    }
}
