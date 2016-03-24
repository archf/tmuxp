# -*- coding: utf-8 -*-
"""Test for tmuxp Server object.

tmuxp.tests.server
~~~~~~~~~~~~~~~~~~

"""

from __future__ import absolute_import, division, print_function, \
    with_statement, unicode_literals

import logging
import unittest

from tmuxp.testsuite import t
from tmuxp.testsuite.helpers import TmuxTestCase
from tmuxp import Server

logger = logging.getLogger(__name__)


class ServerTest(TmuxTestCase):

    def test_has_session(self):
        self.assertTrue(t.has_session(self.TEST_SESSION_NAME))
        self.assertFalse(t.has_session('asdf2314324321'))

    def test_socket_name(self):
        """ ``-L`` socket_name.

        ``-L`` socket_name  file name of socket. which will be stored in
               env TMUX_TMPDIR or /tmp if unset.)

        """
        myserver = Server(socket_name='test')

        self.assertEqual(myserver.socket_name, 'test')

    def test_socket_path(self):
        """ ``-S`` socket_path  (alternative path for server socket). """
        myserver = Server(socket_path='test')

        self.assertEqual(myserver.socket_path, 'test')

    def test_config(self):
        """ ``-f`` file for tmux(1) configuration. """
        myserver = Server(config_file='test')
        self.assertEqual(myserver.config_file, 'test')

    def test_256_colors(self):
        myserver = Server(colors=256)
        self.assertEqual(myserver.colors, 256)

        proc = myserver.cmd('list-servers')

        self.assertIn('-2', proc.cmd)
        self.assertNotIn('-8', proc.cmd)

    def test_88_colors(self):
        myserver = Server(colors=88)
        self.assertEqual(myserver.colors, 88)

        proc = myserver.cmd('list-servers')

        self.assertIn('-8', proc.cmd)
        self.assertNotIn('-2', proc.cmd)


class EnvironmentTest(TmuxTestCase):

    def test_show_environment(self):
        """Server.show_environment() returns dict."""
        vars = self.server.show_environment()
        self.assertIsInstance(vars, dict)

    def test_set_show_environment_single(self):
        """Set environment then Server.show_environment(key)."""
        self.server.set_environment('FOO', 'BAR')
        self.assertEqual('BAR', self.server.show_environment('FOO'))

        self.server.set_environment('FOO', 'DAR')
        self.assertEqual('DAR', self.server.show_environment('FOO'))

        self.assertEqual('DAR', self.server.show_environment()['FOO'])

    def test_show_environment_not_set(self):
        """Unset environment variable returns None."""
        self.assertEqual(None, self.server.show_environment('BAR'))


def suite():
    _suite = unittest.TestSuite()
    _suite.addTest(unittest.makeSuite(ServerTest))
    _suite.addTest(unittest.makeSuite(EnvironmentTest))
    return _suite
