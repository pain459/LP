const Voting = artifacts.require("Voting");

module.exports = function(deployer) {
    deployer.deploy(Voting, 3); // Assuming 3 proposals
};
