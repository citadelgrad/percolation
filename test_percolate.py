import pytest

from percolate import Percolate


@pytest.fixture
def p_instance():
    yield Percolate()


def test_create_connection(p_instance):
    p_instance.create_connection(2, 3)
    assert p_instance.adjaceny_list == {2: {3}}


def test_create_multiple_connections(p_instance):
    p_instance.create_connection(2, 3)
    assert p_instance.adjaceny_list == {2: {3}}
    p_instance.create_connection(2, 5)
    p_instance.create_connection(2, 4)
    p_instance.create_connection(1, 3)
    assert p_instance.adjaceny_list[2] == {3, 4, 5}


def test_open_block(p_instance):
    assert not any(p_instance.block)
    opened = p_instance.open_block()
    assert len(opened) == 2
    assert any(p_instance.block)


# def test_main(p_instance):
#     assert p_instance.block_main()

def test_does_it_percolate(p_instance):
    assert p_instance.does_it_percolate()


def test_find_neighbors(p_instance):
    item_index = 2
    values = p_instance.find_neighbors(item_index)
    assert values[0] == 1
    assert values[1] == 3
    assert values[2] == (item_index - p_instance.ROW)
    assert values[3] == (item_index + p_instance.ROW)
