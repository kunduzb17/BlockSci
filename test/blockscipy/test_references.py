from test_addresses import ADDR_TYPES


def test_block_references(chain):
    for i in range(1, len(chain)):
        assert chain[i-1] == chain[i].prev_block


def test_tx_references(chain, json_data):
    for addr_type in ADDR_TYPES:
        for i in range(3):
            tx = chain.tx_with_hash(json_data["address-{}-spend-{}-tx".format(addr_type, i)])
            height = json_data["address-{}-spend-{}-height".format(addr_type, i)]

            assert chain[height] == tx.block


def test_output_references(chain, json_data):
    for addr_type in ADDR_TYPES:
        for i in range(3):
            tx = chain.tx_with_hash(json_data["address-{}-spend-{}-tx".format(addr_type, i)])
            height = json_data["address-{}-spend-{}-height".format(addr_type, i)]

            for j in range(tx.output_count):
                assert tx == tx.outputs[j].tx
                assert chain[height] == tx.outputs[j].tx.block


def test_spending_tx_references(chain, json_data):
    for i in range(8):
        tx = chain.tx_with_hash(json_data["tx-chain-10-tx-{}".format(i)])
        next_tx = chain.tx_with_hash(json_data["tx-chain-10-tx-{}".format(i + 1)])

        assert next_tx == tx.outputs[0].spending_tx
        assert tx == next_tx.inputs[0].spent_tx


def test_address_references(chain, json_data):
    for addr_type in ADDR_TYPES:
        for i in range(2):
            addr = chain.address_from_string(json_data["address-{}-spend-{}".format(addr_type, i)])
            tx = chain.tx_with_hash(json_data["address-{}-spend-{}-tx".format(addr_type, i)])
            height = json_data["address-{}-spend-{}-height".format(addr_type, i)]

            for j in range(i):
                assert tx == addr.outs.to_list()[j].tx
                assert chain[height] == addr.outs.to_list()[j].tx.block