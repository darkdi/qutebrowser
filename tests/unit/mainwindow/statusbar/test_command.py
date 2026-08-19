# SPDX-FileCopyrightText: Dmitry <45711841+darkdi@users.noreply.github.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import pytest

from qutebrowser.mainwindow.statusbar import command


@pytest.mark.parametrize(('action', 'method'), [
    ('clear', 'clear'),
    ('select-all', 'selectAll'),
    ('copy', 'copy'),
    ('cut', 'cut'),
    ('paste', 'paste'),
    ('undo', 'undo'),
    ('redo', 'redo'),
])
def test_cmd_action(mocker, action, method):
    cmd = mocker.MagicMock()

    command.Command.cmd_action(cmd, action)

    getattr(cmd, method).assert_called_once_with()
