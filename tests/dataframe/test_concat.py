from __future__ import annotations

import pytest


def test_simple_concat(make_df, with_morsel_size):
    import daft
    from daft.testing import assert_frame_equal

    df1 = make_df({"foo": [1, 2, 3]})
    df2 = make_df({"foo": [4, 5, 6]})
    result = df1.concat(df2)
    expected = daft.from_pydict({"foo": [1, 2, 3, 4, 5, 6]})
    assert_frame_equal(result, expected)


def test_concat_schema_mismatch(make_df, with_morsel_size):
    df1 = make_df({"foo": [1, 2, 3]})
    df2 = make_df({"foo": ["4", "5", "6"]})
    with pytest.raises(ValueError):
        df1.concat(df2)


def test_self_concat(make_df, with_morsel_size):
    import daft
    from daft.testing import assert_frame_equal

    df = make_df({"foo": [1, 2, 3]})
    expected = daft.from_pydict({"foo": [1, 2, 3, 1, 2, 3]})
    assert_frame_equal(df.concat(df), expected)
