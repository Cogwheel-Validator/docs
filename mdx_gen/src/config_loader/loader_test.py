"""Test the config loader."""
from .loader import Config, validate_config


def test_validate_config() -> None:
    """Test the validate_config function."""
    config = Config(
        name="test",
        binary_name="test",
        home_dir="test",
        chain_id="test",
        minimum_gas_prices="test",
        validator_amount="test",
        path="test",
    )
    # Pass a dictionary with the config, as validate_config expects dict[str, Config]
    configs_dict = {"test": config}
    assert validate_config(configs_dict) == (True, None)
    # Empty dictionary should fail validation since no configs are provided
    result = validate_config({})
    assert not result[0]
    assert str(result[1]) == "No configs provided"
    # Test with a dict containig a config with one missing element
    # This returns an error because the path is missing
    # So this will block the script from running
    config_missing_element = Config(
        name="test",
        binary_name="test",
        home_dir="test",
        chain_id="test",
        minimum_gas_prices="test",
        validator_amount="test",
    )
    configs_dict = {"test": config_missing_element}
    result = validate_config(configs_dict)
    assert not result[0]
    assert str(result[1]) == "Config test is missing the following elements: ['path']"
