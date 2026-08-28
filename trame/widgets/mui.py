from trame_mui.widgets.mui import *  # noqa: F403


def initialize(server):
    from trame_mui import module

    server.enable_module(module)
