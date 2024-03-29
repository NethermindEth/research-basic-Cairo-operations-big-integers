import asyncio
import os
import pytest
from starkware.starknet.testing.starknet import Starknet
from starkware.starknet.compiler.compile import compile_starknet_files

# Some test fixtures are defined here

UINT256_CONTRACT = os.path.join("contracts", "uint256_contract.cairo")
UINT384_CONTRACT = os.path.join("contracts", "uint384_contract.cairo")
UINT384_EXTENSION_CONTRACT = os.path.join(
    "contracts", "uint384_extension_contract.cairo"
)
FIELD_ARITHMETIC_CONTRACT = os.path.join("contracts", "field_arithmetic_contract.cairo")


@pytest.fixture(scope="module")
def event_loop():
    return asyncio.new_event_loop()


@pytest.fixture(scope="module")
async def starknet_factory():
    starknet = await Starknet.empty()
    return starknet


@pytest.fixture(scope="module")
async def uint256_contract(starknet_factory):
    starknet = starknet_factory
    # Deploy the account contract
    # contract_class = compile_starknet_files(
    #     files=[UINT384_CONTRACT], disable_hint_validation=True
    # )
    contract = await starknet.deploy(source=UINT256_CONTRACT,disable_hint_validation=True)
    return contract


@pytest.fixture(scope="module")
async def uint384_contract(starknet_factory):
    starknet = starknet_factory
    # Deploy the account contract
    # contract_class = compile_starknet_files(
    #     files=[UINT384_CONTRACT], disable_hint_validation=True
    # )
    contract = await starknet.deploy(source=UINT384_CONTRACT,disable_hint_validation=True)
    return contract


@pytest.fixture(scope="module")
async def uint384_extension_contract(starknet_factory):
    starknet = starknet_factory
    # Deploy the account contract
    # contract_class = compile_starknet_files(
    #     files=[UINT384_EXTENSION_CONTRACT], disable_hint_validation=True
    # )
    contract = await starknet.deploy(source=UINT384_EXTENSION_CONTRACT,disable_hint_validation=True)
    return contract


@pytest.fixture(scope="module")
async def field_arithmetic_contract(starknet_factory):
    starknet = starknet_factory
    # Deploy the account contract
    # contract_class = compile_starknet_files(
    #     files=[FIELD_ARITHMETIC_CONTRACT], disable_hint_validation=True
    # )
    contract = await starknet.deploy(source=FIELD_ARITHMETIC_CONTRACT,disable_hint_validation=True)
    return contract
