from clrs.chapter15.huffman_code import (
    HuffmanNode,
    calc_freq,
    huffman_decode,
    huffman_encode,
    huffman_tree,
)


def test_calc_freq():
    freq = calc_freq("ABABA")

    assert freq[ord("A")] == 3
    assert freq[ord("B")] == 2


def test_huffman_tree_created():
    tree = huffman_tree("ABC")

    assert tree is not None
    assert isinstance(tree, HuffmanNode)


def test_encode_decode_short_string():
    text = "hello world"

    encoded, tree = huffman_encode(text)

    decoded = huffman_decode(encoded, tree)

    assert decoded == text


def test_encode_decode_single_character():
    text = "AAAAAA"

    encoded, tree = huffman_encode(text)

    decoded = huffman_decode(encoded, tree)

    assert decoded == text


def test_encode_decode_empty_string():
    text = ""

    encoded, tree = huffman_encode(text)

    decoded = huffman_decode(encoded, tree)

    assert decoded == text


def test_encode_decode_repeated_pattern():
    text = "ABABABABABABABAB"

    encoded, tree = huffman_encode(text)

    decoded = huffman_decode(encoded, tree)

    assert decoded == text


def test_encode_decode_longer_text():
    text = (
        "The quick brown fox jumps over the lazy dog. "
        "The quick brown fox jumps over the lazy dog."
    )

    encoded, tree = huffman_encode(text)

    decoded = huffman_decode(encoded, tree)

    assert decoded == text


def test_tree_generates_codes():
    tree = huffman_tree("AABBBCCCC")
    tree.build_codes(tree, "")

    assert ord("A") in tree.codes
    assert ord("B") in tree.codes
    assert ord("C") in tree.codes

    assert isinstance(tree.codes[ord("A")], str)
    assert isinstance(tree.codes[ord("B")], str)
    assert isinstance(tree.codes[ord("C")], str)


def test_encoded_output_is_not_empty():
    encoded, _ = huffman_encode("hello")

    assert len(encoded) > 0
