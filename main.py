def get_nested_value(obj, key):

    """
    This function retrieves a value from a nested dict given a slash-delimited key string. If key is empty, it returns the input object and raises exceptions if any of the test cases defined below fail.
    """

    if obj is None and key != "":
        raise KeyError("Object is None")
    if obj is None and key == "":
        return None
    if key == "":
        return obj

    parts = key.split('/')
    current = obj

    for part in parts:
        if not isinstance(current, dict):
            raise KeyError(f"Cannot descend into '{part}' in path '{key}': not a dict")
        if part not in current:
            raise KeyError(f"Key '{part}' not found in path '{key}'")
        current = current[part]

    return current

def run_tests() -> None:
    """
    Test suite for get_nested_value function.
    Tests basic functionality, edge cases, and error conditions.
    """
    # Test basic nested access
    obj1 = {"a": {"b": {"c": "d"}}}
    assert get_nested_value(obj1, "a/b/c") == "d", "Basic nested access failed"

    obj2 = {"x": {"y": {"z": "a"}}}
    assert get_nested_value(obj2, "x/y/z") == "a", "Basic nested access failed"

    # Test simple key access
    obj3 = {"k": "v"}
    assert get_nested_value(obj3, "k") == "v", "Simple key access failed"

    # Test empty key
    obj4 = {"any": {"thing": 123}}
    assert get_nested_value(obj4, "") is obj4, "Empty key should return original object"

    # Test error cases
    _test_missing_key()
    _test_not_a_dict()
    _test_none_values()
    _test_trailing_slash()
    _test_empty_key_path()

    print("All tests passed!")

def _test_missing_key() -> None:
    """Test handling of missing keys"""
    try:
        get_nested_value({"a": {"b": {"c": "d"}}}, "a/x/c")
        raise AssertionError("KeyError for missing key")
    except KeyError as e:
        pass

def _test_not_a_dict() -> None:
    """Test handling of non-dict intermediate values"""
    try:
        get_nested_value({"a": {"b": "not_a_dict"}}, "a/b/c")
        raise AssertionError("KeyError for non-dict intermediate")
    except KeyError:
        pass

def _test_none_values() -> None:
    """Test handling of None values"""
    obj5 = {"a": {"b": None}}
    assert get_nested_value(obj5, "a/b") is None, "Should handle None values"
    assert get_nested_value(None, "") is None, "Should handle None input"
    try:
        get_nested_value(None, "a")
        raise AssertionError("KeyError for None obj with non-empty key")
    except KeyError:
        pass

def _test_trailing_slash() -> None:
    """Test handling of trailing slashes"""
    try:
        get_nested_value({"a": {"b": "c"}}, "a/b/")
        raise AssertionError("KeyError for trailing slash")
    except KeyError:
        pass

def _test_empty_key_path() -> None:
    """Test handling of empty key components"""
    obj7 = {"": {"a": "b"}}
    assert get_nested_value(obj7, "/a") == "b", "Should handle empty key components"

if __name__ == "__main__":
    run_tests()