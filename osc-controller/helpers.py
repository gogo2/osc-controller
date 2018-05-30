from collections import Iterable

from pythonosc import osc_bundle_builder
from pythonosc.osc_message_builder import OscMessageBuilder


def osc_message(address, args):
    builder = OscMessageBuilder(address)
    if not isinstance(args, Iterable) or isinstance(args, (str, bytes)):
        args = [args]
    for arg in args:
        builder.add_arg(arg)
    return builder.build()


def osc_bundle(contents):
    builder = osc_bundle_builder.OscBundleBuilder(osc_bundle_builder.IMMEDIATELY)
    for content in contents:
        builder.add_content(content)
    return builder.build()
