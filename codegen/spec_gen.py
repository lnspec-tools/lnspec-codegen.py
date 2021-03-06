def towire_tlv_payload_amt_to_forward(value):
    _n = 0
    buf = bytes()
    value = {"amt_to_forward": value}
    buf += towire_tu64(value["amt_to_forward"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_tlv_payload_amt_to_forward(buffer):
    value = {}

    return value["amt_to_forward"], buffer


def towire_tlv_payload_outgoing_cltv_value(value):
    _n = 0
    buf = bytes()
    value = {"outgoing_cltv_value": value}
    buf += towire_tu32(value["outgoing_cltv_value"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_tlv_payload_outgoing_cltv_value(buffer):
    value = {}

    return value["outgoing_cltv_value"], buffer


def towire_tlv_payload_short_channel_id(value):
    _n = 0
    buf = bytes()
    value = {"short_channel_id": value}
    buf += towire_short_channel_id(value["short_channel_id"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_tlv_payload_short_channel_id(buffer):
    value = {}

    return value["short_channel_id"], buffer


def towire_tlv_payload_payment_data(value):
    _n = 0
    buf = bytes()
    for v in value["payment_secret"]:
        buf += towire_byte(v)
    buf += towire_payment_data.payment_secret(value["payment_secret"])
    _n += 1
    buf += towire_tu64(value["total_msat"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_tlv_payload_payment_data(buffer):
    value = {}

    return value, buffer


tlv_tlv_payload = {
    2: (
        "amt_to_forward",
        towire_tlv_payload_amt_to_forward,
        fromwire_tlv_payload_amt_to_forward,
    ),
    4: (
        "outgoing_cltv_value",
        towire_tlv_payload_outgoing_cltv_value,
        fromwire_tlv_payload_outgoing_cltv_value,
    ),
    6: (
        "short_channel_id",
        towire_tlv_payload_short_channel_id,
        fromwire_tlv_payload_short_channel_id,
    ),
    8: (
        "payment_data",
        towire_tlv_payload_payment_data,
        fromwire_tlv_payload_payment_data,
    ),
}


def towire_offer_chains(value):
    _n = 0
    buf = bytes()
    value = {"chains": value}
    for v in value["chains"]:
        buf += towire_chain_hash(v)
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_offer_chains(buffer):
    value = {}

    return value["chains"], buffer


def towire_offer_currency(value):
    _n = 0
    buf = bytes()
    value = {"iso4217": value}
    buf += towire_array_utf8(value["iso4217"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_offer_currency(buffer):
    value = {}

    return value["iso4217"], buffer


def towire_offer_amount(value):
    _n = 0
    buf = bytes()
    value = {"amount": value}
    buf += towire_tu64(value["amount"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_offer_amount(buffer):
    value = {}

    return value["amount"], buffer


def towire_offer_description(value):
    _n = 0
    buf = bytes()
    value = {"description": value}
    buf += towire_array_utf8(value["description"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_offer_description(buffer):
    value = {}

    return value["description"], buffer


def towire_offer_features(value):
    _n = 0
    buf = bytes()
    value = {"features": value}
    for v in value["features"]:
        buf += towire_byte(v)
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_offer_features(buffer):
    value = {}

    return value["features"], buffer


def towire_offer_absolute_expiry(value):
    _n = 0
    buf = bytes()
    value = {"seconds_from_epoch": value}
    buf += towire_tu64(value["seconds_from_epoch"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_offer_absolute_expiry(buffer):
    value = {}

    return value["seconds_from_epoch"], buffer


def towire_offer_paths(value):
    _n = 0
    buf = bytes()
    value = {"paths": value}
    for v in value["paths"]:
        buf += towire_blinded_path(v)
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_offer_paths(buffer):
    value = {}

    return value["paths"], buffer


def towire_offer_vendor(value):
    _n = 0
    buf = bytes()
    value = {"vendor": value}
    buf += towire_array_utf8(value["vendor"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_offer_vendor(buffer):
    value = {}

    return value["vendor"], buffer


def towire_offer_quantity_min(value):
    _n = 0
    buf = bytes()
    value = {"min": value}
    buf += towire_tu64(value["min"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_offer_quantity_min(buffer):
    value = {}

    return value["min"], buffer


def towire_offer_quantity_max(value):
    _n = 0
    buf = bytes()
    value = {"max": value}
    buf += towire_tu64(value["max"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_offer_quantity_max(buffer):
    value = {}

    return value["max"], buffer


def towire_offer_recurrence(value):
    _n = 0
    buf = bytes()
    buf += towire_byte(value["time_unit"])
    _n += 1
    buf += towire_tu32(value["period"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_offer_recurrence(buffer):
    value = {}

    return value, buffer


def towire_offer_recurrence_paywindow(value):
    _n = 0
    buf = bytes()
    buf += towire_u32(value["seconds_before"])
    _n += 1
    buf += towire_byte(value["proportional_amount"])
    _n += 1
    buf += towire_tu32(value["seconds_after"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_offer_recurrence_paywindow(buffer):
    value = {}

    return value, buffer


def towire_offer_recurrence_limit(value):
    _n = 0
    buf = bytes()
    value = {"max_period": value}
    buf += towire_tu32(value["max_period"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_offer_recurrence_limit(buffer):
    value = {}

    return value["max_period"], buffer


def towire_offer_recurrence_base(value):
    _n = 0
    buf = bytes()
    buf += towire_byte(value["start_any_period"])
    _n += 1
    buf += towire_tu64(value["basetime"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_offer_recurrence_base(buffer):
    value = {}

    return value, buffer


def towire_offer_node_id(value):
    _n = 0
    buf = bytes()
    value = {"node_id": value}
    buf += towire_point32(value["node_id"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_offer_node_id(buffer):
    value = {}

    return value["node_id"], buffer


def towire_offer_send_invoice(value):
    _n = 0
    buf = bytes()
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_offer_send_invoice(buffer):
    value = {}

    return value, buffer


def towire_offer_refund_for(value):
    _n = 0
    buf = bytes()
    value = {"refunded_payment_hash": value}
    buf += towire_sha256(value["refunded_payment_hash"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_offer_refund_for(buffer):
    value = {}

    return value["refunded_payment_hash"], buffer


def towire_offer_signature(value):
    _n = 0
    buf = bytes()
    value = {"sig": value}
    buf += towire_bip340sig(value["sig"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_offer_signature(buffer):
    value = {}

    return value["sig"], buffer


tlv_offer = {
    2: ("chains", towire_offer_chains, fromwire_offer_chains),
    6: ("currency", towire_offer_currency, fromwire_offer_currency),
    8: ("amount", towire_offer_amount, fromwire_offer_amount),
    10: ("description", towire_offer_description, fromwire_offer_description),
    12: ("features", towire_offer_features, fromwire_offer_features),
    14: (
        "absolute_expiry",
        towire_offer_absolute_expiry,
        fromwire_offer_absolute_expiry,
    ),
    16: ("paths", towire_offer_paths, fromwire_offer_paths),
    20: ("vendor", towire_offer_vendor, fromwire_offer_vendor),
    22: ("quantity_min", towire_offer_quantity_min, fromwire_offer_quantity_min),
    24: ("quantity_max", towire_offer_quantity_max, fromwire_offer_quantity_max),
    26: ("recurrence", towire_offer_recurrence, fromwire_offer_recurrence),
    64: (
        "recurrence_paywindow",
        towire_offer_recurrence_paywindow,
        fromwire_offer_recurrence_paywindow,
    ),
    66: (
        "recurrence_limit",
        towire_offer_recurrence_limit,
        fromwire_offer_recurrence_limit,
    ),
    28: (
        "recurrence_base",
        towire_offer_recurrence_base,
        fromwire_offer_recurrence_base,
    ),
    30: ("node_id", towire_offer_node_id, fromwire_offer_node_id),
    54: ("send_invoice", towire_offer_send_invoice, fromwire_offer_send_invoice),
    34: ("refund_for", towire_offer_refund_for, fromwire_offer_refund_for),
    240: ("signature", towire_offer_signature, fromwire_offer_signature),
}


def towire_invoice_request_chains(value):
    _n = 0
    buf = bytes()
    value = {"chains": value}
    for v in value["chains"]:
        buf += towire_chain_hash(v)
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_request_chains(buffer):
    value = {}

    return value["chains"], buffer


def towire_invoice_request_offer_id(value):
    _n = 0
    buf = bytes()
    value = {"offer_id": value}
    buf += towire_sha256(value["offer_id"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_request_offer_id(buffer):
    value = {}

    return value["offer_id"], buffer


def towire_invoice_request_amount(value):
    _n = 0
    buf = bytes()
    value = {"msat": value}
    buf += towire_tu64(value["msat"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_request_amount(buffer):
    value = {}

    return value["msat"], buffer


def towire_invoice_request_features(value):
    _n = 0
    buf = bytes()
    value = {"features": value}
    for v in value["features"]:
        buf += towire_byte(v)
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_request_features(buffer):
    value = {}

    return value["features"], buffer


def towire_invoice_request_quantity(value):
    _n = 0
    buf = bytes()
    value = {"quantity": value}
    buf += towire_tu64(value["quantity"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_request_quantity(buffer):
    value = {}

    return value["quantity"], buffer


def towire_invoice_request_recurrence_counter(value):
    _n = 0
    buf = bytes()
    value = {"counter": value}
    buf += towire_tu32(value["counter"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_request_recurrence_counter(buffer):
    value = {}

    return value["counter"], buffer


def towire_invoice_request_recurrence_start(value):
    _n = 0
    buf = bytes()
    value = {"period_offset": value}
    buf += towire_tu32(value["period_offset"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_request_recurrence_start(buffer):
    value = {}

    return value["period_offset"], buffer


def towire_invoice_request_payer_key(value):
    _n = 0
    buf = bytes()
    value = {"key": value}
    buf += towire_point32(value["key"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_request_payer_key(buffer):
    value = {}

    return value["key"], buffer


def towire_invoice_request_payer_note(value):
    _n = 0
    buf = bytes()
    value = {"note": value}
    buf += towire_array_utf8(value["note"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_request_payer_note(buffer):
    value = {}

    return value["note"], buffer


def towire_invoice_request_payer_info(value):
    _n = 0
    buf = bytes()
    value = {"blob": value}
    for v in value["blob"]:
        buf += towire_byte(v)
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_request_payer_info(buffer):
    value = {}

    return value["blob"], buffer


def towire_invoice_request_replace_invoice(value):
    _n = 0
    buf = bytes()
    value = {"payment_hash": value}
    buf += towire_sha256(value["payment_hash"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_request_replace_invoice(buffer):
    value = {}

    return value["payment_hash"], buffer


def towire_invoice_request_payer_signature(value):
    _n = 0
    buf = bytes()
    value = {"sig": value}
    buf += towire_bip340sig(value["sig"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_request_payer_signature(buffer):
    value = {}

    return value["sig"], buffer


tlv_invoice_request = {
    2: ("chains", towire_invoice_request_chains, fromwire_invoice_request_chains),
    4: ("offer_id", towire_invoice_request_offer_id, fromwire_invoice_request_offer_id),
    8: ("amount", towire_invoice_request_amount, fromwire_invoice_request_amount),
    12: (
        "features",
        towire_invoice_request_features,
        fromwire_invoice_request_features,
    ),
    32: (
        "quantity",
        towire_invoice_request_quantity,
        fromwire_invoice_request_quantity,
    ),
    36: (
        "recurrence_counter",
        towire_invoice_request_recurrence_counter,
        fromwire_invoice_request_recurrence_counter,
    ),
    68: (
        "recurrence_start",
        towire_invoice_request_recurrence_start,
        fromwire_invoice_request_recurrence_start,
    ),
    38: (
        "payer_key",
        towire_invoice_request_payer_key,
        fromwire_invoice_request_payer_key,
    ),
    39: (
        "payer_note",
        towire_invoice_request_payer_note,
        fromwire_invoice_request_payer_note,
    ),
    50: (
        "payer_info",
        towire_invoice_request_payer_info,
        fromwire_invoice_request_payer_info,
    ),
    56: (
        "replace_invoice",
        towire_invoice_request_replace_invoice,
        fromwire_invoice_request_replace_invoice,
    ),
    240: (
        "payer_signature",
        towire_invoice_request_payer_signature,
        fromwire_invoice_request_payer_signature,
    ),
}


def towire_invoice_chains(value):
    _n = 0
    buf = bytes()
    value = {"chains": value}
    for v in value["chains"]:
        buf += towire_chain_hash(v)
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_chains(buffer):
    value = {}

    return value["chains"], buffer


def towire_invoice_offer_id(value):
    _n = 0
    buf = bytes()
    value = {"offer_id": value}
    buf += towire_sha256(value["offer_id"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_offer_id(buffer):
    value = {}

    return value["offer_id"], buffer


def towire_invoice_amount(value):
    _n = 0
    buf = bytes()
    value = {"msat": value}
    buf += towire_tu64(value["msat"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_amount(buffer):
    value = {}

    return value["msat"], buffer


def towire_invoice_description(value):
    _n = 0
    buf = bytes()
    value = {"description": value}
    buf += towire_array_utf8(value["description"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_description(buffer):
    value = {}

    return value["description"], buffer


def towire_invoice_features(value):
    _n = 0
    buf = bytes()
    value = {"features": value}
    for v in value["features"]:
        buf += towire_byte(v)
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_features(buffer):
    value = {}

    return value["features"], buffer


def towire_invoice_paths(value):
    _n = 0
    buf = bytes()
    value = {"paths": value}
    for v in value["paths"]:
        buf += towire_blinded_path(v)
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_paths(buffer):
    value = {}

    return value["paths"], buffer


def towire_invoice_blindedpay(value):
    _n = 0
    buf = bytes()
    value = {"payinfo": value}
    for v in value["payinfo"]:
        buf += towire_blinded_payinfo(v)
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_blindedpay(buffer):
    value = {}

    return value["payinfo"], buffer


def towire_invoice_blinded_capacities(value):
    _n = 0
    buf = bytes()
    value = {"incoming_msat": value}
    for v in value["incoming_msat"]:
        buf += towire_u64(v)
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_blinded_capacities(buffer):
    value = {}

    return value["incoming_msat"], buffer


def towire_invoice_vendor(value):
    _n = 0
    buf = bytes()
    value = {"vendor": value}
    buf += towire_array_utf8(value["vendor"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_vendor(buffer):
    value = {}

    return value["vendor"], buffer


def towire_invoice_node_id(value):
    _n = 0
    buf = bytes()
    value = {"node_id": value}
    buf += towire_point32(value["node_id"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_node_id(buffer):
    value = {}

    return value["node_id"], buffer


def towire_invoice_quantity(value):
    _n = 0
    buf = bytes()
    value = {"quantity": value}
    buf += towire_tu64(value["quantity"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_quantity(buffer):
    value = {}

    return value["quantity"], buffer


def towire_invoice_refund_for(value):
    _n = 0
    buf = bytes()
    value = {"refunded_payment_hash": value}
    buf += towire_sha256(value["refunded_payment_hash"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_refund_for(buffer):
    value = {}

    return value["refunded_payment_hash"], buffer


def towire_invoice_recurrence_counter(value):
    _n = 0
    buf = bytes()
    value = {"counter": value}
    buf += towire_tu32(value["counter"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_recurrence_counter(buffer):
    value = {}

    return value["counter"], buffer


def towire_invoice_send_invoice(value):
    _n = 0
    buf = bytes()
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_send_invoice(buffer):
    value = {}

    return value, buffer


def towire_invoice_recurrence_start(value):
    _n = 0
    buf = bytes()
    value = {"period_offset": value}
    buf += towire_tu32(value["period_offset"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_recurrence_start(buffer):
    value = {}

    return value["period_offset"], buffer


def towire_invoice_recurrence_basetime(value):
    _n = 0
    buf = bytes()
    value = {"basetime": value}
    buf += towire_tu64(value["basetime"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_recurrence_basetime(buffer):
    value = {}

    return value["basetime"], buffer


def towire_invoice_payer_key(value):
    _n = 0
    buf = bytes()
    value = {"key": value}
    buf += towire_point32(value["key"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_payer_key(buffer):
    value = {}

    return value["key"], buffer


def towire_invoice_payer_note(value):
    _n = 0
    buf = bytes()
    value = {"note": value}
    buf += towire_array_utf8(value["note"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_payer_note(buffer):
    value = {}

    return value["note"], buffer


def towire_invoice_payer_info(value):
    _n = 0
    buf = bytes()
    value = {"blob": value}
    for v in value["blob"]:
        buf += towire_byte(v)
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_payer_info(buffer):
    value = {}

    return value["blob"], buffer


def towire_invoice_created_at(value):
    _n = 0
    buf = bytes()
    value = {"timestamp": value}
    buf += towire_tu64(value["timestamp"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_created_at(buffer):
    value = {}

    return value["timestamp"], buffer


def towire_invoice_payment_hash(value):
    _n = 0
    buf = bytes()
    value = {"payment_hash": value}
    buf += towire_sha256(value["payment_hash"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_payment_hash(buffer):
    value = {}

    return value["payment_hash"], buffer


def towire_invoice_relative_expiry(value):
    _n = 0
    buf = bytes()
    value = {"seconds_from_creation": value}
    buf += towire_tu32(value["seconds_from_creation"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_relative_expiry(buffer):
    value = {}

    return value["seconds_from_creation"], buffer


def towire_invoice_cltv(value):
    _n = 0
    buf = bytes()
    value = {"min_final_cltv_expiry": value}
    buf += towire_tu32(value["min_final_cltv_expiry"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_cltv(buffer):
    value = {}

    return value["min_final_cltv_expiry"], buffer


def towire_invoice_fallbacks(value):
    _n = 0
    buf = bytes()
    buf += towire_byte(len(value["fallbacks"]))
    _n += 1
    for v in value["fallbacks"]:
        buf += towire_fallback_address(v)
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_fallbacks(buffer):
    value = {}

    return value, buffer


def towire_invoice_refund_signature(value):
    _n = 0
    buf = bytes()
    value = {"payer_signature": value}
    buf += towire_bip340sig(value["payer_signature"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_refund_signature(buffer):
    value = {}

    return value["payer_signature"], buffer


def towire_invoice_replace_invoice(value):
    _n = 0
    buf = bytes()
    value = {"payment_hash": value}
    buf += towire_sha256(value["payment_hash"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_replace_invoice(buffer):
    value = {}

    return value["payment_hash"], buffer


def towire_invoice_signature(value):
    _n = 0
    buf = bytes()
    value = {"sig": value}
    buf += towire_bip340sig(value["sig"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_signature(buffer):
    value = {}

    return value["sig"], buffer


tlv_invoice = {
    2: ("chains", towire_invoice_chains, fromwire_invoice_chains),
    4: ("offer_id", towire_invoice_offer_id, fromwire_invoice_offer_id),
    8: ("amount", towire_invoice_amount, fromwire_invoice_amount),
    10: ("description", towire_invoice_description, fromwire_invoice_description),
    12: ("features", towire_invoice_features, fromwire_invoice_features),
    16: ("paths", towire_invoice_paths, fromwire_invoice_paths),
    18: ("blindedpay", towire_invoice_blindedpay, fromwire_invoice_blindedpay),
    19: (
        "blinded_capacities",
        towire_invoice_blinded_capacities,
        fromwire_invoice_blinded_capacities,
    ),
    20: ("vendor", towire_invoice_vendor, fromwire_invoice_vendor),
    30: ("node_id", towire_invoice_node_id, fromwire_invoice_node_id),
    32: ("quantity", towire_invoice_quantity, fromwire_invoice_quantity),
    34: ("refund_for", towire_invoice_refund_for, fromwire_invoice_refund_for),
    36: (
        "recurrence_counter",
        towire_invoice_recurrence_counter,
        fromwire_invoice_recurrence_counter,
    ),
    54: ("send_invoice", towire_invoice_send_invoice, fromwire_invoice_send_invoice),
    68: (
        "recurrence_start",
        towire_invoice_recurrence_start,
        fromwire_invoice_recurrence_start,
    ),
    64: (
        "recurrence_basetime",
        towire_invoice_recurrence_basetime,
        fromwire_invoice_recurrence_basetime,
    ),
    38: ("payer_key", towire_invoice_payer_key, fromwire_invoice_payer_key),
    39: ("payer_note", towire_invoice_payer_note, fromwire_invoice_payer_note),
    50: ("payer_info", towire_invoice_payer_info, fromwire_invoice_payer_info),
    40: ("created_at", towire_invoice_created_at, fromwire_invoice_created_at),
    42: ("payment_hash", towire_invoice_payment_hash, fromwire_invoice_payment_hash),
    44: (
        "relative_expiry",
        towire_invoice_relative_expiry,
        fromwire_invoice_relative_expiry,
    ),
    46: ("cltv", towire_invoice_cltv, fromwire_invoice_cltv),
    48: ("fallbacks", towire_invoice_fallbacks, fromwire_invoice_fallbacks),
    52: (
        "refund_signature",
        towire_invoice_refund_signature,
        fromwire_invoice_refund_signature,
    ),
    56: (
        "replace_invoice",
        towire_invoice_replace_invoice,
        fromwire_invoice_replace_invoice,
    ),
    240: ("signature", towire_invoice_signature, fromwire_invoice_signature),
}


def towire_invoice_error_erroneous_field(value):
    _n = 0
    buf = bytes()
    value = {"tlv_fieldnum": value}
    buf += towire_tu64(value["tlv_fieldnum"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_error_erroneous_field(buffer):
    value = {}

    return value["tlv_fieldnum"], buffer


def towire_invoice_error_suggested_value(value):
    _n = 0
    buf = bytes()
    value = {"value": value}
    for v in value["value"]:
        buf += towire_byte(v)
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_error_suggested_value(buffer):
    value = {}

    return value["value"], buffer


def towire_invoice_error_error(value):
    _n = 0
    buf = bytes()
    value = {"msg": value}
    buf += towire_array_utf8(value["msg"])
    _n += 1
    # Ensures there are no extra keys!
    assert len(value) == _n
    return buf


def fromwire_invoice_error_error(buffer):
    value = {}

    return value["msg"], buffer


tlv_invoice_error = {
    1: (
        "erroneous_field",
        towire_invoice_error_erroneous_field,
        fromwire_invoice_error_erroneous_field,
    ),
    3: (
        "suggested_value",
        towire_invoice_error_suggested_value,
        fromwire_invoice_error_suggested_value,
    ),
    5: ("error", towire_invoice_error_error, fromwire_invoice_error_error),
}


def towire_onionmsg_path(value):
    _n = 0
    buf = bytes()
    buf += towire_point(value["node_id"])
    _n += 1
    buf += towire_u16(len(value["enctlv"]))
    _n += 1
    for v in value["enctlv"]:
        buf += towire_byte(v)
    _n += 1
    assert len(value) == _n
    return buf


def fromwire_onionmsg_path(buffer):
    value = {}

    return value, buffer


def towire_blinded_path(value):
    _n = 0
    buf = bytes()
    buf += towire_point(value["blinding"])
    _n += 1
    buf += towire_u16(len(value["path"]))
    _n += 1
    for v in value["path"]:
        buf += towire_onionmsg_path(v)
    _n += 1
    assert len(value) == _n
    return buf


def fromwire_blinded_path(buffer):
    value = {}

    return value, buffer


def towire_blinded_payinfo(value):
    _n = 0
    buf = bytes()
    buf += towire_u32(value["fee_base_msat"])
    _n += 1
    buf += towire_u32(value["fee_proportional_millionths"])
    _n += 1
    buf += towire_u16(value["cltv_expiry_delta"])
    _n += 1
    buf += towire_u16(len(value["features"]))
    _n += 1
    for v in value["features"]:
        buf += towire_byte(v)
    _n += 1
    assert len(value) == _n
    return buf


def fromwire_blinded_payinfo(buffer):
    value = {}

    return value, buffer


def towire_fallback_address(value):
    _n = 0
    buf = bytes()
    buf += towire_byte(value["version"])
    _n += 1
    buf += towire_u16(len(value["address"]))
    _n += 1
    for v in value["address"]:
        buf += towire_byte(v)
    _n += 1
    assert len(value) == _n
    return buf


def fromwire_fallback_address(buffer):
    value = {}

    return value, buffer


def towire_invalid_realm(value):
    _n = 0
    buf = bytes()
    assert len(value) == _n
    return buf


def fromwire_invalid_realm(buffer):
    value = {}

    return value, buffer


def towire_temporary_node_failure(value):
    _n = 0
    buf = bytes()
    assert len(value) == _n
    return buf


def fromwire_temporary_node_failure(buffer):
    value = {}

    return value, buffer


def towire_permanent_node_failure(value):
    _n = 0
    buf = bytes()
    assert len(value) == _n
    return buf


def fromwire_permanent_node_failure(buffer):
    value = {}

    return value, buffer


def towire_required_node_feature_missing(value):
    _n = 0
    buf = bytes()
    assert len(value) == _n
    return buf


def fromwire_required_node_feature_missing(buffer):
    value = {}

    return value, buffer


def towire_invalid_onion_version(value):
    _n = 0
    buf = bytes()
    buf += towire_sha256(value["sha256_of_onion"])
    _n += 1
    assert len(value) == _n
    return buf


def fromwire_invalid_onion_version(buffer):
    value = {}

    return value, buffer


def towire_invalid_onion_hmac(value):
    _n = 0
    buf = bytes()
    buf += towire_sha256(value["sha256_of_onion"])
    _n += 1
    assert len(value) == _n
    return buf


def fromwire_invalid_onion_hmac(buffer):
    value = {}

    return value, buffer


def towire_invalid_onion_key(value):
    _n = 0
    buf = bytes()
    buf += towire_sha256(value["sha256_of_onion"])
    _n += 1
    assert len(value) == _n
    return buf


def fromwire_invalid_onion_key(buffer):
    value = {}

    return value, buffer


def towire_temporary_channel_failure(value):
    _n = 0
    buf = bytes()
    buf += towire_u16(len(value["channel_update"]))
    _n += 1
    for v in value["channel_update"]:
        buf += towire_byte(v)
    _n += 1
    assert len(value) == _n
    return buf


def fromwire_temporary_channel_failure(buffer):
    value = {}

    return value, buffer


def towire_permanent_channel_failure(value):
    _n = 0
    buf = bytes()
    assert len(value) == _n
    return buf


def fromwire_permanent_channel_failure(buffer):
    value = {}

    return value, buffer


def towire_required_channel_feature_missing(value):
    _n = 0
    buf = bytes()
    assert len(value) == _n
    return buf


def fromwire_required_channel_feature_missing(buffer):
    value = {}

    return value, buffer


def towire_unknown_next_peer(value):
    _n = 0
    buf = bytes()
    assert len(value) == _n
    return buf


def fromwire_unknown_next_peer(buffer):
    value = {}

    return value, buffer


def towire_amount_below_minimum(value):
    _n = 0
    buf = bytes()
    buf += towire_u64(value["htlc_msat"])
    _n += 1
    buf += towire_u16(len(value["channel_update"]))
    _n += 1
    for v in value["channel_update"]:
        buf += towire_byte(v)
    _n += 1
    assert len(value) == _n
    return buf


def fromwire_amount_below_minimum(buffer):
    value = {}

    return value, buffer


def towire_fee_insufficient(value):
    _n = 0
    buf = bytes()
    buf += towire_u64(value["htlc_msat"])
    _n += 1
    buf += towire_u16(len(value["channel_update"]))
    _n += 1
    for v in value["channel_update"]:
        buf += towire_byte(v)
    _n += 1
    assert len(value) == _n
    return buf


def fromwire_fee_insufficient(buffer):
    value = {}

    return value, buffer


def towire_incorrect_cltv_expiry(value):
    _n = 0
    buf = bytes()
    buf += towire_u32(value["cltv_expiry"])
    _n += 1
    buf += towire_u16(len(value["channel_update"]))
    _n += 1
    for v in value["channel_update"]:
        buf += towire_byte(v)
    _n += 1
    assert len(value) == _n
    return buf


def fromwire_incorrect_cltv_expiry(buffer):
    value = {}

    return value, buffer


def towire_expiry_too_soon(value):
    _n = 0
    buf = bytes()
    buf += towire_u16(len(value["channel_update"]))
    _n += 1
    for v in value["channel_update"]:
        buf += towire_byte(v)
    _n += 1
    assert len(value) == _n
    return buf


def fromwire_expiry_too_soon(buffer):
    value = {}

    return value, buffer


def towire_incorrect_or_unknown_payment_details(value):
    _n = 0
    buf = bytes()
    buf += towire_u64(value["htlc_msat"])
    _n += 1
    buf += towire_u32(value["height"])
    _n += 1
    assert len(value) == _n
    return buf


def fromwire_incorrect_or_unknown_payment_details(buffer):
    value = {}

    return value, buffer


def towire_final_incorrect_cltv_expiry(value):
    _n = 0
    buf = bytes()
    buf += towire_u32(value["cltv_expiry"])
    _n += 1
    assert len(value) == _n
    return buf


def fromwire_final_incorrect_cltv_expiry(buffer):
    value = {}

    return value, buffer


def towire_final_incorrect_htlc_amount(value):
    _n = 0
    buf = bytes()
    buf += towire_u64(value["incoming_htlc_amt"])
    _n += 1
    assert len(value) == _n
    return buf


def fromwire_final_incorrect_htlc_amount(buffer):
    value = {}

    return value, buffer


def towire_channel_disabled(value):
    _n = 0
    buf = bytes()
    buf += towire_u16(value["flags"])
    _n += 1
    buf += towire_u16(len(value["channel_update"]))
    _n += 1
    for v in value["channel_update"]:
        buf += towire_byte(v)
    _n += 1
    assert len(value) == _n
    return buf


def fromwire_channel_disabled(buffer):
    value = {}

    return value, buffer


def towire_expiry_too_far(value):
    _n = 0
    buf = bytes()
    assert len(value) == _n
    return buf


def fromwire_expiry_too_far(buffer):
    value = {}

    return value, buffer


def towire_invalid_onion_payload(value):
    _n = 0
    buf = bytes()
    buf += towire_bigsize(value["type"])
    _n += 1
    buf += towire_u16(value["offset"])
    _n += 1
    assert len(value) == _n
    return buf


def fromwire_invalid_onion_payload(buffer):
    value = {}

    return value, buffer


def towire_mpp_timeout(value):
    _n = 0
    buf = bytes()
    assert len(value) == _n
    return buf


def fromwire_mpp_timeout(buffer):
    value = {}

    return value, buffer
